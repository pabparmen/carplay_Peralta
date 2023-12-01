from django.shortcuts import render, get_object_or_404
from .models import Category, Department, Manufacturer, Product


def product_list(request, category_slug=None,department_slug=None,manufacturer_slug=None):
    category = None
    department = None
    manufacturer = None

    categories = Category.objects.all()
    departments = Department.objects.all()
    manufacturers = Manufacturer.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if department_slug:
        department = get_object_or_404(Department, slug=department_slug)
        products = products.filter(department=department)

    if manufacturer_slug:
        manufacturer = get_object_or_404(Manufacturer, slug=manufacturer_slug)
        products = products.filter(manufacturer=manufacturer)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'department':department,
                   'departments':departments,
                   'manufacturer':manufacturer,
                   'manufacturers':manufacturers,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    return render(request, 'shop/product/detail.html', {'product': product})