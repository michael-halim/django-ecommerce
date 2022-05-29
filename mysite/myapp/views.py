from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.paginator import Paginator
def index(request):
    return HttpResponse('hello there')

# def products(request):
#     page_obj = products = Product.objects.all()

#     product_name = request.GET.get('product_name')
#     if product_name != '' and product_name is not None:
#         page_obj = products.filter(name__icontains = product_name)
        

#     paginator = Paginator(page_obj,3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'page_obj':page_obj
#     }
#     return render(request,'myapp/index.html',context)


# def product_detail(request,id):
#     product = Product.objects.get(id=id)
#     context = {
#         'product':product
#     }
#     return render(request,'myapp/detail.html',context)

# @login_required
# def add_product(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         desc = request.POST.get('desc')
#         image = request.FILES['upload']
#         seller_name=request.user
#         product = Product(name=name, price=price, desc=desc, image=image,seller_name=seller_name)
#         product.save()

#     return render(request,'myapp/addproduct.html')
# def update_product(request,id):
#     product = Product.objects.get(id=id)

#     if request.method == 'POST':
#         product.name = request.POST.get('name')
#         product.price = request.POST.get('price')
#         product.desc = request.POST.get('desc')
#         product.image = request.FILES['upload']

#         product.save()
#         return redirect('/myapp/products')

#     context = {
#         'product':product
#     }

#     return render(request, 'myapp/update_product.html',context)
    

# def delete_product(request,id):
# product = Product.objects.get(id=id)
# context = {
#     'product':product
# }

# if request.method == 'POST':
#     product.delete()
#     return redirect('/myapp/products')


# return render(request, 'myapp/delete_product.html',context)
# Class Based View [ListView]
class ProductListView(ListView):
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(name__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/detail.html'
    context_object_name = 'product'

class CreateProductView(CreateView):
    model = Product
    fields = ['name', 'price','desc', 'image', 'seller_name']

class UpdateProductView(UpdateView):
    model = Product
    fields = ['name', 'price','desc', 'image', 'seller_name']
    template_name_suffix = '_update_form'

class DeleteProductView(DeleteView):
    model = Product
    success_url = reverse_lazy('myapp:products')


@login_required
def my_listings(request):
    products = Product.objects.filter(seller_name=request.user)
    context = {
        'products':products, 
    }
    return render(request, 'myapp/my_listings.html',context)
