from django.db import models


# Create your models here.
class RequestedFeatures(models.Model):
    brand = models.IntegerField(blank=False, null=False)
    body = models.IntegerField(blank=False, null=False)
    mileage = models.IntegerField(blank=False, null=False)
    engine_v = models.FloatField(blank=False, null=False)
    engine_type = models.IntegerField(blank=False, null=False)
    registration = models.BooleanField(blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    model = models.IntegerField(blank=False, null=False)


class PredictedPrice(models.Model):
    request_id = models.ForeignKey(RequestedFeatures, related_name="request_id", on_delete=models.CASCADE)
    predicted_price = models.FloatField(blank=False, null=False)
