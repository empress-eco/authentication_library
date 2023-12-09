import requests
import json
import frappe
import json
import base64
from werkzeug.wrappers import Response
from frappe.utils.password import update_password as _update_password
from frappe.utils import now
import random
from frappe.core.doctype.user.user import User
from frappe.utils import get_url
from frappe.utils import (
	now_datetime
)

error='Authentication required. Please provide valid credentials..'

@frappe.whitelist(allow_guest=True)
def getToken2(self):
    pass


@frappe.whitelist(allow_guest=True)
def test_api():
    return "test api success"


@frappe.whitelist(allow_guest=True)
def generate_token_secure( api_key, api_secret, app_key):
    try:
        try:
            app_key = base64.b64decode(app_key).decode("utf-8")
        except Exception as e:
            return Response(json.dumps({"message": "Security Parameters are not valid" , "user_count": 0}), status=401, mimetype='application/json')
        clientID, clientSecret, clientUser = frappe.db.get_value('OAuth Client', {'app_name': app_key}, ['client_id', 'client_secret','user'])
        
        if clientID is None:
            # return app_key
            return Response(json.dumps({"message": "Security Parameters are not valid" , "user_count": 0}), status=401, mimetype='application/json')
        
        client_id = clientID  # Replace with your OAuth client ID
        client_secret = clientSecret  # Replace with your OAuth client secret
        url =  frappe.local.conf.host_name  + "/api/method/frappe.integrations.oauth2.get_token"
        payload = {
            "username": api_key,
            "password": api_secret,
            "grant_type": "password",
            "client_id": client_id,
            "client_secret": client_secret,
            # "grant_type": "refresh_token"
        }
        files = []
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", url, data=payload, files=files)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            frappe.local.response.http_status_code = 401
            return json.loads(response.text)
            
    except Exception as e:
            # frappe.local.response.http_status_code = 401
            # return json.loads(response.text)
            return Response(json.dumps({"message": e , "user_count": 0}), status=500, mimetype='application/json')

@frappe.whitelist(allow_guest=True)
def generate_custom_token(username, password):  #Used for development testing only. not for production
    
    #this function can be used for development testing only. not for production. Uncomment the below code to use it.
    return Response(json.dumps({"message": "Can not be used for production environmet" , "user_count": 0}), status=500, mimetype='application/json')
    #------------
    
    try:
        clientID, clientSecret, clientUser = frappe.db.get_value('OAuth Client', {'app_name': 'MobileAPP'}, ['client_id', 'client_secret','user'])
        client_id = clientID  # Replace with your OAuth client ID
        client_secret = clientSecret  # Replace with your OAuth client secret
        url =  frappe.local.conf.host_name  + "/api/method/employee_app.gauth.get_token"
        payload = {
            "username": username,
            "password": password,
            "grant_type": "password",
            "client_id": client_id,
            "client_secret": client_secret,
        }
        files = []
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", url, data=payload, files=files)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            frappe.local.response.http_status_code = 401
            return json.loads(response.text)
            
    except Exception as e:
            frappe.local.response.http_status_code = 401
            return json.loads(response.text)
            
@frappe.whitelist(allow_guest=True)
def generate_custom_token_for_employee( password):
    try:
        clientID, clientSecret, clientUser = frappe.db.get_value('OAuth Client', {'app_name': 'MobileAPP'}, ['client_id', 'client_secret','user'])
        username = clientUser
       
        client_id = clientID  # Replace with your OAuth client ID
        client_secret = clientSecret  # Replace with your OAuth client secret
        url =  frappe.local.conf.host_name  + "/api/method/employee_app.gauth.get_token"
        payload = {
            # "username": username,
            "username": clientUser,
            "password": password,
            "grant_type": "password",
            "client_id": client_id,
            "client_secret": client_secret,
        }
        files = []
        headers = {"Content-Type": "application/json"}
        response = requests.request("POST", url, data=payload, files=files)
        # return json.loads(response.text)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            frappe.local.response.http_status_code = 401
            return json.loads(response.text)
        
    except Exception as e:
     
        frappe.local.response.http_status_code = 401
        return json.loads(response.text)

@frappe.whitelist(allow_guest=True)
def whoami():
        try:
            return frappe.session.user
        except Exception as e:
             frappe.throw(error)

@frappe.whitelist()
def get_user_name(user_email = None, mobile_phone = None):
    if mobile_phone is not None:
        user_details = frappe.get_list('User', filters={'mobile_no': mobile_phone}, fields=["name", "enabled"] )
    elif user_email is not None:
        user_details = frappe.get_list('User', filters={'email': user_email}, fields=["name", "enabled"] )
    else:
        return  Response(json.dumps({"message": "User not found" , "user_count": 0}), status=404, mimetype='application/json')
    
    if len(user_details) >=1:
        return  user_details
    else:
        return  Response(json.dumps({"message": "User not found" , "user_count": 0}), status=404, mimetype='application/json')
             
@frappe.whitelist()
def is_user_available(user_email = None, mobile_phone = None):
        # response = Response()
        try:
            if mobile_phone is not None:
                mobile_count = len(frappe.get_all('User', {'mobile_no': mobile_phone}))
            else:
                mobile_count = 0
                
            if user_email is not None:
                email_count = len(frappe.get_all('User', {'email': user_email}))
            else:
                email_count = 0
                
            if mobile_count >= 1 and email_count < 1:
                response = {"message": "Mobile exists", "user_count": mobile_count}
                status_code = 200
            if email_count >= 1 and mobile_count < 1:
                response = {"message": "Email exists", "user_count": email_count}
                status_code = 200
            if mobile_count >= 1 and email_count >= 1:
                response = {"message": "Mobile and Email exists", "user_count": mobile_count}
                status_code = 200
            if mobile_count < 1 and email_count < 1:
                response = {"message": "Mobile and Email does not exist", "user_count": 0}
                status_code = 404
            return Response(json.dumps(response), status=status_code, mimetype='application/json')

        except Exception as e:
                return  Response(json.dumps({"message": e , "user_count": 0}), status=500, mimetype='application/json')
            

@frappe.whitelist()
def g_create_user(full_name, password, mobile_no, email,role=None):
    
    user_exists = get_user_name(user_email=email, mobile_phone=mobile_no)
    return  Response(json.dumps({"message": user_exists , "user_count": 0}), status=500, mimetype='application/json')
    
    try:
        frappe.get_doc({"doctype":"User",
                        "name":email,
                        "first_name":full_name,
                        "mobile_no":mobile_no,
                        "email": email,
                        "roles": [{"role": role}]
                        }).insert()
        
        return g_generate_reset_password_key(email, send_email=False, password_expired=False)

        # return  Response(json.dumps({"message": "User successfully created" , "user_count": 1}), status=200, mimetype='application/json')
        
    except Exception as e:
        return  Response(json.dumps({"message": e , "user_count": 0}), status=500, mimetype='application/json')
    

@frappe.whitelist()
def g_update_password(username, password):
    try:
        if(len(frappe.get_all('User', {'name': username}))<1):
            return  Response(json.dumps({"message": "User not found" , "user_count": 0}), status=404, mimetype='application/json')    
        
        _update_password(username, password, logout_all_sessions=True)
        # frappe.db.commit()
        return  Response(json.dumps({"message": "Password successfully updated" , "user_count": 1}), status=200, mimetype='application/json')
        
    except Exception as e:
        return  Response(json.dumps({"message": e , "user_count": 0}), status=500, mimetype='application/json')
    
@frappe.whitelist()
def g_generate_reset_password_key(user, send_email=False, password_expired=False):
    try:
        key  = str(random.randint(100000, 999999))
        doc2 = frappe.get_doc("User", user)
        doc2.reset_password_key = key
        doc2.last_reset_password_key_generated_on = now_datetime()
        doc2.save()
        
        url = "/update-password?key=" + key
        if password_expired:
            url = "/update-password?key=" + key + "&password_expired=true"

        link = get_url(url)
        if send_email:
            User.password_reset_mail(link)

        return   Response(json.dumps({"reset_key": key , "generated_time": str(now_datetime()), "URL": link }), status=200, mimetype='application/json')
    except Exception as e:
        return  Response(json.dumps({"message": e , "user_count": 0}), status=500, mimetype='application/json')

@frappe.whitelist()
def g_delete_user(username, email, mobile_no):
    try:
        if(len(frappe.get_all('User', {"name":username, "email": email, "mobile_no": mobile_no}))<1):
            return  Response(json.dumps({"message": "User not found" , "user_count": 0}), status=404, mimetype='application/json')    
        
        frappe.db.delete("User", {"name":username, "email": email, "mobile_no": mobile_no}),
        return  Response(json.dumps({"message": "User successfully deleted" , "user_count": 1}), status=200, mimetype='application/json')
        
    except Exception as e:
        return  Response(json.dumps({"message": e , "user_count": 0}), status=500, mimetype='application/json')


@frappe.whitelist()
def g_user_enable(username, email, mobile_no, enable_user: bool = True):
    try:
        if(len(frappe.get_all('User', {"name":username, "email": email, "mobile_no": mobile_no}))<1):
            return  Response(json.dumps({"message": "User not found" , "user_count": 0}), status=404, mimetype='application/json')    

        frappe.db.set_value('User', username, 'enabled', enable_user)
        return  Response(json.dumps({"message": f"User successfully {'enabled' if enable_user else 'disabled'} " , "user_count": 1}), status=200, mimetype='application/json')
       
    except Exception as e:
        return  Response(json.dumps({"message": e , "user_count": 0}), status=500, mimetype='application/json')

 