from firebase import firebase
from datetime import date
import sys


firebaseref = firebase.FirebaseApplication("https://njvidhyalay-4f0ea.firebaseio.com")

today = date.today()
d1 = today.strftime("%d/%m/%Y")

string1 = "/std10A/"

for x in range(2):
    firebaseref.put(string1+'linkdetails/2','link','https://us02web.zoom.us/j/81139258056?pwd=NUxuOUNRYkh4Q2xIYmsxbVdoaGpndz09')
    firebaseref.put(string1+'linkdetails/2','date', d1)
    firebaseref.put(string1+'linkdetails/2','subject','અંગ્રેજી')
    string1 = "/std10B/"