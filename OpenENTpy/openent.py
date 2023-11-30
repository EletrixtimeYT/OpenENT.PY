#================================
#         OPEN-ENT.PY
#================================
# 2023 EletrixTime


# Importing normal libraires

import requests
import json

# Importing builded in libs
from OpenENTpy import vars


main_url = ""
init = False
cookies = {}

def init(url,token,xsrf_token):
    global main_url
    global init
    global cookies
    global h
   
    cookies = {'oneSessionId': token,'authenficated': 'true','XSRF-TOKEN':xsrf_token}
    main_url = url
    csrftoken = {xsrf_token}
    init = True
    #r = requests.get(f"{url}/timeline/conf/public",cookies=cookies)

    
def getuser_json(uuid):
    if init:
        try:
            r = requests.get(f"{main_url}/directory/userbook/{uuid}",cookies=cookies)
            if r.text == vars.LOGIN_PAGE:
                return("NO_AUTHENFICATED")
            else:
                return(r.text)
            

        except Exception as e:
            print(f"[OpenENT/Main_ERROR] : {e} ")
            return("ExceptionOccured")

    else:
        raise("NO_INIT")
        
    
def getuser_profilepicture(uuid):
    if init:
        djson = getuser_json(uuid=uuid)
        if djson == "NO_AUTHENFICATED":
            return("NO_AUTHENFICATED")
        else:
            y = json.loads(str(djson))
            pp = y['picture']
            final = f"{main_url}{pp}"
            return(final)
    else:
        raise("NO_INIT")
def class_get_user_list():
    if init:
        x = requests.get(f"{main_url}/userbook/search/criteria?getClassesMonoStructureOnly=true",cookies=cookies)
        if requests.status_codes == '403': 
            return("NO_AUTHENFICATED")
        else:
            return x.text
    else:
        raise("NO_INIT")
def message_send(to,subject,body):
    if init:
        headers = {'X-XSRF-TOKEN': cookies['XSRF-TOKEN']}
        
        r = requests.post(
            f'{main_url}/conversation/send#/inbox',
            json={"body": body, "cc": [], "cci": [], "subject": subject, "to": [to]},
            cookies=cookies,
            headers=headers 
        )

        if r.status_code == '403':
            return(r.text)
        else:
            return(r.text)
    else:   
        raise("NO_INIT")

def message_getjson(page,unread):
    if init:
        x = requests.get(f"{main_url}/conversation/list/inbox?page={page}&unread={unread}",cookies=cookies)
        return x.text
    else:
        raise("NO_INIT")

