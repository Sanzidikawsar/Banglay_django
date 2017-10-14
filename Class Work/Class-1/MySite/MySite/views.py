from django.http import request,HttpResponse

def hello(request):
    return  HttpResponse("Hellow World!")
# <html>
#     <p>Hi there..</p>
# </html>