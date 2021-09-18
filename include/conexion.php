<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors',1);
error_reporting(E_ALL);
$varservername= "ftp.nemonico.com.mx";
$varusername= "sepherot_dianac";
$varpassword= "SIJ2e04sKLGh";
$vardbname= "sepherot_dianacBD";
//crear conexion
$varconexion = mysqli_connect($varservername, $varusername,$varpassword,$vardbname);

//revisar la conexion
if(!$varconexion) {
    die("fallo la conexion: ");
}

//devolver conexion
else{
    //echo "conexion exitosa";
    return $varconexion;
}

?>

