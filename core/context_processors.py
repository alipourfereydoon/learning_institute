from .models import SiteSetting
def site_settings(request):
    return {'site_config': SiteSetting.objects.first()}
