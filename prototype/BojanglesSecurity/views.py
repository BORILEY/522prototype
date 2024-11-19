from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import PrivacySettings

# Create your views here.

class HomeView(TemplateView):
    template_name = "BojanglesSecurity/home.html"  # Replace with your actual template path
    

@csrf_exempt
def update_privacy_setting(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            setting_id = data.get("id")
            field = data.get("field")
            value = data.get("value")

            # Validate and update the setting
            privacy_setting = get_object_or_404(PrivacySettings, id=setting_id)
            if hasattr(privacy_setting, field):
                setattr(privacy_setting, field, value)
                privacy_setting.save()
                return JsonResponse({"success": True, "message": f"{field} updated to {value}."})
            else:
                return JsonResponse({"success": False, "message": "Invalid field."}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)}, status=400)
    return JsonResponse({"success": False, "message": "Invalid request method."}, status=405)