$(document).ready(function(){
    /* Se crea un objeto socket y se conecta al servidor y se le pasa la URL del servidor */
    const socket = io();

    /* socket.on('connect', function(){
        socket.send('Nuevo usuario conectado');
    }); */
    
    socket.on('message', function(msg){
        $("#messages").append('<li> Mari: '+msg+'</li>');
        console.log('Mensaje recibido desde servidor: ' + msg);
    });

    $('#sendButton').on('click', function(){
        socket.send($('#myMessage').val());
        $("#messages").append('<li> Paciente: '+ $('#myMessage').val() +'</li>');
        $('#myMessage').val('');                
    });
});