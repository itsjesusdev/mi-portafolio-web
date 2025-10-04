<?php
    // Recibir datos del formulario y limpiar caracteres especiales
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $nombre = htmlspecialchars($_POST['nombre']);
        $telefono = htmlspecialchars($_POST['telefono']);
        $email = htmlspecialchars($_POST['email']);
        $mensaje = htmlspecialchars($_POST['mensaje']); 

        // Destinatario
        $destinatario = "jmendozadev@gmail.com";

        // Asunto del correo
        $asunto = "Nuevo mensaje desde tu formulario web";

        // Cuerpo del mensaje
        $cuerpo = "Nombre: $nombre\n";
        $cuerpo .= "Teléfono: $telefono\n";
        $cuerpo .= "Email: $email\n";
        $cuerpo .= "Mensaje:\n$mensaje\n";

        // Encabezados del correo
        $cabeceras = "From: $email\r\n";
        $cabeceras .= "Reply-To: $email\r\n";

        // Enviar el correo
        if (mail($destinatario, $asunto, $cuerpo, $cabeceras)) {
            echo "<h2>Mensaje enviado correctamente. Gracias por ponerte en contacto $nombre.</h2>";
        } else {
            echo "<h2>Error al enviar el mensaje. Por favor, intenta nuevamente.</h2>";
        } 
    } else {
        echo "<h2>Acceso no permitido.</h2>";
    }
?>