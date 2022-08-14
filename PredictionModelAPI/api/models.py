from django.db import models


# Create your models here.
class RequestedFeatures(models.Model):
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
    request_id = models.ForeignKey(RequestedFeatures, related_name="request_id", on_delete=models.CASCADE)
    predicted_price = models.FloatField(blank=False, null=False)
