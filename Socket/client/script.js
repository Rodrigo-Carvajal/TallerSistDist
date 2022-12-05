//This is jquery syantax to autoexecute function once
let socket, sendMessageBoard;
$(() => {
  socket = io.connect("192.168.1.93:8000");
  sendMessageBoard = new DrawingBoard.Board("sendMessageBoard");
  $("#sendDWGbtn").click(() => {
    // Enviar imágen al hacer click en el boton enviar dibujo
    //console.log("SEND DRAWINGG");
    socket.emit("drawing", sendMessageBoard.getImg());
    //Despues de enviar el dibujo, reiniciar el lienzo
    sendMessageBoard.resetBackground();
    return false;
  });
  socket.on("drawing", function (msg) {
    $("#messageContainer").append(
      $("<li class='w-100 d-flex align-center justify-content-center'>").html(
        `<img src="${msg}" class="w-75 m-auto img-msg"/>`
      )
    );
    window.scrollTo(0, document.body.scrollHeight);
  });
});
