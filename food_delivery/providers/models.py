from django.db import models


# Create your models here.
class Restaurants(models.Model):
    """Information od Cook who Provide the Foods"""
    res_name = models.CharField(max_length=100, blank=False)
    res_image = models.ImageField(blank=False, upload_to='images')
    contact_no = models.PositiveIntegerField(blank=False)
    x = models.DecimalField(max_digits=9, decimal_places=6,default=0.0)
    y = models.DecimalField(max_digits=9, decimal_places=6,default=0.0)
    content = models.TextField(default = 'none')


    class Meta:
        verbose_name_plural = "Restraunt's Infos"

    def __str__(self):
        """Returns Name of the Object"""
        return self.res_name

class Delivery_partners(models.Model):
    """Information od Cook who Provide the Foods"""
    name = models.CharField(max_length=100, blank=False)
    contact_no = models.PositiveIntegerField(blank=False)
    x = models.DecimalField(max_digits=9, decimal_places=6,default=0.0)
    y = models.DecimalField(max_digits=9, decimal_places=6,default=0.0)


    class Meta:
        verbose_name_plural = "Delivery partners"

    def __str__(self):
        """Returns Name of the Object"""
        return self.name