from flask import Flask, request, jsonify, render_template
import networkx as nx
import social_aware_assignment_of_passengers_in_ridesharing as saapir

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/match_and_merge", methods=["POST"])
def match_and_merge():
    # Get the graph and number from the request body
    data = request.json
    graph = data['graph']
    number = data['number']
    # Convert the graph from json format to networkx format
    G = nx.Graph(graph)
    # Call the match_and_merge function
    partition = saapir.match_and_merge(G, number)
    # Return the partition as a JSON response
    return jsonify(partition)

if __name__ == "__main__":
    app.run()