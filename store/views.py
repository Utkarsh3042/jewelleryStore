from django.shortcuts import render, get_object_or_404, redirect
from .models import Jewels,Category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from .forms import CustomSignUp
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib import messages


def is_staff_user(user):
    if not user.is_staff:
        raise PermissionDenied
    return True

@login_required
@user_passes_test(is_staff_user)
def adminpanel(request):
    jewellery = Jewels.objects.all().order_by("-id")
    return render(request, 'store/admin.html', {'jewellery':jewellery})

@login_required
@user_passes_test(is_staff_user)
def add_jewellery(request):
    if request.method == 'POST':
        jewel_name = request.POST.get('jewel_name')
        jewel_description = request.POST.get('jewel_description')
        jewel_price = request.POST.get('jewel_price')
        jewel_image = request.FILES.get('jewel_image')
        category_id = request.POST.get('category')
        new_category = request.POST.get('new_category')

        if Jewels.objects.filter(jewel_name=jewel_name).exists():
            messages.error(request, f'{jewel_name} already exists')
            

        else:
            if new_category:
                category, created = Category.objects.get_or_create(category_name=new_category)
            else:
                category = Category.objects.get(id=category_id)
        
        #note::condition to check if jewel already exists

            Jewels.objects.create(
                jewel_name=jewel_name,
                jewel_price=jewel_price,
                jewel_description=jewel_description,
                jewel_image=jewel_image,
                jewel_category=category,
            )
            messages.success(request, 'Item added Successfully')
            return redirect('adminpanel')

    categories = Category.objects.all()
    return render(request,'store/add_jewellery.html', {'categories': categories})

@login_required
@user_passes_test(is_staff_user)
def edit_jewellery(request,pk):
    jewel = get_object_or_404(Jewels,pk=pk)
    if request.method == 'POST':
        jewel.jewel_name = request.POST.get('jewel_name')
        jewel.jewel_description = request.POST.get('jewel_description')
        jewel.jewel_price = request.POST.get('jewel_price')
        
        # Check if a new image is uploaded
        if 'jewel_image' in request.FILES:
            jewel.jewel_image = request.FILES['jewel_image']
        
        jewel.save()
        messages.success(request, 'Item Details Updated Successfully')
        return redirect('adminpanel')

    return render(request,'store/edit_jewellery.html',{'jewel':jewel})

@login_required
@user_passes_test(is_staff_user)
def delete_jewellery(request,pk):
    jewel = get_object_or_404(Jewels,pk=pk)
    if request.method=='POST':
        jewel.delete()
        messages.info(request, 'Item Deleted Successfully')
        return redirect('adminpanel')
    return render(request,'store/delete_jewellery.html',{'jewel':jewel})



def home(request):
    categories = Category.objects.all()
    jewellery = Jewels.objects.all().order_by("-id")
    return render(request, 'store/home.html', {'jewellery': jewellery,'categories': categories})


def signup(request):
    if request.method == 'POST':
        form = CustomSignUp(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created, You can now Login into your account')
            return redirect('signin')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = CustomSignUp()
    return render(request, 'store/signup.html', {'form':form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, 'Login Successful')
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)            
    else:
        form = AuthenticationForm()
    return render(request, 'store/signin.html',{'form':form})


def logout_view(request):
    logout(request)
    messages.info(request,'Log out')
    return redirect('signin')



def details(request, pk):
    jewel = get_object_or_404(Jewels, pk=pk)
    #print(jewel)
    return render(request, 'store/details.html', {'jewel':jewel})

def category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    jewellery = Jewels.objects.filter(jewel_category=category).order_by("-id")
    #print(jewellery)
    return render(request, 'store/category.html' , {'jewellery': jewellery, 'category': category })
    

def about(request):
    return render(request, 'store/about.html')


def search_view(request):
    search_item = request.GET.get('search')    
    jewellery = Jewels.objects.filter(jewel_name__icontains=search_item).order_by("-id")
    return render(request, 'store/search.html', {'jewellery':jewellery, 'search_item':search_item})


def forget_password(request):
    return redirect('signin')