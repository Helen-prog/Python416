from django.shortcuts import render
from .models import ProductCategory, Product
from django.core.paginator import Paginator


def index(request):
    context = {
        'title': 'Market Place'
    }
    return render(request, "products/index.html", context)


def products(request, category_id=None):
    context = {
        'title': 'Market Place - Каталог',
        'categories': ProductCategory.objects.all(),
        # 'products': Product.objects.all()
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    paginator = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context.update({'products': page_obj})
    return render(request, "products/products.html", context)


def product(request, pk):
    product_obj = Product.objects.get(id=pk)
    context = {
        'title': product_obj.name,
        'product': product_obj,
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/product.html', context)
