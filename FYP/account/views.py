from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
from subprocess import call
from os import system

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
print("*****"+str(valdata))



def home(request):
    return render(request,'account/home.html')


def challans(request):
    msg = {"insert":valdata}
    return render(request,'account/challans.html',context=msg)

def showchallandata(request):
    username = request.GET.get("challanid")
    value = db.child("Challans").child(username).get()
    valdata = dict(value.val())
    msg = {"userchallan":valdata}
    return render(request,'account/showchallandata.html',context=msg)

    


