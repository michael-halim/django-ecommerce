from django.shortcuts import redirect, render
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

def register(request):
    if request.method =='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('myapp/products')

    form = NewUserForm()
    context = {
        'form':form,
    }
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')


def create_profile(request):
    if request.method == 'POST':
        contact = request.POST.get('contact')
        image = request.FILES['upload']
        user = request.user   
        profile = Profile(user=user, image=image, contact_number = contact)
        profile.save()

    return render(request, 'users/create_profile.html')

def seller_profile(request,id):
    seller = User.objects.get(id=id)
    context = {
        'seller':seller,
    }
    return render(request, 'users/seller_profile.html',context=context)