from django.db import models

class responsibility(models.Model):
    name = models.CharField(max_length=256)
    task1 = models.CharField(max_length=256, null=True, blank=True)
    task2 = models.CharField(max_length=256, null=True, blank=True)
    task3 = models.CharField(max_length=256, null=True, blank=True)
    task4 = models.CharField(max_length=256, null=True, blank=True)
    task5 = models.CharField(max_length=256, null=True, blank=True)
    task6 = models.CharField(max_length=256, null=True, blank=True)
    task7 = models.CharField(max_length=256, null=True, blank=True)
    task8 = models.CharField(max_length=256, null=True, blank=True)
    task9 = models.CharField(max_length=256, null=True, blank=True)
    task10 = models.CharField(max_length=256, null=True, blank=True)
    task11 = models.CharField(max_length=256, null=True, blank=True)
    task12 = models.CharField(max_length=256, null=True, blank=True)
    task13 = models.CharField(max_length=256, null=True, blank=True)
    task14 = models.CharField(max_length=256, null=True, blank=True)
    task15 = models.CharField(max_length=256, null=True, blank=True)
    task16 = models.CharField(max_length=256, null=True, blank=True)
    task17 = models.CharField(max_length=256, null=True, blank=True)
    task18 = models.CharField(max_length=256, null=True, blank=True)
    task19 = models.CharField(max_length=256, null=True, blank=True)
    task20 = models.CharField(max_length=256, null=True, blank=True)
    def __str__(self):
        return self.name
