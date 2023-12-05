from django.shortcuts import render, get_object_or_404
from .models import Category, Department, Manufacturer, Product
from cart.forms import CartAddProductForm
from django.db.models import Q

def product_list(request, category_slug=None,department_slug=None,manufacturer_slug=None):
    category = None
    department = None
    manufacturer = None

    categories = Category.objects.all()
    departments = Department.objects.all()
    manufacturers = Manufacturer.objects.all()
    products = Product.objects.all()

    #Esto es para la busqueda segun las tres categorias dadas. 

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if department_slug:
        department = get_object_or_404(Department, slug=department_slug)
        products = products.filter(department=department)

    if manufacturer_slug:
        manufacturer = get_object_or_404(Manufacturer, slug=manufacturer_slug)
        products = products.filter(manufacturer=manufacturer)


    #Esto es para la busqueda del producto segun el nombre

    search_query = request.GET.get('q')
    if search_query:
        products = products.filter(Q(name__icontains=search_query))


    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'department':department,
                   'departments':departments,
                   'manufacturer':manufacturer,
                   'manufacturers':manufacturers,
                   'products': products,
                   'search_query': search_query})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)

    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})