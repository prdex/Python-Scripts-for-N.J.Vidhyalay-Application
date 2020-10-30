from firebase import firebase
from firebase import firebase
from datetime import date
import sys

firebaseref = firebase.FirebaseApplication("https://njvidhyalay-4f0ea.firebaseio.com")

english = "%E0%AA%85%E0%AA%82%E0%AA%97%E0%AB%8D%E0%AA%B0%E0%AB%87%E0%AA%9C%E0%AB%80/"
gujarati = "%E0%AA%97%E0%AB%81%E0%AA%9C%E0%AA%B0%E0%AA%BE%E0%AA%A4%E0%AB%80/"
eco     = "%E0%AA%85%E0%AA%B0%E0%AB%8D%E0%AA%A5%E0%AA%B6%E0%AA%BE%E0%AA%B8%E0%AB%8D%E0%AA%A4%E0%AB%8D%E0%AA%B0/"
tatva   = "%E0%AA%A4%E0%AA%A4%E0%AB%8D%E0%AA%B5%E0%AA%9C%E0%AB%8D%E0%AA%9E%E0%AA%BE%E0%AA%A8"
mano    = "%E0%AA%AE%E0%AA%A8%E0%AB%8B%E0%AA%B5%E0%AA%BF%E0%AA%9C%E0%AB%8D%E0%AA%9E%E0%AA%BE%E0%AA%A8"

datevar = "10/06/2020"
linkvar = "https://www.youtube.com/watch?v=Gj2PF2sJihY"
notevar = "પ્રકરણ-૪"
stdvar = "12"
subjectvar = "ગુજરાતી"


datalecture = {
    'date':datevar,
    'link':linkvar,
    'note':notevar,
    'std':stdvar,
    'subject':subjectvar
}
standard1 = "/std12A/"

print("Enter subject code")
subjectindex = input().strip()

if subjectindex == "1":
        result = firebaseref.get(standard1+"linkdetails/"+english,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'linkdetails/'+english+firstelementindex, datalecture)
        firebaseref.put(standard1+'linkdetails/'+english+firstelementindex,'date',datevar)
        firebaseref.put(standard1+'linkdetails/'+english+firstelementindex,'link',linkvar)
        firebaseref.put(standard1+'linkdetails/'+english+firstelementindex,'note',notevar)
        firebaseref.put(standard1+'linkdetails/'+english+firstelementindex,'std',stdvar)
        firebaseref.put(standard1+'linkdetails/'+english+firstelementindex,'subject',subjectvar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'linkdetails/'+english+firstelementindex, stringdelete)  

    
elif subjectindex == "2":
        result = firebaseref.get(standard1+"linkdetails/"+gujarati,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'linkdetails/'+gujarati+firstelementindex, datalecture)
        firebaseref.put(standard1+'linkdetails/'+gujarati+firstelementindex,'date',datevar)
        firebaseref.put(standard1+'linkdetails/'+gujarati+firstelementindex,'link',linkvar)
        firebaseref.put(standard1+'linkdetails/'+gujarati+firstelementindex,'note',notevar)
        firebaseref.put(standard1+'linkdetails/'+gujarati+firstelementindex,'std',stdvar)
        firebaseref.put(standard1+'linkdetails/'+gujarati+firstelementindex,'subject',subjectvar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'linkdetails/'+gujarati+firstelementindex, stringdelete)  
    
    
elif subjectindex == "3":
        result = firebaseref.get(standard1+"linkdetails/"+eco,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'linkdetails/'+eco+firstelementindex, datalecture)
        firebaseref.put(standard1+'linkdetails/'+eco+firstelementindex,'date',datevar)
        firebaseref.put(standard1+'linkdetails/'+eco+firstelementindex,'link',linkvar)
        firebaseref.put(standard1+'linkdetails/'+eco+firstelementindex,'note',notevar)
        firebaseref.put(standard1+'linkdetails/'+eco+firstelementindex,'std',stdvar)
        firebaseref.put(standard1+'linkdetails/'+eco+firstelementindex,'subject',subjectvar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'linkdetails/'+eco+firstelementindex, stringdelete)  
        