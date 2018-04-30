from django.db import models

# Create your models here.
class Map(models.Model):
    #id_num = models.IntegerField()
    import_country = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    sold_by = models.CharField(max_length=200)
    sale_price = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return self.import_country

