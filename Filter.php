<?php

# // Created By @R3ppy

$Domain = $_GET['domain'];

function FilterDomain($Domain) {
    # Checking If It's Durpal
    $ch = curl_init($Domain."/user/login");
    curl_setopt($ch, CURLOPT_TIMEOUT, 10);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    $result = curl_exec($ch);
    curl_close($ch);
    if (strpos($result, "<html>") !== false) {
        echo $Domain." : Durpal!\n";
    }
    
    # Checking If It's Joomla
    $ch = curl_init($Domain."/administrator/index.php");
    curl_setopt($ch, CURLOPT_TIMEOUT, 10);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    $result = curl_exec($ch);
    curl_close($ch);
    if (strpos($result, "<html>") !== false) {
        echo $Domain." : Joomla!\n";
    }
    
    # Checking If It's WordPress
    $ch = curl_init($Domain."/wp-login.php");
    curl_setopt($ch, CURLOPT_TIMEOUT, 10);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    $result = curl_exec($ch);
    curl_close($ch);
    if (strpos($result, "Powered by WordPress") !== false) {
        echo $Domain." : WordPress!\n";
    }
}

FilterDomain($Domain);

?>

<html>
    <head>
        <title>R3ppy @#~</title>
    </head>
    <body>
        <?php ?>
    </body>
</html>