from django.http import HttpRequest
from django.forms.models import model_to_dict
from polls.service.user import UserService
from polls.utils.responser import Responser
import json

# @csrf_exempt
def get_user(request: HttpRequest):
    if request.method == "GET":
        getAllUser = UserService().getAllUser()
        # qs_json = serializers.serialize('json', getAllUser)
        return Responser().Success([i for i in getAllUser],"ok", 200)
    else:
        return Responser().Failed("","Unknown Method", 405)
    
def get_specific_user(request:HttpRequest, name:str):
    if request.method == "GET":
        getUser = UserService().getSpecificUser(name=name)
        if(getUser):
            return Responser().Success(model_to_dict(getUser),"ok", 200)
        return Responser().Failed("","Cannot Find User", 404)
    else:
        return Responser().Failed("","Unknown Method", 405)
    
    

def create_user(request: HttpRequest):
    if request.method == "POST":
        data = json.loads(request.body)
        addUsr = UserService().insertUser(data['name'])
        if(addUsr):
            return Responser().Success([],"ok", 200)
        return Responser().Failed("","Unprocessable Entity", 422)
    else:
        return Responser().Failed("","Unknown Method", 405)
    
def update_user(request:HttpRequest):
    if request.method == "POST":
        data = json.loads(request.body)
        updateUser = UserService().updateUser(data['id'], name=data['name'])
        if(updateUser):
            return Responser().Success([],"ok", 200)
        return Responser().Failed("","Unprocessable Entity", 422)
    else:
        return Responser().Failed("","Unknown Method", 405)
