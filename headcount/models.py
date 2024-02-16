from django.db import models

class Headcount(models.Model):
    id_employee = models.CharField(max_length=300, null=False)
    ds_category_1 = models.CharField(max_length=300, null=False)
    ds_category_2 = models.CharField(max_length=300, null=False)
    ds_category_3 = models.CharField(max_length=300, null=False)
    ds_category_4 = models.CharField(max_length=300, null=False)
    ds_category_5 = models.CharField(max_length=300, null=False)
    fg_status = models.IntegerField()
    fg_dismissal_on_month = models.IntegerField()
    dt_reference_month = models.DateField()