from django.http import JsonResponse

class Responser:
    def Success(self, datas:any, message:str, status:int = 200) -> JsonResponse:
        return JsonResponse({'message':message, "data": datas}, status=status)
    
    def Failed(self, datas:any, message:str, status:int = 400) -> JsonResponse:
        return JsonResponse({"message":message, "data": datas}, status=status)
    