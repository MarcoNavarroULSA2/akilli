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
    <?php
     $varnombre= htmlspecialchars($_GET["nombre"]);
     $varcorreo= htmlspecialchars($_REQUEST["c"]);
     $varpassword= htmlspecialchars($_REQUEST["p"]);
     $vartel= htmlspecialchars($_REQUEST["t"]);
     $varfecha= htmlspecialchars($_REQUEST["fecha"]);
    ?>

    <h1>Formulario2</h1>
    <div class="Registrarse">
        <?php
          echo " <input class='etiqueta' value=".$varnombre."> ";
        ?>

            <input  value="<?php  echo $varnombre; ?>" id="etiqueta2"/> 
            <input  value="<?php  echo $varcorreo; ?>"/>
            <input  value="<?php  echo $varpassword; ?>"/>
            <input  value="<?php  echo $vartel; ?>"/>
            <input  value="<?php  echo $varfehca; ?>"/>
            <button type="submit" class="btn btn-primary btn-block btn-large"> regresar al inicio</button>
     
    </div>
</body>
</html>