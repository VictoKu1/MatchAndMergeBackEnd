import networkx as nx
from flask import Flask, render_template, request

from coalition_formation import match_and_merge

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def match_and_merge_route():
    # Get the form data
    graph = request.form["graph"]
    number = request.form["number"]
    edges = eval(graph)
    G = nx.Graph()
    G.add_edges_from(edges)
    k = int(number)
    # Call match_and_merge function
    result = match_and_merge(G, k)
    log = ""
    # Use the log file if exists
    with open("coalition_formation.log", "r") as f:
        log = f.read()
    return render_template(
        "result.html", result=result, graph=graph, number=number, log=log
    )

if __name__ == "__main__":
    # Run the app
    app.run(host="0.0.0.0", port=5001)

