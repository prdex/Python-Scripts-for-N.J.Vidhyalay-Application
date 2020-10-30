from firebase import firebase
from datetime import date
import sys


firebaseref = firebase.FirebaseApplication("https://njvidhyalay-4f0ea.firebaseio.com")

today = date.today()
d1 = today.strftime("%d/%m/%Y")

string1    = "/std12A/"
linkvar    = "https://us02web.zoom.us/j/86168122224?pwd=S3FjT01JQldHMmkrQVhHYmwycXNMQT09"
subjectvar = "અંગ્રેજી"

for x in range(2):
    firebaseref.put(string1+'linkdetails/1','link', linkvar)
    firebaseref.put(string1+'linkdetails/1','date', d1)
    firebaseref.put(string1+'linkdetails/1','subject', subjectvar)
    string1 = "/std12C/"