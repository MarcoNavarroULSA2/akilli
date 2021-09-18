<?php
include"conexion.php";
$conn=$varconexion;

if($conn->connect_error){
    die("Fallo la conexion: ". $conn->connect_error);
}

$sql= "

CREATE TABLE `Empleado` (
    `ID_Empleado` int(11) NOT NULL,  
    `NombreCompleto` varchar(100) COLLATE utf8_spanish_ci NOT NULL, 
    `Correo` varchar(250) COLLATE utf8_spanish_ci NOT NULL, 
    `Password` varchar(250) COLLATE utf8_spanish_ci NOT NULL, 
    `Telefono` int(11) NOT NULL DEFAULT 1, 
    `Puesto` varchar(100) COLLATE utf8_spanish_ci NOT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;
  
  




";

//TRUNCATE TABLE Login_Empleado
//INSERT INTO Login_Empleado (Correo, Password) VALUES ('cristian@hotmail.com', 'password');


//TRUNCATE TABLE Empleado
//INSERT INTO Empleado (Nombre, Telefono, Puesto, ID_LoginEmpleado) VALUES ('Cristian Alan', '5555547', 'Ing', 1);
?>

