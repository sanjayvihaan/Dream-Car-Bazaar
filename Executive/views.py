from django.shortcuts import render,HttpResponseRedirect
from ProductManagement.models import *
from UserManagement.models import *
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
# Create your views here.


def pending_car_approval(request):
    all_car_details = CarDetails.objects.all()
    return render(request, "Executive/product/pending_approval.html",{'all_car_details': all_car_details})




def car_review(request):
    if request.method == "POST":
        car_id = request.POST.get('car_id')
        approval_status = request.POST.get('approval')

        car_detail = get_object_or_404(CarDetails, id=car_id)

        if approval_status == 'yes':
            car_detail.review = 'approved'
            car_detail.status = 'live'
            car_detail.is_draft = False
            full_name = f"{car_detail.variant.model.brand.name} {car_detail.variant.model.name} {car_detail.variant.name}"
            
            if car_detail.created_by:
                user_name = car_detail.created_by.get_full_name()
                msg = f"User {user_name} car {full_name} is approved by the admin. Added to Live Cars!"
                print(msg)
                Notification.objects.create(user=car_detail.created_by, message=msg, source='admin') 
            else:
                msg = f"Car {full_name} is approved by the admin but not associated with user"
                print(msg)
            
            #  messages.success(request, f"Car #{car_detail.id} approved successfully!")
        elif approval_status == 'no':
            car_detail.review = 'rejected'
            full_name = f"{car_detail.variant.model.brand.name} {car_detail.variant.model.name} {car_detail.variant.name}"
            
            if car_detail.created_by:
                user_name = car_detail.created_by.get_full_name()
                msg = f"User {user_name} car {full_name} is rejected by the admin. Added to Rejected Cars!"
                print(msg)

                Notification.objects.create(user=car_detail.created_by, message=msg, source='admin')
            else: 
                msg = f"Car {full_name}  is rejected by the admin"
                print(msg)


        car_detail.save()
        referrer = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(referrer) 
        
