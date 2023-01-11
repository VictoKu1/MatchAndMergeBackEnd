document.getElementById("form").addEventListener("submit", function(event) {
    event.preventDefault();
    var graph = document.getElementById("graph").value;
    var number = document.getElementById("number").value;
    //* Print the values to the console
    console.log(graph);
    console.log(number);
    var data = { graph: graph, number: number };
    fetch("/run_algorithm", {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(res => res.json())
        .then(data => {
            document.getElementById("output").innerHTML = JSON.stringify(data);
        });
});