from django.db import models

Programme_Choice = (
    ("Donation","Donation"),
    ("Volunteer","Volunteer"),
)

class Gallery(models.Model):
    Image = models.ImageField(upload_to="Gallery_Images")
    Alt = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.Alt}"

class Volunteer(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to="Volunteer_Images")
    Position = models.CharField(max_length=100)
    About = models.TextField()
    Facebook = models.URLField(max_length=2000)
    Twitter = models.URLField(max_length=2000)
    Instagram = models.URLField(max_length=2000)

    def __str__(self):
        return f"{self.Name}"

class Programme(models.Model):
    Name = models.CharField(max_length=200)
    Image = models.ImageField(upload_to="Programme_Images")   
    Short_Detail = models.TextField()
    Full_Detail = models.TextField()
    
    Type = models.CharField(choices=Programme_Choice, max_length=50)

    # If Donation
    Money_to_raise = models.FloatField()
    Raised_till_now = models.FloatField()

    def __str__(self):
        return f"{self.Name}"

class Blog(models.Model):

    Featured_Image = models.ImageField(upload_to="Blog_Images")
    Title = models.CharField(max_length=2000)
    Text = models.TextField()

    def __str__(self):
        return f"{self.Title}"
    