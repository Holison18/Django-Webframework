from django.http import HttpResponse

def home_page_view(request):
    return HttpResponse("""Hello there👋! My name is Kobina Akofi-Holison. I am a computer engineering student""")