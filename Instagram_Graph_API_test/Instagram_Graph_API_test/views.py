from django.http import HttpResponse

def facebook_callback(request):
    # Aqui você pode processar a resposta do Facebook
    return HttpResponse("Callback do Facebook funcionando!")