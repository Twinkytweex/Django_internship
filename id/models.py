from django.db import models
from django.utils import timezone
from PIL import Image


class Id(models.Model):
    image = models.ImageField(default="", upload_to="images")
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    location = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    citizen = models.CharField(max_length=20)
    card_num = models.CharField(max_length=20)
    number_id = models.CharField(max_length=11)
    date_of_birth = models.DateField(default=timezone.now)
    validit_period = models.DateField(default=timezone.now)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image)
        if img.height > 200 and img.width > 200:
            size = (100, 100)
            img.thumbnail(size)
            img.save(self.image.path)
