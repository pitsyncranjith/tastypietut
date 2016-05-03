from django.db import models

class Demo(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()

	def __unicode__(self):
		return self.name


