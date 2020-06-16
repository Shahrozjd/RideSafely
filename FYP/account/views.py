from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pyrebase
from subprocess import call
from django.contrib.auth.decorators import login_required
from os import system
from . import updform
import base64

from .models import City, due
from django.contrib import messages

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





def home(request):
    return render(request,'account/home.html')

#graphs started
@login_required
def graphs(request):
    return render(request,'account/graphs.html')

@login_required
def graph1(request):
    labels = []
    data = []

    queryset = City.objects.order_by('-challans')[:6]
    for city in queryset:
        labels.append(city.name)
        data.append(city.challans)

    return render(request, 'account/graph1.html', {
        'labels': labels,
        'data': data,
    })
    
@login_required
def graph2(request):
    labels = []
    data1 = []
    data2=[]

    queryset = due.objects.order_by('-paid')[:10]
    for Due in queryset:
        labels.append(Due.months)
        data1.append(Due.paid)
        data2.append(Due.unpaid)



    return render(request, 'account/graph2.html',{
        'data1':data1,
    'data2':data2,
        'labels':labels
    })

#graphs ended

#challans started
@login_required
def challans(request):
    idTodlt = request.GET.get("id_to_dlt")
    if idTodlt:
        db.child("Challans").child(idTodlt).remove()
    value = db.child("Challans").shallow().get()
    valdata = list(value.val())        
    msg = {"insert":valdata}
    return render(request,'account/challans.html',context=msg)

def showchallandata(request):
    username = request.GET.get("challanid")
    value = db.child("Challans").child(username).get()
    if(not value.val()):
        print("*******GADISH********")
        messages.info(request, 'No Challan found for this ID')
        return HttpResponseRedirect('/')
        # return render(request,'account/home.html',context=msg)
    else:    
        valdata = dict(value.val())
        # imgdata = base64.b64decode(valdata['IMAGE'])
        # filename = "C:\\Users\\Shahroz Javed\\Desktop\\RideSafely\\RideSafely\\FYP\\account\\static\\account\\image"+value.val()['ChallanID']+".png"  
        # with open(filename, 'wb') as f:
        #     f.write(imgdata)s
        msg = {"userchallan":valdata}
        return render(request,'account/showchallandata.html',context=msg)

#challans ended
    
#update challan form
def updateform(request):
    form = updform.upd_form()
    username = request.GET.get("id_to_updt")
    value = db.child("Challans").child(username).get()
    valdata = dict(value.val())
    form.fields["name"].initial = valdata['Name']
    form.fields["challanid"].initial = valdata['ChallanID']
    form.fields["citizenid"].initial = valdata['CitizenID']
    form.fields["challanamount"].initial = valdata['ChallanAmount']
    form.fields["cnic"].initial = valdata['CNIC']
    form.fields["address"].initial = valdata['Address']
    form.fields["mobile"].initial = valdata['MOBILE']
    form.fields["duedate"].initial = valdata['DueDate']   
    form.fields["issuedate"].initial = valdata['Dateofissue']
    form.fields["liceneseno"].initial = valdata['LiceneseNo']
    form.fields["chasis"].initial = valdata['Chassis']
    form.fields["color"].initial = valdata['Color']
    form.fields["make"].initial = valdata['Make']
    form.fields["paidchallan"].initial = valdata['Paidchallan']
    form.fields["unpaidchallan"].initial = valdata['UnpaidChallan']
    form.fields["penaltypoint"].initial = valdata['PenaltyPoints']
    
    msg = {'form':form}
    if(request.method == 'POST'):
        form = updform.upd_form(request.POST)
        if form.is_valid():
            data = {
    
                    "ChallanID":form.cleaned_data['challanid'],
                    "CitizenID":form.cleaned_data['citizenid'],
                    "Name":form.cleaned_data['name'],
                    "Address":form.cleaned_data['address'],
                    "MOBILE":form.cleaned_data['mobile'],
                    "CNIC":form.cleaned_data['cnic'],
                    "LiceneseNo":form.cleaned_data['liceneseno'],
                    "Make":form.cleaned_data['make'],
                    "Color":form.cleaned_data['color'],
                    "Chassis":form.cleaned_data['chasis'],
                    "Dateofissue":form.cleaned_data['issuedate'],
                    "DueDate":form.cleaned_data['duedate'],
                    "PenaltyPoints":form.cleaned_data['penaltypoint'],
                    "Paidchallan":form.cleaned_data['paidchallan'],
                    "UnpaidChallan":form.cleaned_data['unpaidchallan'],
                    "ChallanAmount":form.cleaned_data['challanamount'],

                    }
            db.child("Challans").child(username).update(data)
            print("Validation Done") 
    
    return render(request,'account/updateform.html',context=msg)    


