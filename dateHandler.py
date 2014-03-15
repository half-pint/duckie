def dateHandler(datearr):
    if len(datearr)==1:
        timestampFrom = str(int(datearr[0])-1) + "-12-31T00:00:00Z"
        timestampTo = str(int(datearr[0])+1) + "-01-01T24:00:00Z"
    if len(datearr)==2:
        if (int(datearr[1])-1==0):
            timestampFrom = str(int(datearr[0])-1)+"-12-31T00:00:00Z"
        elif (int(datearr[1])-1<10):
            timestampFrom = datearr[0]+"-"+"0"+str(int(datearr[1])-1) + "-31T00:00:00Z"
        else:
            timestampFrom =datearr[0]+"-"+str(int(datearr[1])-1) + "-31T00:00:00Z"

        if (int(datearr[1])+1==13):
           timestampTo = str(int(datearr[0])+1) + "-01-01T24:00:00Z"
        elif (int(datearr[1])+1<10):
            timestampTo = datearr[0] + "-" +"0"+str(int(datearr[1])+1) + "-01T24:00:00Z"
        else:
            timestampTo =datearr[0]+"-"+str(int(datearr[1])+1) + "-01T00:00:00Z"

    if len(datearr)==3:
        if (int(datearr[2])-1 == 0):
            if (int(datearr[1])==0):
                timestampFrom = str(int(datearr[0])-1) + "-12-31T00:00:00Z"
            elif (int(datearr[1])<10):
                timestampFrom = datearr[0] + "-" +"0"+ str(datearr[1]-1) + "-"+ "-31T00:00:00Z"
            else:
                timestampFrom = datearr[0]+"-"+str(int(datearr[1])-1) + "-31T00:00:00Z"
        else:
            timestampFrom = datearr[0] + "-" + datearr[1] + "-"+ str(int(datearr[2])-1) + "T00:00:00Z"


        if (int(datearr[2])+1==32):
            if (int(datearr[1])==12):
                timestampTo = str(int(datearr[0])+1) + "-01-01T24:00:00Z"
            elif (int(datearr[1]) < 10):
                timestampTo = datearr[0] + "-" +"0"+str(int(datearr[1])+1) + "-01T24:00:00Z"
            else:
                timestampTo = datearr[0] + "-" +str(int(datearr[1])+1) + "-01T24:00:00Z"
        else:
            timestampTo = datearr[0] + "-" + datearr[1] + "-"+ str(int(datearr[2])+1) + "T24:00:00Z"
    timestamps = [timestampFrom, timestampTo]
    return timestamps
