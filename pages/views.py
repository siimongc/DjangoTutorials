from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from django import forms
from django.contrib import messages
from django.views.generic.edit import FormView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):  
    template_name = 'pages/about.html'  

    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)  
        context.update({  
            "title": "Acerca de nosotros - Tienda en línea",  
            "subtitle": "Acerca de nosotros",  
            "description": "en esta pagina estoy aprendiendo Django",  
            "author": "Desarrollado por: Simon Gaviria",  
        })  

        return context  

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contáctanos",
            "email": "Simon@gmail.com",
            "address": "Calle 123, Ciudad, País",
            "phone": "+57 300 123 4567",
        })
        return context
    

class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price": "$50"},
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": "$600"},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": "$400"},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": "$700"}
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        try:
            id = int(id)
            if id < 1 or id > len(Product.products):
                raise ValueError
            
            viewData = {}
            product = Product.products[id-1]
            product["numeric_price"] = int(product["price"].replace("$", ""))
            viewData["title"] = product["name"] + " - Online Store"
            viewData["subtitle"] = product["name"] + " - Product information"
            viewData["product"] = product

            return render(request, self.template_name, viewData)

        except (ValueError, IndexError):
            return HttpResponseRedirect('/')

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise forms.ValidationError("The price must be greater than zero.")
        return price


from django.contrib import messages

class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {
            "title": "Create product",
            "form": form
        }
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            messages.success(request, "Product created") 
            return redirect('index')
        else:
            viewData = {
                "title": "Create product",
                "form": form
            }
            return render(request, self.template_name, viewData)
