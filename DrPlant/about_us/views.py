from django.shortcuts import render

# Create your views here.
def about_us_def(request):
    return render(request, "about_us.html")
