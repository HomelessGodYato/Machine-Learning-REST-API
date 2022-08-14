from django.contrib import admin
from .models import RequestedFeatures, PredictedPrice
# Register your models here.
admin.site.register(RequestedFeatures)
admin.site.register(PredictedPrice)
