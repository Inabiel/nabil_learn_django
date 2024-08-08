from django.http import HttpRequest
from polls.service.user import UserService
from django.core import serializers
from polls.utils.responser import Responser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_user(request: HttpRequest):
    if request.method == "GET":
        getAllUser = UserService().getAllUser()
        # qs_json = serializers.serialize('json', getAllUser)
        return Responser().Success([i for i in getAllUser],"ok", 200)
    else:
        return Responser().Failed("","Unknown Method", 405)
    

def create_user(request):
    data = request.POST
