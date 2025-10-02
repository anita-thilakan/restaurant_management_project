from django.db import models

# Create your models here.
class MenuCategory(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length= 250, unique=True)
=======
    name = models.CharField(max_length = 250, unique = True)
>>>>>>> bac5e779490cd9da5091f129f83c3043fd071cc9

    def __str__(self):
        return self.name