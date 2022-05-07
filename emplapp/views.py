from unicodedata import name
from django.shortcuts import render,redirect
from userapp.models import Booking, Review, WorkerDetails
from django.core.files.storage import FileSystemStorage
from .models import Gallery
# Create your views here.
def fnmaster(request):
    return render(request,'mat.html')


# def fndeatil(request):
#     return render(request,'detail.html')  
# 
#   
def fnwork_profile(request):
    workerid=request.session['workerid']
    if request.method=='POST':
        pass
    else:
        viewprofile=WorkerDetails.objects.get(workerlogin_id=workerid)
        galleryimg = Gallery.objects.filter(login_id=workerid)
        print(galleryimg)  
    return render(request,'workprofile.html',{'viewprofile':viewprofile,'galleryimg':galleryimg})  


def fnwork_dash(request):
    return render(request,'dash.html')  


def fnorder(request):
    workerId=request.session['workerid']
    print(workerId)

    worker=WorkerDetails.objects.get(workerlogin_id=workerId)
    print(worker)
    booked=Booking.objects.filter(worker__id=worker.id)
    # for i in book:
    #     print(i.user.name)

    return render(request,'order.html',{'booked':booked})    


def fnreview(request):
    workerid = request.session['workerid']
    workerviewid = WorkerDetails.objects.get(workerlogin_id=workerid)
    print(workerviewid)
    viewreview= Review.objects.select_related('login_user').filter(worker_id=workerviewid)
    print(viewreview)
    return render(request,'review.html',{'viewreview':viewreview}) 


def fnquick(request):
    return render(request,'quick.html')  


def fnedit(request):
    workerid=request.session['workerid']
    if request.method=='POST':
        editfirstname=request.POST['pname']
        editlastname=request.POST['lname']
        editemail=request.POST['pemail']
        editphone=request.POST['pphone']
        editpincode=request.POST['ppin']
        editaddress=request.POST['padd']
        editlocation=request.POST['plocation']
        editdistrict=request.POST['pdis']
        editeducation=request.POST['pedu']
        editimg=request.FILES['editimg']
        # print(editimg)
        updimg= editimg
        # test = "Worker_images/"+updimg.name
        # print(test)
        #####################
        obj1= FileSystemStorage()
        obj1.save(editimg.name,editimg)
        ################
        WorkerDetails.objects.filter(workerlogin_id=workerid).update(first_name=editfirstname, last_name=editlastname, w_email=editemail, w_phone=editphone, w_address=editaddress, w_pincode=editpincode, location=editlocation, district=editdistrict, education_qualification=editeducation, w_profilePic=editimg.name)
        return redirect('/work/profile')
    else:
        viewprofile=WorkerDetails.objects.get(workerlogin_id=workerid)
        
    return render(request,'edit.html',{'viewprofile':viewprofile}) 


def fnworkdone(request):
    return render(request,'workdone.html')


def fnrejwork(request):
    return render(request,'rejectwork.html')  


def fnquickdone(request):
    return render(request,'quickdone.html') 


def fnquickreject(request):
    return render(request,'quickreject.html')                        


def logout(req):
    del req.session['workerid']
    return redirect('/user/home')  


def imgalley(request):
    # print(request.session['workerid'])
    # current_user = WorkerDetails.objects.get(id=request.session['workerid'])
    crc = request.session['workerid']
    if request.method=='POST':
        galleryimage=request.FILES['imgalley']  
        print(galleryimage)
        galleryimg=Gallery(picture=galleryimage, login_id=crc)
        galleryimg.save()
        return redirect('/work/profile')
    else:
        workersec=request.session['workerid']
        print(workersec)
        galleryimg = Gallery.objects.filter(login_id=workersec)
        print(galleryimg)   
    return redirect('/work/profile')


