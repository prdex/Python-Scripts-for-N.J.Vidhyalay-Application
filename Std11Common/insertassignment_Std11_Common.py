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

statusvar = "333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333"
subjectvar = "પાઠ-૬ સ્વાધ્યાય પ્ર.૧, પ્ર.૨, પ્ર.૩ (૧)"

data = {
    'date':d1,
    'status':statusvar,
    'subject':subjectvar
}
standard1 = "/std11A/"

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
        standard1 = "/std11C/"
    
    elif subjectindex == "2":
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
        standard1 = "/std11C/"
    
    elif subjectindex == "3":
        result = firebaseref.get(standard1+"assignmentsubject/"+eco,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'assignmentsubject/'+eco+firstelementindex, data)
        firebaseref.put(standard1+'assignmentsubject/'+eco+firstelementindex,'date',d1)
        firebaseref.put(standard1+'assignmentsubject/'+eco+firstelementindex,'status',statusvar)
        firebaseref.put(standard1+'assignmentsubject/'+eco+firstelementindex,'subject',subjectvar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'assignmentsubject/'+eco+firstelementindex, stringdelete)  
        standard1 = "/std11C/"