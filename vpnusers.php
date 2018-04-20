<?php

//$command = escapeshellcmd('/var/www/html/fortiVPNSSL.py');
//$output = shell_exec($command);
//echo $output;

$output=shell_exec('/var/www/html/fortiosapi/fortiVPNSSL.py');
echo "<pre>";
print_r($output);
echo "</pre>";

?>
