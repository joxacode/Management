from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=125)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, verbose_name="parent", related_name='children', null=True, blank=True)
    icon = models.CharField(max_length=50, verbose_name="Icon", null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.name}'


