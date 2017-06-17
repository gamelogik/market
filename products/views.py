from django.shortcuts import render
from django.http import Http404

from django.shortcuts import render, get_object_or_404
# Create your views here.

from .forms import ProductAddForm, ProductModelForm
from .models import Product

def create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.sale_price = instance.price
        instance.save()

    # if form.is_valid():
    #     data = form.cleaned_data
    #     title = data.get("title")
    #     description = data.get("description")
    #     price = data.get("price")
    #     new_obj = Product.objects.create(title=title, description=description, price=price)

    template = "form.html"
    context = {
        'form':form,
        "submit_btn": "Create Product"
    }
    return render(request, template, context)

def update_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    form = ProductModelForm(request.POST or None, instance=product)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.sale_price = instance.price
        instance.save()
    template = "form.html"
    context = {
        "object": product,
        "form": form,
        "submit_btn": "Update Product"
    }
    return render(request, template, context)


def detail_slug_view(request, slug=None ):
    try:
        product = get_object_or_404(Product, slug=slug)
    except Product.MultipleObjectsReturned:
        product = Product.objects.filter(slug=slug).order_by("-title").first()

    template = "detail_view.html"
    context = {
        "object": product
    }
    return render(request, template, context)

def detail_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    template = "detail_view.html"
    context = {
        "object": product
    }
    return render(request, template, context)

    # if object_id is not None:
    #     product = get_object_or_404(Product, id=object_id)
    #
    #     # product = Product.objects.get(id=object_id)
    #     # try:
    #     #     product = Product.objects.get(id=object_id)
    #     # except Product.DoesNotExist:
    #     #     product = None
    # else:
    #     raise Http404


def list_view(request):
    queryset = Product.objects.all()
    template = "list_view.html"
    context = {"queryset": queryset}
    return render(request, template, context)
