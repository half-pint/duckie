function validateForm(){

    if (!validateDate()){
        document.getElementById("validate").value = "0";
        return false;
    }
    else {
        document.getElementById("validate").value = "1";
        return true;
    }

}

function validateDate(element, messageId) {

    var date = element.value;
    if (date.length == 0){
        document.getElementById(messageId).innerHTML = "Right";
        return true;}
    else if (!date.match(/(^....\/..\/..$)|(^....\/..$)|(^....$)/)){
        document.getElementById(messageId).innerHTML = "Wrong";
        return false;
    }
    else {
    var dateSplit = date.split("/")
    var currentTime = new Date()
	    if (dateSplit[0]>1000 & dateSplit[0]<=currentTime.getFullYear() & !dateSplit[1]){
            document.getElementById(messageId).innerHTML = "Right";
            return true;
        }
        else if (dateSplit[0]>1000 & dateSplit[0]<=currentTime.getFullYear() & dateSplit[1]>=1 & dateSplit[1]<=12 & !dateSplit[2]){
            document.getElementById(messageId).innerHTML = "Right";
            return true;
        }

        else if (dateSplit[0]>1000 & dateSplit[0]<=currentTime.getFullYear() & dateSplit[1]>=1 & dateSplit[1]<=12 &  dateSplit[2]>=1 & dateSplit[2]<=31){
            document.getElementById(messageId).innerHTML = "Right";
            return true;
        }
        else{
        document.getElementById(messageId).innerHTML = "Wrong";
        return false;
        }
   
    }


}

function validateDateRange(idF,idT,idMessage){
if (document.getElementById(idF).value.length==0 & document.getElementById(idF).value.length==0)
{document.getElementById(idMessage).innerHTML = "Yaaay";
return true;}
else if (!isItAYear(idF) | !isItAYear(idT)){
document.getElementById(idMessage).innerHTML = "Please enter years in the format yyyy";
return false;
}
else if (document.getElementById(idF).value > document.getElementById(idT).value)
{document.getElementById(idMessage).innerHTML = "The year 'from' should be before the year 'to' ";
return false;
}
else {document.getElementById(idMessage).innerHTML = "Yaaay";
return true;

}
}


function isItAYear(id){
var year = document.getElementById(id).value;
var currentTime = new Date()
    if (!year.match(/^[0-9][0-9][0-9][0-9]$/)){
        return false;}
    else if (year>currentTime.getFullYear())
		{return false;}
    else {return true;}
}

function tgl(element){
if (element.value == 'y'){
document.getElementById("dateofbirth").disabled = true;
document.getElementById("dobRangeFrom").disabled = false;
document.getElementById("dobRangeTo").disabled = false;
}
else{
document.getElementById("dateofbirth").disabled = false;
document.getElementById("dobRangeFrom").disabled = true;
document.getElementById("dobRangeTo").disabled = true;
}
}

function tglD(element){
if (element.value == 'y'){
document.getElementById("dateofdeath").disabled = true;
document.getElementById("dodRangeFrom").disabled = false;
document.getElementById("dodRangeTo").disabled = false;
}
else{
document.getElementById("dateofdeath").disabled = false;
document.getElementById("dodRangeFrom").disabled = true;
document.getElementById("dodRangeTo").disabled = true;
}
}

function messagePrompt(id,text){
document.getElementById(id).innerHTML = text;
}
