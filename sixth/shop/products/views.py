from django.shortcuts import render, redirect
from .models import ProductCategory, Product, Basket
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


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


@login_required(login_url='/users/login/')
def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        # Basket.objects.create(user=request.user, product=product, quantity=1)
        basket = Basket(user=request.user, product=product, quantity=1)
        basket.save()
        return redirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return redirect(current_page)


def basket_minus(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if baskets.exists():
        basket = baskets.first()
        if basket.quantity > 1:
            basket.quantity -= 1
            basket.save()
        else:
            basket.delete()
        return redirect(current_page)


def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return redirect(request.META.get('HTTP_REFERER'))
