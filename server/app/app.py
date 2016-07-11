from flask import Flask
from flask import request
from resources.analyzer import Analyzer

app = Flask(__name__)


@app.route('/get_test_diagram')
def getTestDiagram():
    analyzer = Analyzer()
    return analyzer.getTestData()
