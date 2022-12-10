let socket, sendMessageBoard;
$(() => {
  socket = io.connect("192.168.100.133:8000");
  sendMessageBoard = new DrawingBoard.Board("sendMessageBoard");
  $("#sendDWGbtn").click(() => {
    // Enviar imágen al hacer click en el boton enviar dibujo
    var resultado = window.confirm('¿Deseas enviar este dibujo?');
    if (resultado === true) {//Una vez confirmado, se envie el dibujo y se reinicia el lienzo.
      socket.emit("drawing", sendMessageBoard.getImg());  
      sendMessageBoard.resetBackground();
    }
    else {
      borrar = window.confirm('¿Desea descartar el dibujo realizado?');
        if(borrar === true){
          sendMessageBoard.resetBackground();
        }
        else{
          
        }
    }
    return false;
  });
  socket.on("drawing", function (msg) {
    $("#messageContainer").append(
      $("<li class='w-100 d-flex align-center justify-content-center'>").html(
        `<img src="${msg}" class="w-75 m-auto img-msg"/>`
      )
    );
    window.scroll(0, document.body.scrollHeight);
  });
});
