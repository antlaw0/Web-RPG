console.log("clientgame hello")

var input = document.getElementById("command")
var messages = document.getElementById("messages");


input.addEventListener("keyup", function(event){

  if (event.keyCode != 13) { return; }

  var command = input.value;

  $.ajax( {
    url: "/executeCommand",
    method: "POST",
    data: { command : command }
  }).done(function(data){
    // data returned here
    console.log(data);
    showMessages(data);

  }).fail(function(err){
    // deal with errors here
  })

});



function showMessages(msgs) {

  for (var x = 0 ; x < msgs.length ; x++) {
    var p = document.createElement("p");
    p.innerHTML = msgs[x]
    messages.appendChild(p);
  }

}
