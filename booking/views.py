from django.shortcuts import render
import accounts.views as acc
# Create your views here.
def booking(request):
    if request=='POST':
        acc.login()
    return render(request,'booking.html')