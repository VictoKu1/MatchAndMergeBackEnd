// Get the form
const form = document.getElementById("form");

// Handle the form submit event
form.addEventListener("submit", function(event) {
    event.preventDefault();
    submitForm();
});

// Send a POST request to the server
function submitForm() {
    // Get the form data
    var graph = document.getElementById("graph").value;
    var number = document.getElementById("number").value;

    // Send a POST request to the server
    fetch("/match_and_merge", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ graph: graph, number: number })
        })
        .then(response => {
            if (response.redirected) {
                window.location.href = response.url;
            }
        })
        .catch(error => {
            console.log(error);
        });
}