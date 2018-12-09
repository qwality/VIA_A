<?php
echo $_GET["json"];
$fp = fopen('data.json', 'w');
fwrite($fp, $_GET["json"]);
fclose($fp);
?>
