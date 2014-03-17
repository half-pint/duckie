from flask import Flask
from flask import request
from flask import render_template
from SPARQLWrapper import SPARQLWrapper, JSON
from dateHandler import dateHandler

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("search.html")

@app.route('/', methods=['POST'])
def my_form_post():
    sparql = SPARQLWrapper("http://localhost:3030/books/query")
    query = """
    PREFIX hebridean: <http://www.hebrideanconnections.com/hebridean.owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    SELECT ?name ?bornFrom ?bornTo WHERE
    {
    ?person rdf:type hebridean:Person .
    ?person hebridean:title ?name .
    ?person hebridean:born ?born .
    ?born hebridean:dateFrom ?bornFrom .
    ?born hebridean:dateTo ?bornTo .
    """
    if request.form['name']:
       query = query + " FILTER regex(?name, '%s')" % request.form['name']
    if request.form['date']:
        datearr= request.form['date'].split("/")       
        timestamps = dateHandler(datearr)
        query = query + " FILTER ((xsd:dateTime(?bornFrom) > '%s'^^xsd:dateTime) && (xsd:dateTime(?bornTo)< '%s'^^xsd:dateTime)) " %(timestamps[0],timestamps[1])
        
    query = query + "}"
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    entries =[]
    bornFrom=[]
    bornTo=[]
    for result in results["results"]["bindings"]:
        entries.append({"name":result["name"]["value"], "bornFrom":result["bornFrom"]["value"], "bornTo":result["bornTo"]["value"]})


    return render_template('result.html', entries=entries)


if __name__ == '__main__':
    app.run(debug=True)
