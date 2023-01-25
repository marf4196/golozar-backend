from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from web.models import Tasks, Teeth

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
        raise PermissionError
@csrf_exempt
def tasks_view(request, *args, **kwargs):
    if request.POST:
        if not request.user.is_anonymous:
            user = request.user
            
            qs = Tasks.objects.filter(owner=user)
            return JsonResponse({'objects':qs})
        else:
            return JsonResponse({'user': 'anonymouse'}, status = 403)

    else:
        print('hey')
        raise PermissionError

def tooth_view(request, *args, **kwargs):
    if request.POST:
        pass
    else:
        raise PermissionError 