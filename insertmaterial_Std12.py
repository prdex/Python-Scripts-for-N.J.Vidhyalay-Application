from firebase import firebase
firebaseref = firebase.FirebaseApplication("https://njvidhyalay-4f0ea.firebaseio.com")

#english - %E0%AA%85%E0%AA%82%E0%AA%97%E0%AB%8D%E0%AA%B0%E0%AB%87%E0%AA%9C%E0%AB%80
#Maths - %E0%AA%97%E0%AA%A3%E0%AA%BF%E0%AA%A4
#Gujarati - %E0%AA%97%E0%AB%81%E0%AA%9C%E0%AA%B0%E0%AA%BE%E0%AA%A4%E0%AB%80
#Science - %E0%AA%B5%E0%AA%BF%E0%AA%9C%E0%AB%8D%E0%AA%9E%E0%AA%BE%E0%AA%A8
#scoial - %E0%AA%B8%E0%AA%BE%E0%AA%AE%E0%AA%BE%E0%AA%9C%E0%AA%BF%E0%AA%95%20%E0%AA%B5%E0%AA%BF%E0%AA%9C%E0%AB%8D%E0%AA%9E%E0%AA%BE%E0%AA%A8


data = {
    'downloadlink':'link',
    'name':"name"
}

standard1 = "/std12A/"

for x in range(2):
    result = firebaseref.post(standard1+'materiallink/%E0%AA%B8%E0%AA%82%E0%AA%B8%E0%AB%8D%E0%AA%95%E0%AB%83%E0%AA%A4/99', data)
    firebaseref.put(standard1+'materiallink/%E0%AA%B8%E0%AA%82%E0%AA%B8%E0%AB%8D%E0%AA%95%E0%AB%83%E0%AA%A4/99','date','34354')
    firebaseref.put(standard1+'materiallink/%E0%AA%B8%E0%AA%82%E0%AA%B8%E0%AB%8D%E0%AA%95%E0%AB%83%E0%AA%A4/99','subject','મટિરિયલ માં ટિક કરવેલા પ્રશ્નો ૧ વાર')
    firebaseref.put(standard1+'materiallink/%E0%AA%B8%E0%AA%82%E0%AA%B8%E0%AB%8D%E0%AA%95%E0%AB%83%E0%AA%A4/99','status','33333333333333333333333333333333333333333333333333333333333')
    stringdelete = result["name"]
    firebaseref.delete(standard1+'materiallink/%E0%AA%B8%E0%AA%82%E0%AA%B8%E0%AB%8D%E0%AA%95%E0%AB%83%E0%AA%A4/99/', stringdelete)  
    standard1 = "/std12C/"
