<?php
$xml = simplexml_load_file($xml_file);

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
?>