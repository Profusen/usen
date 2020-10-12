from django.db import models


class Introduction(models.Model):
    Brief_History = models.CharField(max_length=3000)
    Objectives = models.CharField(max_length=3000)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Objectives

    class Meta:
        verbose_name_plural = 'Introduction'


class Water(models.Model):
    Mission_Statement = models.CharField(max_length=3000)
    Quality_control_unit = models.CharField(max_length=3500)
    Laboratory_instrument = models.CharField(max_length=3500)
    introduction = models.ForeignKey(Introduction, on_delete=models.CASCADE)

    def __str__(self):
        return self.Quality_control_unit

    class Meta:
        verbose_name_plural = 'Water'


class Water_Analysis(models.Model):
    Sources = models.CharField(max_length=4000)
    Quality = models.CharField(max_length=4000)
    Physical_Analysis = models.CharField(max_length=4500)
    Turbidity = models.CharField(max_length=4500)

    def __str__(self):
        return self.Sources

    class Meta:
        verbose_name_plural = 'Water_Analysis'


class Water_Treatment(models.Model):
    Coagulation = models.CharField(max_length=4000)
    Sedimentation = models.CharField(max_length=4000)
    Chlorination = models.CharField(max_length=4000)
    Water_Analysis = models.ForeignKey(Water_Analysis, on_delete=models.CASCADE)

    def __str__(self):
        return self.Coagulation

    class Meta:
        verbose_name_plural = 'Water_Treatment'

# Create your models here.
