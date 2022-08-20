from django.db import models
from django.conf import settings


# Create your models here.
class JSONFile(models.Model):
    file = models.FileField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)


class RequestedFeatures(models.Model):
    file_id = models.ForeignKey(JSONFile, related_name="features", on_delete=models.CASCADE)
    carat = models.FloatField(blank=False, null=False)
    cut = models.CharField(max_length=25, blank=False, null=False)
    color = models.CharField(max_length=25, blank=False, null=False)
    clarity = models.CharField(max_length=25, blank=False, null=False)
    depth = models.FloatField(blank=False, null=False)
    table = models.FloatField(blank=False, null=False)
    x = models.FloatField(blank=False, null=False)
    y = models.FloatField(blank=False, null=False)
    z = models.FloatField(blank=False, null=False)


class PredictedPrice(models.Model):
    features_id = models.ForeignKey(RequestedFeatures, related_name="prediction", on_delete=models.CASCADE)
    predicted_price = models.FloatField(blank=False, null=False)
