function send()
{
    var message = document.getElementById("text").value;

    if (message == "")
    {
        alert("Please fill in all fields.");
    }
    else
    {
        var request = new XMLHttpRequest();
        request.open("POST", "/classify", true);
        request.setRequestHeader("Content-Type", "application/json");
        request.send(JSON.stringify({text: message}));
        request.onload = function()
        {
            var response = JSON.parse(request.responseText);
            if (response.status == "success")
            {
                alert("Message Uploaded!");
                document.getElementById("result").innerHTML = response.message;
            }
            else
            {
                alert("Message failed to send.");
            }
        }
    }
}