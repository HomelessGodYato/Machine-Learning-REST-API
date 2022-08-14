from django.contrib import admin
from .models import RequestedFeatures, PredictedPrice,JSONFile
# Register your models here.
admin.site.register(RequestedFeatures)
admin.site.register(PredictedPrice)
admin.site.register(JSONFile)
