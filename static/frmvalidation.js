function validateForm(){
document.getElementById("validate").value = "inside validateFrom";
    if (!validateDate()){
        document.getElementById("validate").innerHTML = "0";
        return false;
    }
    else {
        document.getElementById("validate").innerHTML = "1";
        return true;
    }

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


function toggle(element){
if (element.value == 'y'){
document.getElementById("dateofbirth").disabled = true;
document.getElementById("dateofbirthRangeFrom").disabled = false;
document.getElementById("dateofbirthRangeTo").disabled = false;
validateForm()}
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
