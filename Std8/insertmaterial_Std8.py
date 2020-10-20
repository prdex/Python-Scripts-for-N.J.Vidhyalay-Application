from firebase import firebase
from firebase import firebase
from datetime import date
import sys

firebaseref = firebase.FirebaseApplication("https://njvidhyalay-4f0ea.firebaseio.com")

english  = "%E0%AA%85%E0%AA%82%E0%AA%97%E0%AB%8D%E0%AA%B0%E0%AB%87%E0%AA%9C%E0%AB%80/"
maths    = "%E0%AA%97%E0%AA%A3%E0%AA%BF%E0%AA%A4/"
gujarati = "%E0%AA%97%E0%AB%81%E0%AA%9C%E0%AA%B0%E0%AA%BE%E0%AA%A4%E0%AB%80/"
science  = "%E0%AA%B5%E0%AA%BF%E0%AA%9C%E0%AB%8D%E0%AA%9E%E0%AA%BE%E0%AA%A8/"
social   = "%E0%AA%B8%E0%AA%BE%E0%AA%AE%E0%AA%BE%E0%AA%9C%E0%AA%BF%E0%AA%95%20%E0%AA%B5%E0%AA%BF%E0%AA%9C%E0%AB%8D%E0%AA%9E%E0%AA%BE%E0%AA%A8/"
sanskrit = "%E0%AA%B8%E0%AA%82%E0%AA%B8%E0%AB%8D%E0%AA%95%E0%AB%83%E0%AA%A4/"
hindi    = "%E0%AA%B9%E0%AA%BF%E0%AA%A8%E0%AB%8D%E0%AA%A6%E0%AB%80"

today = date.today()
d1 = today.strftime("%d/%m/%Y")

statusvar = "333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333"
subjectvar = "પાઠ-૧૦ શબ્દાર્થ ૨ વાર અને ફકરા માંથી ૧૦ પ્રશ્નો"

data = {
    'date':d1,
    'status':statusvar,
    'subject':subjectvar
}
standard1 = "/std8/"

print("Enter subject code")
subjectindex = input().strip()

if subjectindex == "1":
    result = firebaseref.get(standard1+"materiallink/"+english,'')
    dict_items = result.items()
    firstelement = list(dict_items)[:1]
    firstelementindex = int(firstelement[0][0])-1
    firstelementindex = str(firstelementindex)
    result = firebaseref.post(standard1+'materiallink/'+english+firstelementindex, data)
    firebaseref.put(standard1+'materiallink/'+english+firstelementindex,'date',d1)
    firebaseref.put(standard1+'materiallink/'+english+firstelementindex,'status',statusvar)
    firebaseref.put(standard1+'materiallink/'+english+firstelementindex,'subject',subjectvar)
    stringdelete = result["name"]
    firebaseref.delete(standard1+'materiallink/'+english+firstelementindex, stringdelete)  

elif subjectindex == "2":
    result = firebaseref.get(standard1+"materiallink/"+maths,'')
    dict_items = result.items()
    firstelement = list(dict_items)[:1]
    firstelementindex = int(firstelement[0][0])-1
    firstelementindex = str(firstelementindex)
    result = firebaseref.post(standard1+'materiallink/'+maths+firstelementindex, data)
    firebaseref.put(standard1+'materiallink/'+maths+firstelementindex,'date',d1)
    firebaseref.put(standard1+'materiallink/'+maths+firstelementindex,'status',statusvar)
    firebaseref.put(standard1+'materiallink/'+maths+firstelementindex,'subject',subjectvar)
    stringdelete = result["name"]
    firebaseref.delete(standard1+'materiallink/'+maths+firstelementindex, stringdelete)  
        

elif subjectindex == "3":
    result = firebaseref.get(standard1+"materiallink/"+gujarati,'')
    dict_items = result.items()
    firstelement = list(dict_items)[:1]
    firstelementindex = int(firstelement[0][0])-1
    firstelementindex = str(firstelementindex)
    result = firebaseref.post(standard1+'materiallink/'+gujarati+firstelementindex, data)
    firebaseref.put(standard1+'materiallink/'+gujarati+firstelementindex,'date',d1)
    firebaseref.put(standard1+'materiallink/'+gujarati+firstelementindex,'status',statusvar)
    firebaseref.put(standard1+'materiallink/'+gujarati+firstelementindex,'subject',subjectvar)
    stringdelete = result["name"]
    firebaseref.delete(standard1+'materiallink/'+gujarati+firstelementindex, stringdelete)  
        
elif subjectindex == "4":
    result = firebaseref.get(standard1+"materiallink/"+science,'')
    dict_items = result.items()
    firstelement = list(dict_items)[:1]
    firstelementindex = int(firstelement[0][0])-1
    firstelementindex = str(firstelementindex)
    result = firebaseref.post(standard1+'materiallink/'+science+firstelementindex, data)
    firebaseref.put(standard1+'materiallink/'+science+firstelementindex,'date',d1)
    firebaseref.put(standard1+'materiallink/'+science+firstelementindex,'status',statusvar)
    firebaseref.put(standard1+'materiallink/'+science+firstelementindex,'subject',subjectvar)
    stringdelete = result["name"]
    firebaseref.delete(standard1+'materiallink/'+science+firstelementindex, stringdelete)  
    
    
elif subjectindex == "5":
    result = firebaseref.get(standard1+"materiallink/"+social,'')
    dict_items = result.items()
    firstelement = list(dict_items)[:1]
    firstelementindex = int(firstelement[0][0])-1
    firstelementindex = str(firstelementindex)
    result = firebaseref.post(standard1+'materiallink/'+social+firstelementindex, data)
    firebaseref.put(standard1+'materiallink/'+social+firstelementindex,'date',d1)
    firebaseref.put(standard1+'materiallink/'+social+firstelementindex,'status',statusvar)
    firebaseref.put(standard1+'materiallink/'+social+firstelementindex,'subject',subjectvar)
    stringdelete = result["name"]
    firebaseref.delete(standard1+'materiallink/'+social+firstelementindex, stringdelete)  
    
elif subjectindex == "6":
    result = firebaseref.get(standard1+"materiallink/"+sanskrit,'')
    dict_items = result.items()
    firstelement = list(dict_items)[:1]
    firstelementindex = int(firstelement[0][0])-1
    firstelementindex = str(firstelementindex)
    result = firebaseref.post(standard1+'materiallink/'+sanskrit+firstelementindex, data)
    firebaseref.put(standard1+'materiallink/'+sanskrit+firstelementindex,'date',d1)
    firebaseref.put(standard1+'materiallink/'+sanskrit+firstelementindex,'status',statusvar)
    firebaseref.put(standard1+'materiallink/'+sanskrit+firstelementindex,'subject',subjectvar)
    stringdelete = result["name"]
    firebaseref.delete(standard1+'materiallink/'+sanskrit+firstelementindex, stringdelete) 
    
elif subjectindex == "7":
    result = firebaseref.get(standard1+"materiallink/"+hindi,'')
    dict_items = result.items()
    firstelement = list(dict_items)[:1]
    firstelementindex = int(firstelement[0][0])-1
    firstelementindex = str(firstelementindex)
    result = firebaseref.post(standard1+'materiallink/'+hindi+firstelementindex, data)
    firebaseref.put(standard1+'materiallink/'+hindi+firstelementindex,'date',d1)
    firebaseref.put(standard1+'materiallink/'+hindi+firstelementindex,'status',statusvar)
    firebaseref.put(standard1+'materiallink/'+hindi+firstelementindex,'subject',subjectvar)
    stringdelete = result["name"]
    firebaseref.delete(standard1+'materiallink/'+hindi+firstelementindex, stringdelete) 
    
    
  