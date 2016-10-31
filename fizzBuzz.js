//Fizz Buzz in JS

var returnString;

for(var x = 0;x < 100; x++){
	returnString = "";
	var y = x+1;
	
	if(y % 3 === 0){
		returnString += "Fizz";
	}
	if(y % 5 === 0){
		returnString += "Buzz";
	}
	if(returnString == ""){
		returnString = String(y);
	}
	
	console.log(returnString);
}