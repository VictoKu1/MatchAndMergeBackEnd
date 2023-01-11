from flask import Flask, request, jsonify, render_template
import social_aware_assignment_of_passengers_in_ridesharing as saapir
import networkx as nx

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/match_and_merge', methods=['POST'])
def match_and_merge_route():
    # Get the form data
    graph = request.json.get('graph')
    number = request.json.get('number')

    edges = [tuple(map(int, edge.split(','))) for edge in graph.strip('[]').split('), (')]
    print(edges)
    G=nx.Graph()
    G.add_edges_from(edges)
    k = int(number)
    # Call match_and_merge function
    result = saapir.match_and_merge(G, k)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

