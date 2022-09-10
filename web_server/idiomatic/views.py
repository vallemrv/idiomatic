from tokenapi.http import JsonResponse, JsonError
from django.contrib.auth.admin import User
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt

def crear_leccion(request):
    return JsonResponse({})


@csrf_exempt
def is_username_free(request):
    print(request.method)
    if request.method == "POST":
        user = User.objects.filter(username=request.POST["username"]).first()
        if user:
            return JsonError("El usuario esta en uso")
        else:
            return JsonResponse() 
    else:
        return JsonError("Solo peticiones post")

@csrf_exempt
def registrarse(request):
    if request.method == "POST":
        user = User.objects.filter(username=request.POST["username"]).first()
        if user:
            return JsonError("El usuario esta en uso")
        else:
            user = User()
            user.username =   request.POST["username"]
            user.first_name = request.POST["nombre"]
            user.last_name = request.POST["apellido"]  
            user.email = request.POST["email"]  
            user.password = make_password(request.POST["password"] )
            user.is_staff = False  
            user.is_superuser = False
            user.save()
            return JsonResponse({"alert":"Usuario creado con exito"}) 
    else:
        return JsonError("Solo peticiones post")