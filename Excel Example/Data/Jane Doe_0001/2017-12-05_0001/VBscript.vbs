
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
	Set xlBook = xlApp.Workbooks.Open("C:\Users\nbr\Desktop\Excel Example\Templates\ExcelTemplate.xlsx", 0, True) 

	'Load tsv file
	fileList=Array("Dynamic 1","Dynamic 2","Dynamic 3") 

	For each fileName in fileList
		connection = "TEXT;C:\Users\nbr\Desktop\Excel Example\Data\Jane Doe_0001\2017-12-05_0001\" + fileName + ".tsv"

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
	xlBook.SaveAs("C:\Users\nbr\Desktop\Excel Example\Data\Jane Doe_0001\2017-12-05_0001\Report.xlsx")

	'Uncomment this line to close Excel after running the macro:
	'xlApp.Quit 

	Set xlBook = Nothing 
	Set xlApp = Nothing

End Sub 