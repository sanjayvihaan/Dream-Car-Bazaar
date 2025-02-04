from django.shortcuts import render
from ProductManagement.models import *
from UserManagement.models import *

# Create your views here.


def pending_car_approval(request):
    all_car_details = CarDetails.objects.all()
    return render(request, "Executive/product/pending_approval.html",{'all_car_details': all_car_details})
