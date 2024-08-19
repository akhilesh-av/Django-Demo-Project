from django.db import models

class CensorInfo(models.Model):
    ratting = models.CharField(max_length=10,null=True)
    certified_by = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.certified_by
    
    
class Director(models.Model):
    name = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name


class MovieInfo(models.Model):
    title =models.CharField(max_length=100)
    year = models.IntegerField()
    summary = models.CharField(max_length=250)
    poster =  models.ImageField(upload_to='images/',null=True)
    censor_details =models.OneToOneField(CensorInfo,on_delete=models.SET_NULL,related_name='movie',null=True)
    directed_by = models.ForeignKey(Director,on_delete=models.CASCADE,null=True,related_name='directed_movie')
    
    def __str__(self):
        return self.title
    

    
    

    
