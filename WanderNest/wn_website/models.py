from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Transport(models.Model):
    name = models.CharField(max_length=255,blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Tour(models.Model):
    title= models.CharField(max_length=255)
    img_url = models.CharField(max_length=500, blank=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transport = models.ForeignKey(Transport,on_delete=models.CASCADE)
    creation_tour_date = models.DateTimeField(auto_created=True)
    slug = models.SlugField(unique=True,blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tour_details',kwargs={'tour':self.slug})

class Booking(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour,on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'User:{self.user}. Booked tour:{self.tour}'
