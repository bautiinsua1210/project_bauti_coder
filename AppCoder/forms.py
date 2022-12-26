from django import forms

class ClientForm(forms.Form):
    name= forms.CharField(label="Name", max_length=50)
    surname= forms.CharField(label="Surname", max_length=50)
    email= forms.EmailField(label="Email")
    role= forms.CharField(label="Role", max_length=50)

class CarForm(forms.Form):
    brand= forms.CharField(label="Brand", max_length=50)
    model= forms.CharField(label="Model", max_length=50)
    year= forms.IntegerField(label="Year")
    mile= forms.IntegerField(label="Mile")

class ServiceForm(forms.Form):
    type= forms.CharField(label="Type", max_length=50)
    time= forms.IntegerField(label="Time")
    price= forms.IntegerField(label="Price")




