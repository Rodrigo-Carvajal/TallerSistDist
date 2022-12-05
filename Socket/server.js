const express = require("express");
var app = express();
var http = require("http").createServer(app);
var io = require("socket.io")(http);
var PORT = process.env.PORT || 8000;

app.use(express.static(`${__dirname}/client`));
let dibujos = [];

//Envío en tiempo real a través del socket
io.on("connection", function (socket) {
  //Cuando el socket consigue un dibujo, se lo envía al resto de clientes
  socket.on("drawing", function (dibujo) {
    dibujos.push(dibujo);
    io.emit("drawing", dibujo);
  });
});

http.listen(PORT, function () {
  console.log(`El servidor está siendo oído en el puerto: ${PORT}`);
});
