from SPARQLWrapper import SPARQLWrapper, JSON

def month(number):
	if number <=12:
		if number == 1:
			month = 'January'
		if number == 2:
			month = 'February'
		if number == 3:
			month = 'March'
		if number == 4:
			month = 'April'
		if number == 5:
			month = 'May'
		if number == 6:
			month = 'June'
		if number == 7:
			month = 'July'
		if number == 8:
			month = 'August'
		if number == 9:
			month = 'September'
		if number == 10:
			month = 'October'
		if number == 11:
			month = 'November'
		if number == 12:
			month = 'December'
	return month

def lived(ID, entries):
	locations = []
	used = []
	for entry in entries:
		if ID == entry["id"]:
			if entry["addressID"] not in used:
				locations.append(entry["address"])
				used.append(entry["addressID"])
	return locations

def siblings(ID, entries):
	siblings = []
	used = []
	for entry in entries:
		if ID == entry["id"]:
			if entry["siblingID"] not in used:
				siblings.append(entry["sibling"])
				used.append(entry["siblingID"])
	return siblings

def married(ID, entries):
	married = []
	used = []
	for entry in entries:
		if ID == entry["id"]:
			if entry["marriedID"] not in used:
				married.append(entry["married"])
				used.append(entry["marriedID"])
	return married

def children(ID, entries):
	children = []
	used = []
	for entry in entries:
		if ID == entry["id"]:
			if entry["childID"] not in used:
				children.append(entry["child"])
				used.append(entry["childID"])
	return children

def parents(ID, entries):
	parents = []
	used = []
	for entry in entries:
		if ID == entry["id"]:
			if entry["parentID"] not in used:
				parents.append(entry["parent"])
				used.append(entry["parentID"])
	return parents

def occupation(ID, entries):
	occupations = []
	for entry in entries:
		if ID == entry["id"]:
			if entry["occupation"] not in occupations:
				occupations.append(entry["occupation"])
	return occupations

def generateSummaries(entries):
	summaries =[]
	ID = 0
	for entry in entries:
		if ID != entry["id"]:
			summary=" "
			summary += entry["name"]
			dateF = entry["bornFrom"].split('T')
			dateT = entry["bornTo"].split('T')
			dateSplitF = dateF[0].split('-')
			dateSplitT = dateT[0].split('-')
			if dateF[0] == dateT[0]:
				summary = summary +" was born on " + dateSplitF[2] +" "+ month(int(dateSplitF[1])) +" " +dateSplitF[0]
			elif dateSplitF[0] == dateSplitT[0]:
				if dateSplitF[1] == dateSplitT[1]:
					summary = summary +" was born in " + month(int(dateSplitF[1])) +" " +dateSplitF[0]
				else:
					summary = summary +" was born in " +dateSplitF[0]
			else:
				summary = summary +" was born between "+dateF[0]+" and "+dateT[0]
			summary = summary + " and lived at "
			locations = lived(entry["id"], entries)

			#Check if the last location in the list in order decide between ',' or '.'			
			dot = len(locations)
			control = 1
			for location in locations:
				summary+=  location
				if control == dot:
					summary += ". "
				elif control+1 == dot:
					summary += " and "
				else:
					summary += ", "
				control+=1


			#Check the sex of the person in order to use the proper pronoun 
			if entry["sex"] == "Female":
				personalPronoun = "She"
				possessivePronoun = "Her"
			elif entry["sex"] == "Male":
				personalPronoun = "He"
				possessivePronoun = "His"
			else:
				personalPronoun = "They"
				possessivePronoun = "Their"
			ID = entry["id"]

			#Died
			if  entry["diedFrom"] == "N/a":
				summary += "There is no information in the database about "+possessivePronoun.lower()+" date of death. "
			else:
				summary += personalPronoun + " died "
				parentsList = parents(ID, entries)
				dateF = entry["diedFrom"].split('T')
				dateT = entry["diedTo"].split('T')
				dateSplitF = dateF[0].split('-')
				dateSplitT = dateT[0].split('-')
				if dateF[0] == dateT[0]:
					summary = summary + "on "+ dateSplitF[2] +" "+ month(int(dateSplitF[1])) +" " +dateSplitF[0]+". "
				elif dateSplitF[0] == dateSplitT[0]:
					if dateSplitF[1] == dateSplitT[1]:
						summary = summary +"in " + month(int(dateSplitF[1])) +" " +dateSplitF[0]+". "
					else:
						summary = summary +"in " +dateSplitF[0]+". "
				else:
					summary = summary +" between "+dateF[0]+" and "+dateT[0] +". "
			#Mention siblings and other relatives
			#Siblings
			if  entry["sibling"] == "N/a":
				summary += "There is no information about siblings. "
			else:
				summary += personalPronoun + " was a sibling of "
				siblingsList = siblings(ID, entries)
				dot = len(siblingsList)
				control = 1
				for sibling in siblingsList:
					summary+=  sibling
					if control == dot:
						summary += ". "
					elif control+1 == dot:
						summary += " and "
					else:
						summary += ", "
					control+=1
			#Married
			if  entry["married"] == "N/a":
				summary += "There is no information in the database if "+personalPronoun.lower()+" was married. "
			else:
				summary += personalPronoun + " was married to "
				marriedList = married(ID, entries)
				dot = len(marriedList)
				control = 1
				for spouse in marriedList:
					summary+=  spouse
					if control == dot:
						summary += ". "
					elif control+1 == dot:
						summary += " and "
					else:
						summary += ", "
					control+=1
			#Children
			if  entry["child"] == "N/a":
				summary += "There is no information in the database if "+personalPronoun.lower()+" had any children. "
			else:
				summary += personalPronoun + " was a parent of "
				childrenList = children(ID, entries)
				dot = len(childrenList)
				control = 1
				for child in childrenList:
					summary+=  child
					if control == dot:
						summary += ". "
					elif control+1 == dot:
						summary += " and "
					else:
						summary += ", "
					control+=1
			#Parents
			if  entry["parent"] == "N/a":
				summary += "There is no information in the database about "+possessivePronoun.lower()+" parents. "
			else:
				summary += personalPronoun + " was a child of "
				parentsList = parents(ID, entries)
				dot = len(parentsList)
				control = 1
				for parent in parentsList:
					summary+=  parent
					if control == dot:
						summary += ". "
					elif control+1 == dot:
						summary += " and "
					else:
						summary += ", "
					control+=1
			#Occupation
			if  entry["occupation"] == "N/a":
				summary += "There is no information in the database about "+possessivePronoun.lower()+" occupation. "
			else:
				summary += personalPronoun + " worked as a "
				occupationList = occupation(ID, entries)
				dot = len(occupationList)
				control = 1
				for job in occupationList:
					summary+=  job
					if control == dot:
						summary += ". "
					elif control+1 == dot:
						summary += " and "
					else:
						summary += ", "
					control+=1

				 
			summaries.append({"summary":summary, "name":entry["name"]})
				

	return summaries
    
