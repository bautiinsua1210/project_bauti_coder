from django.shortcuts import render
from .models import Client, Car, Service

from AppCoder.forms import ClientForm, CarForm, ServiceForm



def home(request):
    return render (request, "AppCoder/inicio.html")
def clients(request):
    return render (request, "AppCoder/client.html")
def cars(request):
    return render (request, "AppCoder/car.html")
def services(request):
    return render (request, "AppCoder/service.html")





#CLIENT#
def clientForm(request):
    if request.method=="POST":
        form= ClientForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            name= informacion["name"]
            surname= informacion["surname"]
            email= informacion["email"]
            role= informacion["role"]
            client= Client(name=name, surname=surname, email=email, role=role)
            client.save()
            clients=Client.objects.all()
            return render(request, "AppCoder/client.html" ,{"clients":clients, "message": "Client saved"})
        else:
            return render(request, "AppCoder/clientForm.html" ,{"form": form, "message": "Invalid data"})
        
    else:
        form= ClientForm()
        return render (request, "AppCoder/clientForm.html", {"form": form})


def readClient(request):
    clients=Client.objects.all()
    return render(request, "AppCoder/client.html", {"clients": clients})


def deleteClient(request, id):
    client=Client.objects.get(id=id)
    print(client)
    client.delete()
    clients=Client.objects.all()
    return render(request, "AppCoder/client.html", {"clients": clients, "message": "Client deleted"})


def clientEdit(request, id):
    client=Client.objects.get(id=id)
    if request.method=="POST":
        form= ClientForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            client.name=info["name"]
            client.surname=info["surname"]
            client.email=info["email"]
            client.role=info["role"]
            client.save()
            clients=Client.objects.all()
            return render(request, "AppCoder/client.html" ,{"clients":clients, "message": "Client edited"})
        pass
    else:
        form= ClientForm(initial={"name":client.name, "surname":client.surname, "email":client.email, "role":client.role})
        return render(request, "AppCoder/clientEdit.html", {"form": form, "client": client})



#CAR#

def carForm(request):
    if request.method=="POST":
        form= CarForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            brand= informacion["brand"]
            model= informacion["model"]
            year= informacion["year"]
            mile= informacion["mile"]
            car= Car(brand=brand, model=model, year=year, mile=mile)
            car.save()
            cars=Car.objects.all()
            return render(request, "AppCoder/car.html" ,{"cars":cars, "message": "Car saved"})
        else:
            return render(request, "AppCoder/clientForm.html" ,{"form": form, "message": "Invalid data"})
        
    else:
        form= CarForm()
        return render (request, "AppCoder/carForm.html", {"form": form})


def readCar(request):

    cars=Car.objects.all()
    return render(request, "AppCoder/car.html", {"cars": cars})

def deleteCar(request, id):
    car=Car.objects.get(id=id)
    print(car)
    car.delete()
    cars=Car.objects.all()
    return render(request, "AppCoder/car.html", {"cars": cars, "message": "Car deleted"})

def carEdit(request, id):
    car=Car.objects.get(id=id)
    if request.method=="POST":
        form= CarForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            car.brand=info["brand"]
            car.model=info["model"]
            car.year=info["year"]
            car.mile=info["mile"]
            car.save()
            cars=Car.objects.all()
            return render(request, "AppCoder/car.html" ,{"cars":cars, "message": "Car edited"})
        pass
    else:
        form= CarForm(initial={"brand":car.brand, "model":car.model, "year":car.year, "mile":car.mile})
        return render(request, "AppCoder/carEdit.html", {"form": form, "car": car})




#SERVICE#
def serviceForm(request):
    if request.method=="POST":
        form= ServiceForm(request.POST)
        
        if form.is_valid():
            informacion=form.cleaned_data
            type= informacion["type"]
            time= informacion["time"]
            price= informacion["price"]
            service= Service(type=type, time=time, price=price)
            service.save()
            services=Service.objects.all()
            return render(request, "AppCoder/service.html" ,{"services":services, "message": "Service saved"})
        else:
            return render(request, "AppCoder/serviceForm.html" ,{"form": form, "message": "Invalid data"})
        
    else:
        form= ServiceForm()
        return render (request, "AppCoder/serviceForm.html", {"form": form})


def readService(request):
    services=Service.objects.all()
    return render(request, "AppCoder/service.html", {"services": services})


def deleteService(request, id):
    service=Service.objects.get(id=id)
    print(service)
    service.delete()
    services=Service.objects.all()
    return render(request, "AppCoder/service.html", {"services": services, "message": "Service deleted"})


def serviceEdit(request, id):
    service=Service.objects.get(id=id)
    if request.method=="POST":
        form= ServiceForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            service.type=info["type"]
            service.time=info["time"]
            service.price=info["price"]
            service.save()
            services=Service.objects.all()
            return render(request, "AppCoder/service.html" ,{"services":services, "message": "Service edited"})
        pass
    else:
        form= ServiceForm(initial={"type":service.type, "time":service.time, "price":service.price})
        return render(request, "AppCoder/serviceEdit.html", {"form": form, "service": service})


#SEARCH

def brandSearch(request):
    return render(request, "AppCoder/carSearch.html")
    
def search(request):
    
    brand= request.GET["brand"]
    if brand!="":
        cars= Car.objects.filter(brand__icontains=brand)
        return render(request, "AppCoder/resultSearch.html", {"cars": cars})
    else:
        return render(request, "AppCoder/resultSearch.html", {"message": "Insert a brand to find a car!"})

