from django.db import models

# Create your models here.
#from rest_framework.validators import UniqueTogetherValidator


class Store(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    description = models.CharField(max_length=800, verbose_name='description')
    ratings = models.IntegerField()

    # class Meta:
    #     validators = [
    #         UniqueTogetherValidator(
    #             queryset=Store.objects.all(),
    #             fields=['title', 'description', 'ratings']
    #         )
    #     ]