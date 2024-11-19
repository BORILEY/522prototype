from django.db import models

# Create your models here.

class PrivacySettings(models.Model):
    EnableDataCollection = models.BooleanField(default=True)
    ActivityTracking = models.BooleanField(default=True)
    VoiceDataCollection = models.BooleanField(default=True)
    LocationTracking = models.BooleanField(default=True)
    ShareDataWithThirdParties = models.BooleanField(default=True)
    AllowUsageTracking = models.BooleanField(default=True)
    DataEncryption = models.BooleanField(default=True)
    StorePersonalUsageData = models.BooleanField(default=True)
    StorePurchaseHistory = models.BooleanField(default=True)
    AllowDataCollectionForCrossDevice = models.BooleanField(default=True)