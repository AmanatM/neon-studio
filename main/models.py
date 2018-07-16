from django.db import models

# Create your models here.

class Content(models.Model):

	title = models.CharField(max_length=50, default='')
	features_heading = models.CharField(max_length=50, default='Почему мы?')

	feature_1_text = models.CharField(max_length=200, default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?')
	feature_2_text = models.CharField(max_length=200, default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?')
	feature_3_text = models.CharField(max_length=200, default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?')
	feature_4_text = models.CharField(max_length=200, default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?')
	feature_5_text = models.CharField(max_length=200, default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?')
	feature_6_text = models.CharField(max_length=200, default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?')
	feature_7_text = models.CharField(max_length=200, default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?')
	feature_8_text = models.CharField(max_length=200, default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?')
	feature_9_text = models.CharField(max_length=200, default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Laudantium, magni?')




	def __str__(self):
		return self.title


