<?php    
  $error_form = false;
    //Validacion correo
    $varcorreo= htmlspecialchars($_REQUEST["email"]);

    if(empty($varcorreo)){
        $correo_error = "Por favor ingresa tu correo";
        $error_form = true;
    }

    //Validacion password
    $varpassword= htmlspecialchars($_REQUEST["password"]);

    if(empty($varpassword)){
        $password_error = "Por favor ingresa una contraseña";
        $error_form = true;
    }

    

    if(!$error_form){
        $usuariosEncontrados = selectLoginEmpleado($varcorreo, $varpassword);
    
        if($usuariosEncontrados == 1){
            header("Location: /dianac/menu.html");
            exit();
        }
        else{
            $password_error = "Usuario o contraseña incorrecto";
        }
    }
    
    include('login.php');

    function selectLoginEmpleado($correo, $password){
    
        include "include/conexion.php";

        //echo $password;

        $sql_SelectLoginEmpleado = "SELECT password FROM Login_Empleado WHERE Correo = '$correo';";

        //echo $sql_SelectLoginEmpleado;
        $result = mysqli_query($varconexion, $sql_SelectLoginEmpleado);

        $usuariosEncontrados = $result->num_rows;

        if ($usuariosEncontrados > 0){
            $usuario = $result -> fetch_object();
            if (password_verify($password, $usuario -> password)){
                $usuariosEncontrados = 1;
            }
        }

        mysqli_close($varconexion);

        return $usuariosEncontrados;
    }
?>

