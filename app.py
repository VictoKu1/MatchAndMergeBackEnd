from flask import Flask, request, jsonify, render_template
import social_aware_assignment_of_passengers_in_ridesharing as saapir
import networkx as nx
import socket
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/match_and_merge', methods=['POST'])
def match_and_merge_route():
    # Get the form data
    graph = request.json.get('graph')
    number = request.json.get('number')
    edges = eval(graph)
    G=nx.Graph()
    G.add_edges_from(edges)
    k = int(number)
    # Call match_and_merge function
    result = saapir.match_and_merge(G, k)
    return jsonify({'result': result})

if __name__ == '__main__':
    # Find a free port to run the app and print it
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    p = s.getsockname()[1]
    s.close()
    print("Port: "+p)
    # Run the app
    app.run(host="0.0.0.0", port=8080)


