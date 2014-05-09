

from SPARQLWrapper import SPARQLWrapper, JSON


def updateLocationMenu():
	sparql = SPARQLWrapper("http://localhost:3030/hebridean/query")
	query = """
	PREFIX hebridean: <http://www.hebrideanconnections.com/hebridean.owl#>
	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
	SELECT ?name WHERE
	{
	?location rdf:type hebridean:Location .
	?location hebridean:title ?name .

	
	} ORDER BY ?name

	"""
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()

	locations =[]
	for result in results["results"]["bindings"]:
		locations.append({"name":result["name"]["value"] })
	with open('templates/locations.html', 'w') as file:
		for location in locations:
			file.write("<option>"+location["name"]+"</option>\n")


if __name__=="__main__":
	updateLocationMenu()
	
