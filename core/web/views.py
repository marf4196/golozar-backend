from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def login_view(request, *args, **kwargs):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request,user)
            return JsonResponse({'login':'okay'})
        return JsonResponse({'login', 'fail'})

    else:
        return HttpResponse('else1')

def tasks_view(request, *args, **kwargs):
    if request.POST:
        pass
    else:
        raise PermissionError

def tooth_view(request, *args, **kwargs):
    if request.POST:
        pass
    else:
        raise PermissionError 