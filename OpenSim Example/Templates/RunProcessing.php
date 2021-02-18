<?php
$temp_dir = str_replace('\\','\\\\', $template_directory);
$work_dir = str_replace('\\','\\\\', $working_directory);

// Load xml file with session information
$xml = simplexml_load_file($working_directory . "session.xml");

// Create array with information about measurements
$measurements = array();
foreach( $xml->Session->Measurement as $meas )
{
    $measurement = array();
    $measurement["Type"] = (string)$meas["Type"];
    $measurement["Filename"] = (string)$meas["Filename"];
    foreach( $meas->Fields->children() as $field )
    {
        $measurement[$field->getName()] = (string)$field;
    }
    $measurements[] = $measurement;
}

// Run processing on each measurement
foreach($measurements as $m) {
	if($m["Used"] === "True") {
        $path_parts = pathinfo($m["Filename"]);
        print('Processing ' . $working_directory . $path_parts['filename'] .'.c3d');
        $last_line = system("python -c \"".
            "import os;".
            "os.chdir('" . $temp_dir . "');".
            "from qtm2opensim import convert_c3d;".
            "convert_c3d('" . $work_dir . "', '" . $path_parts['filename'] . ".c3d')".
            "\"", $return_value);
        if($return_value == 0)
            print(" ... Completed\n");
        else
            print(" ... ERROR " . $last_line . "\n");
    }
}
?> 