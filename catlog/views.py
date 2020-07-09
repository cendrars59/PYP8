from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from users.models import User, UserProductsSearch

from .models import Product


def detail(request, product_id):
    """Accordingv the requesting, getting the information for
    a given product.

    Args:
        request (request): Incoming request
        product_id (integer): technical id of the product

    Returns:
        view: return the view according the product info
    """
    product = Product.objects.get(pk=product_id)
    context = {
        'product': product,
        'product_categories': product.categories.all(),
        'product_stores': product.stores.all(),
        'product_brands': product.brands.all(),
        'nutriscore_image': 'dist/assets/img/nutri/Nutri-score-{0}.png'.format(
            product.nutrition_grade_fr.upper()
        ),
    }
    print(context)
    return render(request, 'catlog/detail.html', context)


def search(request):
    """ If the request is type Get
    According the user request retrieve the product.
    if no match : User is notified that there is no results
    if more than one match : User is notified that the user has to refine
    his or her request.
    if one match : Get the product and then get the list of recommanded
    products associated with.

    If the request is type Post
    Saving the selected product

    Args:
        request (request): [description]

    Returns:
        [type]: Return the context to display.
    """

    if request.method == 'GET':

        query = request.GET.get('query')
        products = []
        context = {
            'products': [],
            'title': "",
            'query': query,
            'paginate': True,
            'picture_head': None,
            'perfect_match': False,
            'product': None,
        }
        # In those cases we display the catalogue page
        if (
            not query
            or len(Product.objects.filter(name__icontains=query)) == 0
        ):
            products = []
            context['title'] = "Pas de résultat pour %s" % query
            context['products'] = products
            return render(request, 'catlog/search.html', context)
        # In this case user has to refine his or her request
        if len(Product.objects.filter(name__icontains=query)) > 1:
            products = []
            context['title'] = (
                "Trop de résultats pour %s. Affinez votre recherche" % query
            )
        # In returning the found product and recommanded products associated
        #  with
        elif len(Product.objects.filter(name__icontains=query)) == 1:
            temp_list = Product.objects.filter(name__icontains=query)
            product = Product.objects.get(pk=temp_list[0].id)
            products = product.get_recommanded_products()
            context['picture_head'] = product.url_images
            context['perfect_match'] = True
            context['title'] = "%s" % query.upper()
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
                # If page is out of range (e.g. 9999), deliver last page
                #  of results.
                products = paginator.page(paginator.num_pages)
            context['product'] = product
        context['products'] = products

        return render(request, 'catlog/search.html', context)
    # saving the product
    elif request.method == 'POST':
        subproduct = Product.objects.get(
            id=int(request.POST.get('subproductid'))
        )
        user = User.objects.get(id=int(request.POST.get('userid')))
        product = Product.objects.get(id=int(request.POST.get('productid')))
        if (
            len(
                UserProductsSearch.objects.filter(
                    user=user, mainProduct=product, subProduct=subproduct
                )
            )
            == 0
        ):
            print("Toto")
            UserProductsSearch.objects.create(
                user=user, mainProduct=product, subProduct=subproduct
            )
        return redirect(request.POST.get('next'))
