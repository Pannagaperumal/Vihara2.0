from django.shortcuts import render
from .models import destination

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render

#from pann.speed.models import destination

# Create your views here.
def index(request):
    dests = destination.objects.all()
    return render(request, "index.html",{'dests': dests})

    '''
    dest1 = destination()
    dest1.name ='Banglore'
    dest1.img= 'banglore1.jpg'
    dest1.desc ='Silicon valley of India'
    dest1.offer= True
    dest2=destination()
    dest2.name='Mysore'
    dest2.img='images/mysore.jpg'
    dest2.desc='The Heritage city'
    dest2.offer= False

    dest3=destination()
    dest3.name='Jaipur'
    dest3.img='images/jaipur.jpg'
    dest3.desc='THE Pink City Of India'
    dest3.offer= True


    dest4= destination()
    dest4.name='Tiruvanantapuram,Kerala'
    dest4.img='images/kerala.jpg'
    dest4.desc="THe God's Own Country"

    dests=[dest1,dest2,dest3,dest4]
   '''
    

