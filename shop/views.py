# Create your views here.
from django.shortcuts import render, redirect
from shop.models import Product
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/home')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})


def home(request):

    # products = [{"name": "Vanilla", "price": 5.00},
    #            {"name": "Strawberry", "price": 6.00},
    #             {"name": "Chocolate", "price": 7.00},
    #             {"name": "Mint", "price": 8.00},
    #             {"name": "Pistachio", "price": 9.00},
    #             {"name": "Lemon", "price": 10.00},
    #             {"name": "Tiramisu", "price": 11.00},
    #             {"name": "Peach", "price": 12.00}]

    products = Product.objects.all()

    contextdata = {"sitename": "My IMC ice cream shop",
                   "slogan": "Where ice cream tastes like Italy",
                   "products": products,}

    if request.method == "POST":
        item = request.POST.get("item")
        p = Product.objects.get(id=item)
        qty = request.POST.get("qty")
        if item:
            confirmation_message = {"msg": "You are buying " + str(p) + " and the quantity is " + qty}
            return render(
                request, "shop/confirmation.html", context = confirmation_message)

    return render(request,"shop/index.html", context = contextdata)

def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save() # save the user
        return redirect('/')
    else:
        form = UserCreationForm()
        return render(request, 'shop/register.html', {'form': form})