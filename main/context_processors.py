import datetime
from main.models import SiteInfo


def get_current_year_to_context(request):
    current_datetime = datetime.datetime.now()

    return {
        'current_year': current_datetime.year
    }


def get_site_info(request):
    site_info = SiteInfo.objects.all()

    if len(site_info) == 0:
        return {
            'site_info': None
        }
    else:
        return {
            'site_info': site_info[0]
        }