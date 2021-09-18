<?php
    
    //Revisar si existe la variable varcorreo
    if(!isset($varcorreo)){
        $varcorreo = "";
    }

    //Revisar si existe la variable varpassword
    if(!isset($varpassword)){
        $varpassword = "";
    }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <link href="css/login.css" rel="stylesheet" type="text/css">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SMARTER ASSISTANTS</title>
</head>
<body>
    <h1>login</h1>
    <div class="forma">
        <form action="getLogin.php" method="POST">
          
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
           
            <button type="submit" class="btn btn-primary btn-block btn-large"> aceptar</button>
        </form>
        
    </div>
</body>
</html>