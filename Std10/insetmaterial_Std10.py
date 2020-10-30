from firebase import firebase
firebaseref = firebase.FirebaseApplication("https://njvidhyalay-4f0ea.firebaseio.com")

english = "%E0%AA%85%E0%AA%82%E0%AA%97%E0%AB%8D%E0%AA%B0%E0%AB%87%E0%AA%9C%E0%AB%80/"
maths = "%E0%AA%97%E0%AA%A3%E0%AA%BF%E0%AA%A4/"
gujarati = "%E0%AA%97%E0%AB%81%E0%AA%9C%E0%AA%B0%E0%AA%BE%E0%AA%A4%E0%AB%80/"
science = "%E0%AA%B5%E0%AA%BF%E0%AA%9C%E0%AB%8D%E0%AA%9E%E0%AA%BE%E0%AA%A8/"
scoial = "%E0%AA%B8%E0%AA%BE%E0%AA%AE%E0%AA%BE%E0%AA%9C%E0%AA%BF%E0%AA%95%20%E0%AA%B5%E0%AA%BF%E0%AA%9C%E0%AB%8D%E0%AA%9E%E0%AA%BE%E0%AA%A8/"

linkvar  = "https://drive.google.com/uc?id=1EWOZY-5Gmj46QEY82OLEOMu1sTgiTqXI&export=download"
namevar = "સમાજ પ્રકરણ-૨"

data = {
    'downloadlink':linkvar,
    'name':namevar
}
standard1 = "/std10A/"
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
        firebaseref.put(standard1+'materiallink/'+english+firstelementindex,'downloadlink', linkvar)
        firebaseref.put(standard1+'materiallink/'+english+firstelementindex,'name',namevar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'materiallink/'+english+firstelementindex, stringdelete)  
        standard1 = "/std10B/"
        
    elif subjectindex == "2":
        result = firebaseref.get(standard1+"materiallink/"+maths,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'materiallink/'+maths+firstelementindex, data)
        firebaseref.put(standard1+'materiallink/'+maths+firstelementindex,'downloadlink', linkvar)
        firebaseref.put(standard1+'materiallink/'+maths+firstelementindex,'name',namevar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'materiallink/'+maths+firstelementindex, stringdelete)  
        standard1 = "/std10B/"
    
    elif subjectindex == "3":
        result = firebaseref.get(standard1+"materiallink/"+gujarati,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'materiallink/'+gujarati+firstelementindex, data)
        firebaseref.put(standard1+'materiallink/'+gujarati+firstelementindex,'downloadlink', linkvar)
        firebaseref.put(standard1+'materiallink/'+gujarati+firstelementindex,'name',namevar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'materiallink/'+gujarati+firstelementindex, stringdelete)  
        standard1 = "/std10B/"
    
    elif subjectindex == "4":
        result = firebaseref.get(standard1+"materiallink/"+science,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'materiallink/'+science+firstelementindex, data)
        firebaseref.put(standard1+'materiallink/'+science+firstelementindex,'downloadlink', linkvar)
        firebaseref.put(standard1+'materiallink/'+science+firstelementindex,'name',namevar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'materiallink/'+science+firstelementindex, stringdelete)  
        standard1 = "/std10B/"
    
    elif subjectindex == "5":
        result = firebaseref.get(standard1+"materiallink/"+scoial,'')
        dict_items = result.items()
        firstelement = list(dict_items)[:1]
        firstelementindex = int(firstelement[0][0])-1
        firstelementindex = str(firstelementindex)
        result = firebaseref.post(standard1+'materiallink/'+scoial+firstelementindex, data)
        firebaseref.put(standard1+'materiallink/'+scoial+firstelementindex,'downloadlink', linkvar)
        firebaseref.put(standard1+'materiallink/'+scoial+firstelementindex,'name',namevar)
        stringdelete = result["name"]
        firebaseref.delete(standard1+'materiallink/'+scoial+firstelementindex, stringdelete)  
        standard1 = "/std10B/"

