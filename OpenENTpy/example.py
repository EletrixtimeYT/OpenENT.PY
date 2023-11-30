from OpenENTpy import openent as ent


ent.init("URL","oneSessionId","XSRF TOKEN")
user = ent.getuser_json("UUID") #Get user info a json
print(user)

pp = ent.getuser_profilepicture("UUID") #Get user profile picture
print(pp)
print(ent.message_send("TO UUID","Bot","<div class=\"ng-scope\">OpenENT.Py Fonctionelle !<br></div><div class=\"signature new-signature ng-scope\"></div>")) #Send message
print(ent.class_get_user_list()) #Get user list
print(ent.message_getjson(page=0,unread=False)) #Get messages list in json