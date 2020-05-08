from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
from subprocess import call
from os import system
import base64

from .models import City

config = {
    "apiKey": "AIzaSyBfGWLK-_W_mwNUSskbyJdh1YPnHuhJM7U",
    "authDomain": "ridesafely-e7c52.firebaseapp.com",
    "databaseURL": "https://ridesafely-e7c52.firebaseio.com",
    "projectId": "ridesafely-e7c52",
    "storageBucket": "ridesafely-e7c52.appspot.com",
    "messagingSenderId": "257867644694",
    "appId": "1:257867644694:web:7c9c63f8dcc4aaece69a37",
    "measurementId": "G-0202R98KBF"}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

value = db.child("Challans").shallow().get()

valdata = list(value.val())
print("**ID'S**"+str(valdata))



def home(request):
    return render(request,'account/home.html')

#graphs started
def graphs(request):
    return render(request, 'account/graphs.html')

def graph1(request):
    labels = []
    data = []

    queryset = City.objects.order_by('-challans')[:5]
    for city in queryset:
        labels.append(city.name)
        data.append(city.challans)

    return render(request, 'account/graph1.html', {
        'labels': labels,
        'data': data,
    })

#graphs ended

#challans started
def challans(request):
    msg = {"insert":valdata}
    return render(request,'account/challans.html',context=msg)

def showchallandata(request):
    username = request.GET.get("challanid")
    value = db.child("Challans").child(username).get()
    valdata = dict(value.val())
    # imgdata = base64.b64decode(valdata['IMAGE'])
    # filename = "C:\\Users\\Shahroz Javed\\Desktop\\RideSafely\\RideSafely\\FYP\\account\\static\\account\\image"+value.val()['ChallanID']+".png"  
    # with open(filename, 'wb') as f:
    #     f.write(imgdata)s
    msg = {"userchallan":valdata}
    return render(request,'account/showchallandata.html',context=msg)

#challans ended
    


