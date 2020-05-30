from django.http import HttpResponse,JsonResponse
from .crawler import infocrawler

# Create your views here.
def helloworld(request):
    return HttpResponse('Hello World!')
def crawler(request):
    if request.method == "GET":
        code = 200
        content = infocrawler(int(request.GET.get("num")))
        return JsonResponse({'code':code,'content':content})