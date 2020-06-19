<?php
$xml = simplexml_load_file($working_directory. 'session.xml');

//Subject fields
$subject = array();
$subject["Type"] = (string)$xml["Type"];

foreach( $xml->Fields->children() as $field )
{
    $subject[$field->getName()] = (string)$field;
}

//Session fields
$session = array();
$session["Type"] = (string)$xml->Session["Type"];
foreach( $xml->Session->Fields->children() as $field )
{
    $session[$field->getName()] = (string)$field;
}

//Measurements fields
$measurements = array();
$includes_noraxon = FALSE;
$includes_mega_me6000 = FALSE;
$includes_delsys_trigno = FALSE;

foreach( $xml->Session->Measurement as $meas )
{
    $measurement = array();
    $measurement["Type"] = (string)$meas["Type"];
    $measurement["Filename"] = (string)$meas["Filename"];
    foreach( $meas->Fields->children() as $field )
    {
        $measurement[$field->getName()] = (string)$field;
    }

    //Analog channel names (used files only)
    if (strcmp('True', $measurement["Used"]) == 0)
    {
        $settings_file = $working_directory . str_replace(".qtm", ".settings.xml", $measurement["Filename"]);
        if (file_exists($settings_file))
        {
            $settings = simplexml_load_file($settings_file);
            $channel = array();
            $channels = array();
            foreach( $settings->Channels->children() as $ch )
            {
                $channel["Board"] = (string)$ch["Board"];
                $channel["Name"] = (string)$ch["Name"];
                $channel["Number"] = (string)$ch["Number"];
                $channels[] = $channel;
                if (strcmp('Noraxon', $ch["Board"]) == 0) $includes_noraxon = TRUE;
                if (strcmp('MEGA/ME6000', $ch["Board"]) == 0) $includes_mega_me6000 = TRUE;
                if (strcmp('Delsys Trigno', $ch["Board"]) == 0) $includes_delsys_trigno = TRUE;
            }
            $measurement["Channels"]=$channels;
        }
    }
    $measurements[] = $measurement;
}

if(isset($template_file)){
	include($template_file);
}

?>