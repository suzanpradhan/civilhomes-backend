from .models import HomePageBasic

def get_contact_details(request):
    mainHomeData = HomePageBasic.objects.first()
    contactInfo = mainHomeData.contactInfo
    return {
        "contactInfo":contactInfo,
    }