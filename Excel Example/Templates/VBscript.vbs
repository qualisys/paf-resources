<?
//Use PHP preprocessing to prepare variables
$xml_file=$working_directory . "session.xml";
include("template_xml.php");
$file_list = array();
foreach($measurements as $m)
{
	if($m["Used"] === "True" and $m["Measurement_type"] === "Dynamic")
	{
		$path_parts = pathinfo($m["Filename"]);
		$file_list[] = $path_parts['filename'];
	}
}
?>

Option Explicit

ExcelMacroExample

Sub ExcelMacroExample() 

	Dim xlApp 
	Dim xlBook 
	Dim connection
	Dim fileName
	Dim fileList

	'Start Excel and open template file
	Set xlApp = CreateObject("Excel.Application") 
	xlApp.Application.Visible = True 'Set to False if Excel should not be visible.
	Set xlBook = xlApp.Workbooks.Open("<?=$template_directory?>ExcelTemplate.xlsx", 0, True) 

	'Load tsv file
	<?
	echo('fileList=Array("' . implode('","', $file_list) . '")')
	?> 

	For each fileName in fileList
		connection = "TEXT;<?=$working_directory?>" + fileName + ".tsv"

		'Import marker data from each QTM file into a separate worksheet
		xlApp.Sheets(fileName).Select
		With xlApp.ActiveSheet.QueryTables.Add(connection,xlApp.ActiveSheet.Range("$A$1"))
			.Name = fileName
			.FieldNames = True
			.RowNumbers = False
			.FillAdjacentFormulas = False
			.PreserveFormatting = True
			.RefreshOnFileOpen = False
			.RefreshStyle = 1
			.SavePassword = False
			.SaveData = True
			.AdjustColumnWidth = False
			.RefreshPeriod = 0
			.TextFilePromptOnRefresh = False
			.TextFilePlatform = 850
			.TextFileStartRow = 1
			.TextFileParseType = 1
			.TextFileTextQualifier = 1
			.TextFileConsecutiveDelimiter = False
			.TextFileTabDelimiter = True
			.TextFileSemicolonDelimiter = False
			.TextFileCommaDelimiter = False
			.TextFileSpaceDelimiter = False
			.TextFileOtherDelimiter = "§"
			.TextFileColumnDataTypes = Array(1, 1)
			.TextFileTrailingMinusNumbers = True
			.Refresh False
		End With
	Next

	xlApp.Sheets("Charts").Select

	'Option to run additional macro that could contain more advanced processing steps. Excel template must be saved as .xlsm in that case:
	'xlApp.Run "ExcelTemplate.xlsm!Module1.MyMacro"

	xlApp.DisplayAlerts = False 'Set to False to hide Excel message when overwriting existing file.     
	xlBook.SaveAs("<?=$working_directory?>Report.xlsx")

	'Uncomment this line to close Excel after running the macro:
	'xlApp.Quit 

	Set xlBook = Nothing 
	Set xlApp = Nothing

End Sub 