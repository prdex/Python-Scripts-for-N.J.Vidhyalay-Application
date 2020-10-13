from firebase import firebase
from datetime import date
import sys
from firebase import firebase


firebaseref = firebase.FirebaseApplication("https://njvidhyalay-4f0ea.firebaseio.com")

english = "%E0%AA%85%E0%AA%82%E0%AA%97%E0%AB%8D%E0%AA%B0%E0%AB%87%E0%AA%9C%E0%AB%80/"
maths = "%E0%AA%97%E0%AA%A3%E0%AA%BF%E0%AA%A4/"
gujarati = "%E0%AA%97%E0%AB%81%E0%AA%9C%E0%AA%B0%E0%AA%BE%E0%AA%A4%E0%AB%80/"
science = "%E0%AA%B5%E0%AA%BF%E0%AA%9C%E0%AB%8D%E0%AA%9E%E0%AA%BE%E0%AA%A8/"
social = "%E0%AA%B8%E0%AA%BE%E0%AA%AE%E0%AA%BE%E0%AA%9C%E0%AA%BF%E0%AA%95%20%E0%AA%B5%E0%AA%BF%E0%AA%9C%E0%AB%8D%E0%AA%9E%E0%AA%BE%E0%AA%A8/"


today = date.today()
d1 = today.strftime("%d/%m/%Y")

statusvar = "333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333"
subjectvar = "testsubject"

data = {
    'date':d1,
    'status':statusvar,
    'subject':subjectvar
}

standard1 = "/std10A/"
print("Enter subject code")
subjectindex = input().strip()


for x in range(2):
    if subjectindex == "1":
        result = firebaseref.get(standard1+"assignmentsubject/"+english,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'assignmentsubject/'+english+firstelementindex, data)
        firebaseref.put(standard1+'assignmentsubject/'+english+firstelementindex,'date',d1)
        firebaseref.put(standard1+'assignmentsubject/'+english+firstelementindex,'status',statusvar)
        firebaseref.put(standard1+'assignmentsubject/'+english+firstelementindex,'subject',subjectvar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'assignmentsubject/'+english+firstelementindex, stringdelete)  
        standard1 = "/std10B/"
        
    elif subjectindex == "2":
        result = firebaseref.get(standard1+"assignmentsubject/"+maths,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'assignmentsubject/'+maths+firstelementindex, data)
        firebaseref.put(standard1+'assignmentsubject/'+maths+firstelementindex,'date',d1)
        firebaseref.put(standard1+'assignmentsubject/'+maths+firstelementindex,'status',statusvar)
        firebaseref.put(standard1+'assignmentsubject/'+maths+firstelementindex,'subject',subjectvar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'assignmentsubject/'+maths+firstelementindex, stringdelete)  
        standard1 = "/std10B/"
    
    elif subjectindex == "3":
        result = firebaseref.get(standard1+"assignmentsubject/"+gujarati,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'assignmentsubject/'+gujarati+firstelementindex, data)
        firebaseref.put(standard1+'assignmentsubject/'+gujarati+firstelementindex,'date',d1)
        firebaseref.put(standard1+'assignmentsubject/'+gujarati+firstelementindex,'status',statusvar)
        firebaseref.put(standard1+'assignmentsubject/'+gujarati+firstelementindex,'subject',subjectvar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'assignmentsubject/'+gujarati+firstelementindex, stringdelete)  
        standard1 = "/std10B/"
    
    elif subjectindex == "4":
        result = firebaseref.get(standard1+"assignmentsubject/"+science,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'assignmentsubject/'+science+firstelementindex, data)
        firebaseref.put(standard1+'assignmentsubject/'+science+firstelementindex,'date',d1)
        firebaseref.put(standard1+'assignmentsubject/'+science+firstelementindex,'status',statusvar)
        firebaseref.put(standard1+'assignmentsubject/'+science+firstelementindex,'subject',subjectvar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'assignmentsubject/'+science+firstelementindex, stringdelete)  
        standard1 = "/std10B/"
    
    elif subjectindex == "5":
        result = firebaseref.get(standard1+"assignmentsubject/"+social,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'assignmentsubject/'+social+firstelementindex, data)
        firebaseref.put(standard1+'assignmentsubject/'+social+firstelementindex,'date',d1)
        firebaseref.put(standard1+'assignmentsubject/'+social+firstelementindex,'status',statusvar)
        firebaseref.put(standard1+'assignmentsubject/'+social+firstelementindex,'subject',subjectvar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'assignmentsubject/'+social+firstelementindex, stringdelete)  
        standard1 = "/std10B/"

