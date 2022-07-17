from django.db import models

# Create your models here.
#from rest_framework.validators import UniqueTogetherValidator


class Store(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    description = models.CharField(max_length=800, verbose_name='description')
    ratings = models.IntegerField()
    creator = models.ForeignKey('auth.User', related_name='stores', on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.CharField(max_length=100, verbose_name='owner', null=True, blank=True)
    status = models.CharField(max_length=100, verbose_name='status', default='in_review', choices=(
        ('active','active'),
        ('deactivated', 'deactivated'),
        ('in_review', 'in_review'))
    )



    # class Meta:
    #     validators = [
    #         UniqueTogetherValidator(
    #             queryset=Store.objects.all(),
    #             fields=['title', 'description', 'ratings']
    #         )
    #     ]