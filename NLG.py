from SPARQLWrapper import SPARQLWrapper, JSON

def sentence(subjectID, prop):
	sparql = SPARQLWrapper("http://localhost:3030/hebridean/query")

	query = """
	PREFIX hebridean: <http://www.hebrideanconnections.com/hebridean.owl#>
	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX nlg: <http://www.shiftout.com/~ellie/nlg.owl> 
	SELECT DISTINCT ?template ?object ?subject WHERE {
    %s nlg:template ?template .
	%s nlg:subject ?subject .
	%s nlg:object ?object .
 	}
    """ %(prop,prop,prop)
	
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	templatesResults = sparql.query().convert()
	templates = []
	for result in templatesResults["results"]["bindings"]:
		templates.append({"template":result["template"]["value"], "subject":result["subject"]["value"], "object":result["object"]["value"]})
		

	query = """
	PREFIX hebridean: <http://www.hebrideanconnections.com/hebridean.owl#>
	PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
	PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX nlg: <http://www.shiftout.com/~ellie/nlg.owl> 
	SELECT DISTINCT ?object ?subject WHERE {
	?subjectL rdf:type <%s> .
	?subjectL hebridean:title ?subject .
	?subjectL hebridean:subjectID ?id .
	?subjectL %s ?objectL .
	?objectL hebridean:title ?object .
 FILTER (?id = %s) }
    """ %(templates[0]["subject"], prop, subjectID)
	
	sparql.setQuery(query)
	sparql.setReturnFormat(JSON)
	results = sparql.query().convert()

	control = 1
	objects = []
	for result in results["results"]["bindings"]:
		objects.append(result["object"]["value"])
		subject = result["subject"]["value"]
	
#	for obj in objects:
#		print(obj)

#	print("------------")

	sentence = subject +" "+ templates[0]["template"] + " "
	for obj in objects:
		sentence += obj
		if control == len(objects):
			sentence += ". "
		elif control == len(objects)-1:
			sentence += " and "
		else:
			sentence += ", "
		print(sentence)
		control+=1

	return sentence
