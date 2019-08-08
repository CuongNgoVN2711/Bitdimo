from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .  import serializers, models

def Login(request, username, password):
    if request.method == 'GET':
        if models.User.objects.filter(username = username).count() < 1:
            json = [{'Status':'WU'}]
            return HttpResponse(JSONRenderer().render(json))
        else:
            if models.User.objects.filter(password = password).count() < 1:
                json = [{'Status':'RUWP'}]
                return HttpResponse(JSONRenderer().render(json))
            else:
                user = models.User.objects.filter(username = username, password = password)
                serializer =  serializers.UserSerializer(user, many = True)
                json = [{'Status':'RURP','CurrentUser':serializer.data}]
                return HttpResponse(JSONRenderer().render(json))

def CreateUser(request):
    if request.method == 'POST':
        user = JSONParser().parse(request)
        serializer = serializers.UserSerializer(data = user)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render([{'Status':'Create Success'}]))
        else:
            if models.User.objects.filter(username = user['username']).count() >= 1:
                return HttpResponse(JSONRenderer().render([{'Status':'Username already exist'}]))
            elif models.User.objects.filter(email = user['email']).count() >= 1:
                return HttpResponse(JSONRenderer().render([{'Status':'Email already exist'}]))
            else:
                return HttpResponse(JSONRenderer().render([{'Status':'Unknown'}]))

def  ListUserPost(request, param):
    if request.method == 'GET':
        userpost = models.UserPost.objects.all().order_by(param)
        serializer = serializers.UserPostSerializer(userpost , many =True)
        return HttpResponse(JSONRenderer().render(serializer.data))      
""" 
def CreatePost(request):
    if request.method == 'POST':
        data = {
                'user': request.POST.get('user_id'),
                'area': request.POST.get('area_id'),
                'content': request.POST.get('content'),
                'address': request.POST.get('address'),
                'latitude': request.POST.get('latitude'),
                'longtitude': request.POST.get('longtitude')
            }
        images = {
            'user': request.POST.get('user_id'),
            'images': request.POST.getlist('images[]')
            }
        serializer1 =serializers.UserPostSerializer(data = images)
        if serializer1.is_valid():
            serializer1.save()
            return HttpResponse(JSONRenderer().render([{'Status':'Create Success'}]))
        else:
            return HttpResponse(JSONRenderer().render(serializer1.errors))
        serializer = serializers.UserPostSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(JSONRenderer().render([{'Status':'Create Success'}]))
        else:
            return HttpResponse(JSONRenderer().render(serializer.errors))
 """
 
def  ListAdminPost(request, param):
    if request.method == 'GET':
        adminpost = models.AdminPost.objects.all().order_by(param)
        serializer = serializers.AdminPostSerializer(adminpost , many =True)
        return HttpResponse(JSONRenderer().render(serializer.data))

def DetailAdminPost(request, id):
    if request.method == 'GET':
        admin_post = models.AdminPost.objects.filter(id = id)
        serializer = serializers.DetailAdminPostSerializer(admin_post, many = True)
        return HttpResponse(JSONRenderer().render(serializer.data))      
