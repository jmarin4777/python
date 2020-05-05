from django.shortcuts import render
from datetime import datetime
# Create your views here.
def root(request):
    var = {
        "date": datetime.now().strftime("%h %d, %Y"),
        "time": datetime.now().strftime("%I:%M %p")
    }
    return render(request, "timeDisplay.html", var)