from flask import Flask
from flask import request
from flask import render_template
from SPARQLWrapper import SPARQLWrapper, JSON
from dateHandler import dateHandler
from summaryGenerator import generateSummaries


app = Flask(__name__)

@app.route('/')
def my_form():
	sparql = SPARQLWrapper("http://localhost:3030/hebridean/query")

	query = """

	PREFIX hebridean: <http://www.hebrideanconnections.com/hebridean.owl#>
	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
	SELECT DISTINCT ?name WHERE
	{
	?person rdf:type hebridean:Person .
	?person hebridean:livedAt ?addressL .
	?addressL hebridean:title ?address .
	?addressL hebridean:locatedAt ?location .
	?location hebridean:title ?name .
	} ORDER BY ?name
	"""

	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()
	locations =[]
	for result in results["results"]["bindings"]:
		locations.append({"name":result["name"]["value"] })

	return render_template('search.html', locations=locations)

@app.route('/', methods=['POST'])
def my_form_post():
	sparql = SPARQLWrapper("http://localhost:3030/hebridean/query")
	query = """
	PREFIX hebridean: <http://www.hebrideanconnections.com/hebridean.owl#>
	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
	SELECT DISTINCT ?id ?name ?diedFrom ?diedTo ?bornFrom ?bornTo ?address ?addressID ?livedAt ?bl ?sibling ?siblingID ?marriedID ?married ?child ?childID ?parent ?parentID ?occupation WHERE
	{
	?person rdf:type hebridean:Person .
	?person hebridean:title ?name .
	?person hebridean:subjectID ?id .
	?person hebridean:born ?born .
	?born hebridean:dateFrom ?bornFrom .
	?born hebridean:dateTo ?bornTo .
	?person hebridean:livedAt ?addressL .
	?addressL hebridean:title ?address .
	?addressL hebridean:subjectID ?addressID .
	?addressL hebridean:locatedAt ?location .
	?location hebridean:title ?livedAt .
	?person hebridean:sex ?bl .
	OPTIONAL { 	?person hebridean:dateOfDeath ?died .
				?died hebridean:dateFrom ?diedFrom .
				?died hebridean:dateTo ?diedTo .}
	OPTIONAL { ?person  hebridean:siblingOf  ?siblingL .
				?siblingL hebridean:title ?sibling .
				?siblingL hebridean:subjectID ?siblingID .}
	OPTIONAL { ?person  hebridean:married  ?marriedL .
				?marriedL hebridean:title ?married .
				?marriedL hebridean:subjectID ?marriedID . }
	OPTIONAL { ?person  hebridean:parentOf  ?childL .
				?childL hebridean:title ?child .
				?childL hebridean:subjectID ?childID  .}
	OPTIONAL { ?parentL  hebridean:parentOf  ?person .
				?parentL hebridean:title ?parent .
				?parentL hebridean:subjectID ?parentID  . }
	OPTIONAL { ?person  hebridean:occupation  ?occupation .}



	"""
	if request.form['name']:
	   query = query + " FILTER regex(lcase(str(?name)), '%s')" % request.form['name'].lower()
	if request.form['myradio']=='n':
		if request.form['date']:
			datearr= request.form['date'].split("/")	   
			timestamps = dateHandler(datearr)
			query = query + " FILTER ((xsd:dateTime(?bornFrom) > '%s'^^xsd:dateTime) && (xsd:dateTime(?bornTo)< '%s'^^xsd:dateTime)) " %(timestamps[0],timestamps[1])
	if request.form['myradio']=='y':
		if (request.form['dateFrom'] and request.form['dateTo']):
			datearrF= request.form['dateFrom'].split("/")	   
			timestampsF = dateHandler(datearrF)
			datearrT= request.form['dateTo'].split("/")	   
			timestampsT = dateHandler(datearrT)
			query = query + " FILTER ((xsd:dateTime(?bornFrom) > '%s'^^xsd:dateTime) && (xsd:dateTime(?bornTo)< '%s'^^xsd:dateTime)) " %(timestampsF[0],timestampsT[1])
	if request.form['radioDeath']=='n':
		if request.form['dateofdeath']:
			datearr= request.form['dateofdeath'].split("/")	   
			timestamps = dateHandler(datearr)
			query = query + " FILTER ((xsd:dateTime(?diedFrom) > '%s'^^xsd:dateTime) && (xsd:dateTime(?diedTo)< '%s'^^xsd:dateTime)) " %(timestamps[0],timestamps[1])
	if request.form['radioDeath']=='y':
		if (request.form['dodRangeFrom'] and request.form['dodRangeTo']):
			datearrF= request.form['dodRangeFrom'].split("/")	   
			timestampsF = dateHandler(datearrF)
			datearrT= request.form['dodRangeTo'].split("/")	   
			timestampsT = dateHandler(datearrT)
			query = query + " FILTER ((xsd:dateTime(?diedFrom) > '%s'^^xsd:dateTime) && (xsd:dateTime(?diedTo)< '%s'^^xsd:dateTime)) " %(timestampsF[0],timestampsT[1])
	if request.form['livedAt']!='':
		query = query + " FILTER regex(?livedAt, '%s')" % request.form['livedAt']

	query = query + "}"
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()

	entries =[]
	for result in results["results"]["bindings"]:
		if "sibling" in result:
			sibling = result["sibling"]["value"]
			siblingID = result["siblingID"]["value"]
		else:
			sibling = "N/a"
			siblingID = "N/a"

		if "married" in result:
			married = result["married"]["value"]
			marriedID = result["marriedID"]["value"]
		else:
			married = "N/a"
			marriedID = "N/a"

		if "child" in result:
			child = result["child"]["value"]
			childID = result["childID"]["value"]
		else:
			child = "N/a"
			childID = "N/a"

		if "parent" in result:
			parent = result["parent"]["value"]
			parentID = result["parentID"]["value"]
		else:
			parent = "N/a"
			parentID = "N/a"

		if "occupation" in result:
			occupation = result["occupation"]["value"]
		else:
			occupation = "N/a"

		if "diedFrom" in result:
			diedFrom = result["diedFrom"]["value"]
			diedTo = result["diedTo"]["value"]

		else:
			diedFrom = "N/a"
			diedTo = "N/a"

		entries.append({"id":result["id"]["value"], "name":result["name"]["value"], "bornFrom":result["bornFrom"]["value"], "bornTo":result["bornTo"]["value"], "diedFrom":diedFrom, "diedTo":diedTo, "livedAt":result["livedAt"]["value"], "sex":result["bl"]["value"], "address":result["address"]["value"], "addressID":result["addressID"]["value"], "siblingID": siblingID, "sibling":sibling, "marriedID":marriedID, "married":married, "child":child, "childID":childID, "parent":parent, "parentID":parentID, "occupation":occupation})

	summaries=generateSummaries(entries)
	return render_template('result.html', entries=entries, summaries=summaries)


if __name__ == '__main__':
	app.run(debug=True)
