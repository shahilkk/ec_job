from django.shortcuts import render,redirect
from userapp.models import Contact, Package, WorkerDetails,Login,UserDetails,Review
from emplapp.models import Gallery
from userapp.views import login
from django.db.models import Count
# Create your views here.
def fnindex(request):
    return render(request,'index.html')


def package(request):
    viewpackage = Package.objects.select_related('user').all()
    return render(request,'package.html',{'viewpackage':viewpackage})  


def fndash1(request):
    worker=WorkerDetails.objects.select_related('workerlogin').filter(workerlogin__status=False,workerlogin__mode='Active')
    # worker=WorkerDetails.objects.all()
    workerdel=WorkerDetails.objects.select_related('workerlogin').filter(workerlogin__mode='Deactivate',workerlogin__status=False)
    total_worker= WorkerDetails.objects.all().count()
    print(total_worker)
    return render(request,'dash1.html',{'worker':worker,'workerdel':workerdel,'total_worker':total_worker})     


def fnviewwork(request):
    worker=WorkerDetails.objects.select_related('workerlogin').all()
    print(worker)
    return render(request,'listworker.html',{'worker':worker})      


def fnviewuser(request):
    user=UserDetails.objects.all()
    return render(request,'listuser.html',{'user':user}) 


def fnprowork(request,profile_id):
    print(profile_id)
    workerprofile = WorkerDetails.objects.get(workerlogin_id=profile_id)
    print(workerprofile.first_name)
    galleryimg = Gallery.objects.filter(login_id=profile_id)
    print(galleryimg) 
    viewreview= Review.objects.select_related('login_user').filter(worker_id=workerprofile)
    return render(request,'prowork.html',{'workerprofile':workerprofile,'galleryimg':galleryimg,'viewreview':viewreview})    


def fnprouser(request,user_id):
    print(user_id)
    userdetails = UserDetails.objects.select_related('userlogin').get(userlogin_id=user_id)
    print(userdetails.name)
    return render(request,'prouser.html',{'userdetails':userdetails})      


def fncontact(request):
    adminmess=Contact.objects.select_related('user').all()
    return render(request,'contactdetails.html',{'adminmess':adminmess})


def accpet(req,selected_id):
    print(selected_id)
    Login.objects.filter(id=selected_id).update(status=True)

    # accpeted_id= WorkerDetails.objects.get(id=selected_id)
    # print(accpeted_id)


    # sub=WorkerDetails.objects.select_related('workerlogin').filter(id=selected_id).update(status=True)
    # print(sub)

    

    # acc=accpeted_id.select_related('workerlogin').update(workerlogin__status=True)
    # print(acc)


    # Login.objects.filter(status=False).update(status=True) 
    return redirect ('/admin/home')      

def delect(req,delected_id):
    print(delected_id)
    Login.objects.filter(id=delected_id).update(mode="Deactivate",status=False)
    # Login.objects.filter(status=True).update(status=False)
    return redirect ('/admin/home')
    

