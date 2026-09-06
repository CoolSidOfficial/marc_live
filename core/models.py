from django.db import models



class Profile(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    tagline = models.TextField()
    photo = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name