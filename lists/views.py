from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import List
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
#from .forms import RecordForm
from accounts.models import Profile
from datetime import date,timedelta,datetime
from django.core.mail import send_mail
from django.db.models import Q




# Create your views here.
def home(request):
    
    lists = List.objects.all()
    filter_item=''

    if 'filter' in request.GET:# for filtering
        filter_item=request.GET['filter']
        if filter_item =="all":
            
            contex={'lists':lists}
            
            return render(request, 'lists/home.html',contex)

        else:
            lists=lists.filter(Q(city__iexact=filter_item))
    context ={'lists': lists,'filter_item':filter_item}
    
    return render(request, 'lists/home.html',context)


@login_required(login_url="/accounts/login")

def create(request):
    
    
    if request.method == 'POST':
        if request.POST['city'] and request.POST['state'] and request.POST['available_date'] and request.POST['hotel_name'] and request.FILES['image']:
            product = List()
            product.city= request.POST['city']
            product.state = request.POST['state']
            a=request.POST['available_date']
            temp_date = datetime.strptime(a, "%Y-%m-%d").date()
            
            product.image = request.FILES['image']
           
            product.available_date = temp_date
            product.hotel_name = request.POST['hotel_name']
            messages.success(request,f'Your record has been saved !!')
            product.save()
            return redirect('create')
        else:
            return render(request, 'lists/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'lists/create.html')