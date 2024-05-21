from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>My First Webshop Hello!</h1> <h2>This is fun</h2> <h3>Let's do this</h3>")
