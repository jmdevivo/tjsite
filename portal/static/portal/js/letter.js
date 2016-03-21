//set up the letter class
function Letter(letter, url){
	this.letter = letter;
	this.url = url;
}


//define the letter fetch function
//take in a view update function as 
//a parameter
Letter.prototype.fetch = function(updateView){

	var old_diseases = document.getElementsByClassName("disease");
	
	for(var i=0; i < old_diseases.length; i++){
		old_diseases[0].innerHTML = '';
	}

	var parent = document.getElementsByClassName('disease-list')[0];
	
	$.post(this.url ,{'letter': this.letter}, function(response){
		var decoded = JSON.parse(response);
		while(parent.hasChildNodes()){
			parent.removeChild(parent.lastChild);
		}
		for(var i = 0; i < decoded.length; i++){
			var div = document.createElement("div");
			div.className = 'disease';
			div.disease = new Disease(decoded[i].id, decoded[i].name, decoded[i].description, decoded[i].causes, decoded[i].symptoms, decoded[i].risk_factors);
			div.innerHTML = div.disease.name;
			parent.appendChild(div);
		}
		//updates view based on custum view input function provided
		updateView();

		
	});
}