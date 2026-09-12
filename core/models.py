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
class Website(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField()
    skills = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="websites/icons/", blank=True, null=True)
    preview = models.ImageField(upload_to="websites/previews/", blank=True, null=True)
    traffic = models.PositiveIntegerField(default=0)
    live = models.BooleanField(default=True)

    def __str__(self):
        return self.title