from firebase import firebase
from datetime import date
import sys


firebaseref = firebase.FirebaseApplication("https://njvidhyalay-4f0ea.firebaseio.com")

today = date.today()
d1 = today.strftime("%d/%m/%Y")

string1 = "/std12A/"

for x in range(2):
    firebaseref.put(string1+'linkdetails/1','link','https://us02web.zoom.us/j/84224407442?pwd=eTZPL1FKRzBOemU1U1NPaThZSEd4Zz09')
    firebaseref.put(string1+'linkdetails/1','date', d1)
    firebaseref.put(string1+'linkdetails/1','subject','અર્થશાસ્ત્ર')
    string1 = "/std12C/"