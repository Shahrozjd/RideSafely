import pyrebase
from subprocess import call
from os import system
from datetime import datetime
import uuid
import base64



# Convert from String To image    
# imgdata = base64.b64decode(str)
# filename = "E:\\vsDjango\\sampleimage\\imageToSave.png"  
# with open(filename, 'wb') as f:
#     f.write(imgdata)

#Image to String
with open("E:\\vsDeepLearning\\Fyp_data\\Dataset\\frame1137.jpg", "rb") as imageFile:
    image_str = base64.b64encode(imageFile.read())
    
    
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

CID = uuid.uuid1()
var = CID.hex
challanid = var[:5]
citizenid = var[5:10]
data = {
    
    "ChallanID":challanid,
    "CitizenID":citizenid,
    "Name":"Azeem",
    "Address":"FSD,Punjab",
    "MOBILE":"03243534565",
    "CNIC":"3310075687878",
    "LiceneseNo":"FDR 4564",
    "Make":"Cd 70",
    "Color":"red",
    "Chassis":"56454jkj4kl5j",
    "Dateofissue":"1/4/2020",
    "DueDate":"1/8/2020",
    "PenaltyPoints":"1",
    "Paidchallan":"0",
    "UnpaidChallan":"1",
    "ChallanAmount":"500PKR",
}

db.child("Challans").child(challanid).set(data)
print("DONE")

# db.child("Challans").child('06521').update(data)

# value = db.child("Challans").child("06521").get()

# valdata = dict(value.val())
# print(valdata['Address'])
# # print("ImageString : "+str(value.val()['IMAGE']))
# # image_str = str(image_str, 'utf-8')
# # print(image_str)
# imgdata = base64.b64decode(valdata['IMAGE'])
# filename = "C:\\Users\\Shahroz Javed\\Desktop\\RideSafely\\RideSafely\\sampleimage1.png"  
# with open(filename, 'wb') as f:
#     f.write(imgdata)
