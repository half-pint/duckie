function validateForm(){
    if (!validateDate()){
        return false;
    }
    else {
        return true;
    }

}
function validateDateRange(){
var from = document.getElementById("dateofbirthRangeFrom").value;
var to = document.getElementById("dateofbirthRangeTo").value;
if (!isItAYear("dateofbirthRangeFrom") & !isItAYear("dateofbirthRangeTo")){
document.getElementById("dateofbirthMessageRange").innerHTML = "Please enter years in the format yyyy";
return false;
}
else if (true)
{document.getElementById("dateofbirthMessageRange").innerHTML = "The year 'from' should be before the year 'to' ";
return false;
}
else {document.getElementById("dateofbirthMessageRange").innerHTML = "Yaaay";
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



function validateDate() {

    var date = document.getElementById("dateofbirth").value;
    if (!date.match(/(^....\/..\/..$)|(^....\/..$)|(^....$)/)){
        document.getElementById("dateofbirthMessage").innerHTML = "Wrong";
        return false;
    }
    else {
    var dateSplit = date.split("/")
    var currentTime = new Date()
	    if (dateSplit[0]>1000 & dateSplit[0]<=currentTime.getFullYear() & !dateSplit[1]){
            document.getElementById("dateofbirthMessage").innerHTML = "Right";
            return true;
        }
        else if (dateSplit[0]>1000 & dateSplit[0]<=currentTime.getFullYear() & dateSplit[1]>=1 & dateSplit[1]<=12 & !dateSplit[2]){
            document.getElementById("dateofbirthMessage").innerHTML = "Right";
            return true;
        }

        else if (dateSplit[0]>1000 & dateSplit[0]<=currentTime.getFullYear() & dateSplit[1]>=1 & dateSplit[1]<=12 &  dateSplit[2]>=1 & dateSplit[2]<=31){
            document.getElementById("dateofbirthMessage").innerHTML = "Right";
            return true;
        }
        else{
        document.getElementById("dateofbirthMessage").innerHTML = "Wrong";
        return false;
        }
   
    }


}

function tgl(element){
if (element.value == 'y'){
document.getElementById("dateofbirth").disabled = true;
document.getElementById("dateofbirthRangeFrom").disabled = false;
document.getElementById("dateofbirthRangeTo").disabled = false;
}
else{
document.getElementById("dateofbirth").disabled = false;
document.getElementById("dateofbirthRangeFrom").disabled = true;
document.getElementById("dateofbirthRangeTo").disabled = true;
}
}




function showStuff(id) {
    document.getElementById(id).style.display = 'block';
	}

function hideStuff(id) {
		document.getElementById(id).style.display = 'none';
	}
