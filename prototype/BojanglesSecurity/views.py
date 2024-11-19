from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import PrivacySettings, Device

class HomeView(ListView):
    template_name = "BojanglesSecurity/home.html"
    context_object_name = "device_list"
    
    def get_queryset(self):
        return Device.objects.all()

class DeviceSettingsView(TemplateView):
    template_name = "BojanglesSecurity/deviceSettings.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the device instance using the pk passed in the URL
        device_id = kwargs['pk']
        device = get_object_or_404(Device, id=device_id)
        
        # Check if there's a corresponding PrivacySettings instance
        privacy_settings = PrivacySettings.objects.filter(device=device).first()

        # If no PrivacySettings instance exists, create one with default values
        if not privacy_settings:
            privacy_settings = PrivacySettings.objects.create(device=device)

        context['device'] = device
        context['privacy_settings'] = privacy_settings
        return context
    

@csrf_exempt
def update_privacy_setting(request):
    if request.method == "POST":
        try:
            # Parse the incoming JSON request body
            data = json.loads(request.body)
            print("Received data:", data)  # Debug print to check the data received

            # Extract the device ID from the data (sent as part of the JSON)
            setting_id = data.get("id")
            if not setting_id:
                return JsonResponse({"success": False, "message": "Device ID is missing."}, status=400)

            # Retrieve the device object using the device ID
            device = get_object_or_404(Device, id=setting_id)
            # Get or create the corresponding PrivacySettings for the device
            privacy_settings, created = PrivacySettings.objects.get_or_create(device=device)

            # Iterate through the fields in the JSON data and update the corresponding PrivacySettings
            for field, value in data.items():
                if field != 'id':  # Don't update the ID field
                    if hasattr(privacy_settings, field):
                        setattr(privacy_settings, field, value)
                    else:
                        return JsonResponse({"success": False, "message": f"Invalid field: {field}"}, status=400)

            privacy_settings.save()

            return JsonResponse({"success": True, "message": "Settings updated successfully."})
        
        except Exception as e:
            return JsonResponse({"success": False, "message": f"Error: {str(e)}"}, status=400)

    return JsonResponse({"success": False, "message": "Invalid request method."}, status=405)