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
