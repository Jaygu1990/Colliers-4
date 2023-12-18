from django.db import models

# Create your models here.
class revrecmodel(models.Model):
    name = models.CharField(max_length=256)
    deal = models.PositiveIntegerField()
    due_date = models.DateField()
    note = models.CharField(max_length=256,blank=True)
    assign_status = models.CharField(max_length=256,blank=True,default='unassigned')
    test_status = models.CharField(max_length=256,blank=True,default='untested')
    def __str__(self):
        return self.name