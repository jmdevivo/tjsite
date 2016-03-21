function Testimonial(id, illness_id, patient_number, testimonial_body, language) {
	this.id = id;
	this.illness_id = illness_id;
	this.patient_number = patient_number;
	this.testimonial_body = testimonial_body;
	this.language = language;
}

Testimonial.prototype.render = function() {
	$('#testimonial-patient-num').html("Patient "+ this.patient_number);
	$('#testimonial-patient-lang').html(this.language);
	$('#testimonial-body').html(this.testimonial_body);	
}