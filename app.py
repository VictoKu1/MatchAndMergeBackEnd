from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import social_aware_assignment_of_passengers_in_ridesharing as saapir
import networkx as nx

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def match_and_merge_route():
    # Get the form data
    if request.method == 'POST':
        graph = request.form['graph']
        number = request.form['number']
        edges = eval(graph)
        G = nx.Graph()
        G.add_edges_from(edges)
        k = int(number)
        # Call match_and_merge function
        result = saapir.match_and_merge(G, k)
        return render_template('result.html', result=result)
    else:
        return render_template('result.html')

if __name__ == '__main__':
    # Run the app
    app.run(host="0.0.0.0", port=5001)





