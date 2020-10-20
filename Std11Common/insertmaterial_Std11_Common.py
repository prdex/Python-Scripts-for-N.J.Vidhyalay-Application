from firebase import firebase
from firebase import firebase
from datetime import date
import sys

firebaseref = firebase.FirebaseApplication("https://njvidhyalay-4f0ea.firebaseio.com")

english = "%E0%AA%85%E0%AA%82%E0%AA%97%E0%AB%8D%E0%AA%B0%E0%AB%87%E0%AA%9C%E0%AB%80/"
gujarati = "%E0%AA%97%E0%AB%81%E0%AA%9C%E0%AA%B0%E0%AA%BE%E0%AA%A4%E0%AB%80/"
eco     = "%E0%AA%85%E0%AA%B0%E0%AB%8D%E0%AA%A5%E0%AA%B6%E0%AA%BE%E0%AA%B8%E0%AB%8D%E0%AA%A4%E0%AB%8D%E0%AA%B0/"

today = date.today()
d1 = today.strftime("%d/%m/%Y")

linkvar = "https://drive.google.com/uc?id=14EPgaMcwTCGDUaeBVywduFkm8Uba-TNF&export=download"
namevar = "ગુજરાતી પ્રકરણ-૬"

data = {
    'downloadlink':linkvar,
    'name':namevar
}
standard1 = "/std11A/"

print("Enter subject code")
subjectindex = input().strip()

for x in range(2):
    if subjectindex == "1":
        result = firebaseref.get(standard1+"materiallink/"+english,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'materiallink/'+english+firstelementindex, data)
        firebaseref.put(standard1+'materiallink/'+english+firstelementindex,'downloadlink',linkvar)
        firebaseref.put(standard1+'materiallink/'+english+firstelementindex,'name',namevar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'materiallink/'+english+firstelementindex, stringdelete)  
        standard1 = "/std11C/"
    
    elif subjectindex == "2":
        result = firebaseref.get(standard1+"materiallink/"+gujarati,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'materiallink/'+gujarati+firstelementindex, data)
        firebaseref.put(standard1+'materiallink/'+gujarati+firstelementindex,'downloadlink',linkvar)
        firebaseref.put(standard1+'materiallink/'+gujarati+firstelementindex,'name',namevar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'materiallink/'+gujarati+firstelementindex, stringdelete)  
        standard1 = "/std11C/"
    
    elif subjectindex == "3":
        result = firebaseref.get(standard1+"materiallink/"+eco,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'materiallink/'+eco+firstelementindex, data)
        firebaseref.put(standard1+'materiallink/'+eco+firstelementindex,'downloadlink',linkvar)
        firebaseref.put(standard1+'materiallink/'+eco+firstelementindex,'name',namevar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'materiallink/'+eco+firstelementindex, stringdelete)  
        standard1 = "/std11C/"