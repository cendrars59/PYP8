from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Product, Category
from users.models import User


def catalogue(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    # Get current page number
    page = request.GET.get('page')
    try:
        # Return only this page albums and not others
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
    context = {
        'products': products
    }
    return render(request, 'catlog/catalogue.html', context)


def detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {
        'product': product,
        'product_categories': product.categories.all(),
        'product_stores': product.stores.all(),
        'product_brands': product.brands.all(),
        'nutriscore_image': 'dist/assets/img/nutri/Nutri-score-{0}.png'.format(product.nutrition_grade_fr.upper())
    }
    print(context)
    return render(request, 'catlog/detail.html', context)


def search(request):
    query = request.GET.get('query')
    page_to_return = ''
    products = []
    context = {
                'products': [], 
                'title': "",
                'query': query,
                'paginate': True,
                'picture_head': None,
                'perfect_match': False
            }

    # In those cases we display the catalogue page
    if not query or len(Product.objects.filter(name__icontains=query)) == 0:
        products = Product.objects.all()
        page_to_return = 'catlog/catalogue.html'
        context['title'] = "Pas de resultat pour %s" %query
    else:
        if len(Product.objects.filter(name__icontains=query)) > 1:
            products = Product.objects.filter(name__icontains=query)
            context['title'] = "%s" %query 
        elif len(Product.objects.filter(name__icontains=query)) == 1:
            temp_list = Product.objects.filter(name__icontains=query)
            product = Product.objects.get(pk=temp_list[0].id)
            products = product.get_recommanded_products()
            context['picture_head'] = product.url_images
            context['perfect_match'] = True
        context['title'] = "%s" %query.upper()          
        page_to_return = 'catlog/search.html'
    paginator = Paginator(products, 6)
    # Get current page number
    page = request.GET.get('page')
    try:
        # Return only this page albums and not others
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
    context['products'] = products
    return render(request, page_to_return, context)

    def saving_product(request, user_id, product_id):
        pass
