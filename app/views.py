from django.http import HttpResponse,JsonResponse


# Create your views here.
def helloworld(request):
    return HttpResponse('Hello World!')
def crawler(request):
    if request.method == "GET":
        code = 200
        content = {}
        return JsonResponse({'code':code,'content':content})