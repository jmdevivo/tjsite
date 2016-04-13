from __future__ import unicode_literals

from django.db import models

class Illness(models.Model):
	name = models.CharField(max_length=150)
	causes = models.CharField(max_length=1000)
	symptoms =  models.CharField(max_length=1000)
	risk_factors = models.CharField(max_length=1000)

	def __str__(self):
		return self.name

class Testimonial(models.Model):
	illness = models.ForeignKey(Illness)
	patient_number = models.IntegerField()
	testimonial_body = models.CharField(max_length=5000)
	language = models.CharField(max_length=100)

class FAQ(models.Model):
	question = models.TextField()
	answer=models.TextField()

class SiteText(models.Model):
	home_body = models.TextField()
	home_side = models.TextField()
	philosophy_body = models.TextField()
	home_main = models.TextField()
	about_main = models.TextField()