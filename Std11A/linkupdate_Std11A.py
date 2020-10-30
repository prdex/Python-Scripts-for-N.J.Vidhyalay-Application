from firebase import firebase
from datetime import date
import sys


firebaseref = firebase.FirebaseApplication("https://njvidhyalay-4f0ea.firebaseio.com")

today = date.today()
d1 = today.strftime("%d/%m/%Y")

string1 = "/std11A/"

for x in range(2):
    firebaseref.put(string1+'linkdetails/1','link','https://us05web.zoom.us/j/6962323986?pwd=VitoRFpwR3luZ1g3cUE4eFdDRzhPZz09')
    firebaseref.put(string1+'linkdetails/1','date', d1)
    firebaseref.put(string1+'linkdetails/1','subject','અંગ્રેજી')
    string1 = "/std11C/"