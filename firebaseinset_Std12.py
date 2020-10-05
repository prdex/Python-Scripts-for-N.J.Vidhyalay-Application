from firebase import firebase
firebaseref = firebase.FirebaseApplication("https://njvidhyalay-4f0ea.firebaseio.com")
data = {
    'date':'20/07/2020',
    'status':'33333333333333333333333333333333333333333333333333333333333',
    'subject':"મટિરિયલ માં ટિક કરવેલા પ્રશ્નો ૧ વાર"
}
result = firebaseref.post('std2/assignmentsubject/%E0%AA%B8%E0%AA%82%E0%AA%B8%E0%AB%8D%E0%AA%95%E0%AB%83%E0%AA%A4/99', data)
firebaseref.put('std2/assignmentsubject/%E0%AA%B8%E0%AA%82%E0%AA%B8%E0%AB%8D%E0%AA%95%E0%AB%83%E0%AA%A4/99','date','34354')
firebaseref.put('std2/assignmentsubject/%E0%AA%B8%E0%AA%82%E0%AA%B8%E0%AB%8D%E0%AA%95%E0%AB%83%E0%AA%A4/99','subject','મટિરિયલ માં ટિક કરવેલા પ્રશ્નો ૧ વાર')
firebaseref.put('std2/assignmentsubject/%E0%AA%B8%E0%AA%82%E0%AA%B8%E0%AB%8D%E0%AA%95%E0%AB%83%E0%AA%A4/99','status','33333333333333333333333333333333333333333333333333333333333')
stringdelete = result["name"]
firebaseref.delete('std2/assignmentsubject/%E0%AA%B8%E0%AA%82%E0%AA%B8%E0%AB%8D%E0%AA%95%E0%AB%83%E0%AA%A4/99/', stringdelete)  