from django.contrib import admin
from .models import RequestedFeatures, PredictedPrice,JSONFile,MLModel
# Register your models here.
admin.site.register(RequestedFeatures)
admin.site.register(PredictedPrice)
admin.site.register(JSONFile)
admin.site.register(MLModel)