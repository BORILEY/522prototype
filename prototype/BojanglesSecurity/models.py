from django.db import models

# Create your models here.

class Device(models.Model):
    deviceName = models.TextField()
    def __str__(self):
        return f"{self.deviceName}"

class PrivacySettings(models.Model):
    EnableDataCollection = models.BooleanField(default=True)
    ActivityTracking = models.BooleanField(default=True)
    VoiceDataCollection = models.BooleanField(default=True)
    LocationTracking = models.BooleanField(default=True)
    ShareDataWithThirdParties = models.BooleanField(default=True)
    AllowUsageTracking = models.BooleanField(default=True)
    StorePersonalUsageData = models.BooleanField(default=True)
    StorePurchaseHistory = models.BooleanField(default=True)
    AllowDataCollectionForCrossDevice = models.BooleanField(default=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='privacy_settings')
    def __str__(self):
        return f"{self.device.deviceName} Settings"
    