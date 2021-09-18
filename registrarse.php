<?php
    //Revisar si existe la variable varnombre
    if(!isset($varnombrecompleto)){
        $varnombrecompleto = "";
    }

    //Revisar si existe la variable varcorreo
    if(!isset($varcorreo)){
        $varcorreo = "";
    }

    //Revisar si existe la variable varpassword
    if(!isset($varpassword)){
        $varpassword = "";
    }

    //Revisar si existe la variable vartelefono
    if(!isset($vartel)){
        $vartel = "";
    }

    //Revisar si existe la variable varpuesto
    if(!isset($varpuesto)){
        $varpuesto = "";
    }
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <link href="css/registrarse.css" rel="stylesheet" type="text/css">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Formulario de Registro</h1>
    <div class="forma">
        <form name="myForm" action="getRegistrarse.php" method="POST">
            <!-- CAMPO NOMBRE -->
            <input type="text" name="nombrecompleto" placeholder="Escribe tu nombre completo" value="<?php echo htmlspecialchars($varnombrecompleto) ?>"/> 
            <?php if(isset($namecompleto_error)) {?>
                <p> <?php echo $namecompleto_error ?> </p>
            <?php } ?>

            <!-- CAMPO EMAIL -->
            <input type="email" name="email" placeholder="Escribe tu correo" value="<?php echo htmlspecialchars($varcorreo) ?>"/> 
            <?php if(isset($correo_error)) {?>
                <p> <?php echo $correo_error ?> </p>
            <?php } ?>

            <!-- CAMPO PASSWORD -->
            <input type="password" name="password" placeholder="Escribe tu password" value="<?php echo htmlspecialchars($varpassword) ?>"/> 
            <?php if(isset($password_error)) {?>
                <p> <?php echo $password_error ?> </p>
            <?php } ?>

            <!-- CAMPO Telefono -->
            <input type="tel" name="tel" placeholder="Escribe tu telefono" value="<?php echo htmlspecialchars($vartel) ?>"/> 
            <?php if(isset($tel_error)) {?>
                <p> <?php echo $tel_error ?> </p>
            <?php } ?>

             <!-- CAMPO Puesto -->    
             <input type="text" name="puesto" placeholder="Escribe tu puesto"value="<?php echo htmlspecialchars($varpuesto) ?>"/> 
            <?php if(isset($puesto_error)) {?>
                <p> <?php echo $puesto_error ?> </p>
            <?php } ?>
        

            <button type="submit" class="btn btn-primary btn-block btn-large">Aceptar</button>
        </form>
        
    </div>

   <!-- https://www.youtube.com/watch?v=MMHUxT1pSMg-->
</body>
</html>