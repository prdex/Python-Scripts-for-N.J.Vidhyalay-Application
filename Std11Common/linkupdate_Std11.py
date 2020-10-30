from firebase import firebase
from datetime import date
import sys


firebaseref = firebase.FirebaseApplication("https://njvidhyalay-4f0ea.firebaseio.com")

today = date.today()
d1 = today.strftime("%d/%m/%Y")

linkvar = "https://us02web.zoom.us/j/86750828753?pwd=c0pldlJDcHpSMEp3SHQvVThvWTRlQT09"
subjectvar = "ગુજરાતી"

string1 = "/std11A/"

for x in range(2):
    firebaseref.put(string1+'linkdetails/1','link',linkvar)
    firebaseref.put(string1+'linkdetails/1','date', d1)
    firebaseref.put(string1+'linkdetails/1','subject',subjectvar)
    string1 = "/std11C/"