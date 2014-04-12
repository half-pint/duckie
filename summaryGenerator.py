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
	addr = []
	for entry in entries:
		if ID == entry["id"]:
			locations.append({'city':entry["livedAt"], 'address':entry["address"]})
	return locations

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
			dot = len(locations)
			control = 1 
			for location in locations:
				summary+=  location['address']+" (located at " + location["city"]+") "
				if control == dot:
					summary += ". "
				else: 
					summary += ", "
				control+=1
			if entry["sex"] == "Female":
				summary = summary + " Female"
			elif entry["sex"] == "Male":
				summary += "male"
			else: 
				summary += "n/a"
			ID = entry["id"]
			summaries.append(summary)

	return summaries
    
