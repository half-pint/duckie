from flask import Flask
from flask import request
from flask import render_template
from SPARQLWrapper import SPARQLWrapper, JSON

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("search.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    sparql = SPARQLWrapper("http://localhost:3030/books/query")
    query = """
    PREFIX hebridean: <http://www.hebrideanconnections.com/hebridean.owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT ?name WHERE
    {
    ?person rdf:type hebridean:Person .
    ?person hebridean:title ?name
    """
    if request.form['text']:
        query = query + " FILTER regex(?name, '%s')" % text
    query = query + "}"
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    entries =[]
    for result in results["results"]["bindings"]:
        entries.append(result["name"]["value"])
   
    return render_template('result.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)


