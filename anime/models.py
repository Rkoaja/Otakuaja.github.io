from django.db import models

# Create your models here.
class Studio (models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name
    
class Produser (models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name
    

class Anime (models.Model):
    title = models.CharField(max_length=100)
    rating = models.FloatField(default=0.0)
    produser = models.ForeignKey(Produser, on_delete=models.CASCADE)
    tipe = models.CharField(max_length=20)
    status = models.CharField(max_length=50)
    episode = models.IntegerField()
    duration = models.CharField(max_length=20)
    release_date = models.DateField()
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    genre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='anime_images/', blank=True, null=True)
    description = models.TextField()

    def __str__(self) -> str:
         return self.title