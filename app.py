from flask import Flask, request, render_template
from coalition_formation import match_and_merge
import networkx as nx
import logging
import datetime

app = Flask(__name__)

# Set the logger
LOG_FORMAT = "%(levelname)s, time: %(asctime)s ,line: %(lineno)d, %(message)s"
# Date and time (including milliseconds) for log file name
date_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
logging.basicConfig(
    filename="coalition_formation_start_"+date_time+".log",
    level=logging.DEBUG,
    format=LOG_FORMAT,
)
logger = logging.getLogger()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def match_and_merge_route():
    # Get the form data
    graph = request.form['graph']
    number = request.form['number']
    edges = eval(graph)
    G = nx.Graph()
    G.add_edges_from(edges)
    k = int(number)
    # Call match_and_merge function
    result = match_and_merge(G, k)
    return render_template('result.html', result=result, graph=graph, number=number)

if __name__ == '__main__':
    # Run the app
    app.run(host="0.0.0.0", port=5001)





























