from flask import Flask, request, jsonify, render_template, redirect, url_for, session
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
    edges = eval(graph)
    G = nx.Graph()
    G.add_edges_from(edges)
    k = int(number)
    # Call match_and_merge function
    result = saapir.match_and_merge(G, k)
    session['result'] = result
    return redirect(url_for('result'))

@app.route('/result', methods=['GET'])
def result():
    # Get the result from the session
    result = session.get('result')

    # Render the result page
    return render_template('result.html', result=result)

if __name__ == '__main__':
    # Run the app
    app.run(host="0.0.0.0", port=5001)

