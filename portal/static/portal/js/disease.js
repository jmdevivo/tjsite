//set up the disease class
function Disease(id, name, description, causes, symptoms, risk_factors) {
	this.id = id;
	this.name = name;
	this.description = description;
	this.causes = causes;
	this.symptoms = symptoms;
	this.risk_factors = risk_factors;
}

//define the disease render functon
Disease.prototype.render = function() {

	document.getElementsByClassName('disease-name')[0].innerHTML = this.name;
	document.getElementById('disease-description').innerHTML = this.description;
	document.getElementById('disease-causes').innerHTML = this.causes;
	document.getElementById('disease-symptoms').innerHTML = this.symptoms;
	document.getElementById('disease-risk-factors').innerHTML = this.risk_factors;

}

Disease.prototype.fetchTestimonials = function(url){
	$.post(url, {'illness_id': this.id}, function(response){
		var parent = document.getElementsByClassName('disease-list')[0]
		var decoded = JSON.parse(response);
		var resp_length = decoded.length;
		console.log(resp_length);
		for(var i = 0; i<resp_length; i++){
			var div = document.createElement('div');
			div.className = 'testimonial';
			div.innerHTML = "Testimonial "+decoded[i].patient_number;
			div.testimonial =  new Testimonial(decoded[i].id,decoded[i].illness_id, decoded[i].patient_number,decoded[i].testimonial_body, decoded[i].language);
			parent.appendChild(div);

		}
		$('.testimonial').click(function(){

			$('.testimonial').each(function(){
				this.style.textDecoration = 'none';
				this.style.color = '#6c6e6f';
			});
			this.style.textDecoration = 'underline';
			this.style.color = '#69987d';
			this.testimonial.render();
		});
	});
}