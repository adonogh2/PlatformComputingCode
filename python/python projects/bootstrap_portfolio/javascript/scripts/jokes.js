function getJoke(){
    var request = new XMLHttpRequest();
    request.open("GET", "https://official-joke-api.appspot.com/random_joke");
    request.send();

    request.onload = function(){
        var data = JSON.parse(this.response);
        var setup = data.setup;
        var punchline = data.punchline;
        console.log(punchline);
        console.log(setup);
        document.getElementById("setup").textContent = setup;
        document.getElementById("punchline").textContent = punchline;
    }
}