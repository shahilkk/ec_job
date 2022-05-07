# from crypt import methods
from email import message
from time import time
from unicodedata import category
from django.shortcuts import render, redirect
from emplapp.models import Gallery
from .models import Booking, UserDetails,Login,WorkerDetails,Contact,Quick_booking,Package,Review
from decorator import user_login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
def fnmaster(request):
    # print('session',request.session['userid'])
    # pid=request.session['userid']
    # userid=Login.objects.get(id=pid)
    return render(request,'master.html')

@csrf_exempt
def signup(request):
    if request.method=='POST':
        uname=request.POST['regname']
        uusername=request.POST['reguser']
        uphone=request.POST['regphone']
        uemail=request.POST['regemail']
        upass=request.POST['regpass']
        userLogin=Login(username=uusername,userpassword=upass,usertype='user',status=True,mode='Active')
        userLogin.save()
        data=UserDetails(name=uname,phone=uphone,email=uemail,userlogin_id=userLogin.id, pincode=0,address='' )
        data.save()
        return render(request,'home.html',{'status':1})
    else:
        return render(request,'home.html',{'status':0})

def login(request):

     if request.method=='POST':
        u_name=request.POST['name']
        u_pass=request.POST['pass']

        # login_data=Login.objects.filter(username=u_name,userpassword=u_pass).exists()
        try:
            login_data=Login.objects.filter(username=u_name,userpassword=u_pass).exists()
            if login_data:
                data=Login.objects.get(username=u_name,userpassword=u_pass)
                if data.usertype=='user':

                    request.session['userid']=data.id
                    return redirect('/user/home')
                else:
                    if data.status:
                        request.session['workerid']=data.id
                        return redirect('/work/dash')
                    else:
                        return render(request,'home.html')
        except Login.DoesNotExist:
            return render(request,'home.html')               
                     
     return render(request,'home.html')                 


        # if login_data:
        #     data=Login.objects.get(username=u_name,userpassword=u_pass)

        #     if data.usertype=='user':
        #         request.session['userid']=data.id
        #         return redirect('/user/home')
        #     else:
        #         if data.status:
        #             request.session['workerid']=data.id
        #             return redirect('/work/dash')
        #         else:
        #             return render(request,'home.html')


        # try:
        #     worklogin=Login.objects.get(username=u_name,userpassword=u_pass,usertype='worker',status=True)
        #     return redirect('/work/dash')
        # except Login.DoesNotExist:
        #     return render(request,'home.html')
        # try:
        #     deatils=Login.objects.get(username=u_name,userpassword=u_pass)
        #     # print(deatils.id)
        #     request.session['userid']=deatils.id
        #     return redirect('/user/home')
        # except Login.DoesNotExist:
        #     return render(request,'home.html')


def logout(request):
    del request.session['userid']
    return redirect('/user/home')


def workreg(request):
    if request.method=='POST':
        workercategory=request.POST['category']
        workersubcategory=request.POST['subcategory']
        workerfirstname=request.POST['firstname']
        workerlastname=request.POST['lastname']
        workerusername=request.POST['username']
        workerpassword=request.POST['password']
        workeremail=request.POST['email']
        workerphone=request.POST['phone']
        workerimg=request.FILES['workimg']
        workeraddress=request.POST['address']
        workeraddition=request.POST['addition']
        workerdob=request.POST['dob']
        workerage=request.POST['age']
        workerpin=request.POST['pin']
        workerplace=request.POST['place']
        workerdistrict=request.POST['district']
        workerstate=request.POST['state']
        workerloca=request.POST['loca']
        workereduc=request.POST['educ']
        workerjob=request.POST['radio']
        workerLogin=Login(username=workerusername,userpassword=workerpassword,usertype='worker',status=False,mode='Active')
        workerLogin.save()
        workerdata=WorkerDetails(first_name=workerfirstname, last_name=workerlastname, w_email=workeremail, w_phone=workerphone, w_profilePic=workerimg, category=workercategory, subcategory=workersubcategory,jobtype=workerjob,  w_address=workeraddress, additional_information=workeraddition, date_of_birth=workerdob, age=workerage, w_pincode=workerpin, place=workerplace, district=workerdistrict, state=workerstate, location=workerloca, education_qualification=workereduc, workerlogin_id=workerLogin.id)
        workerdata.save()
        return redirect('/user/home')
 


  

def fnhome(request):
    return render(request,'home.html') 

@user_login_required
def fnprofile(request):
    if request.method=='POST':
        editname=request.POST['name']
        edituser=request.POST['username']
        editemail=request.POST['email']
        editphone=request.POST['phone']
        editpass=request.POST['password']
        addpincode=request.POST['pincode']
        addaddress=request.POST['addre']
        img=request.FILES['upload']

        print(img)
        obj1 = FileSystemStorage()
        obj1.save(img.name,img)
        
        id=request.session['userid']
        UserDetails.objects.filter(userlogin_id=id).update(name=editname,phone=editphone,email=editemail,pincode=addpincode,address=addaddress,profilePic=img)
        Login.objects.filter(id=id).update(username=edituser,userpassword=editpass)
        return redirect('profile')
        
    else:
        pid=request.session['userid']
        view_login=Login.objects.get(id=pid)
        view_pro=UserDetails.objects.get(userlogin=pid)
        return render(request,'profile.html',{'user':view_pro,'login_data':view_login})
     

@user_login_required
@csrf_exempt
def search_list(request):
    if request.method=='POST':
        searchlist=request.POST['search']
        if searchlist!="":
            srch_products=WorkerDetails.objects.filter(Q(first_name__icontains=searchlist) | Q(last_name__icontains=searchlist) | Q(category__icontains=searchlist) | Q(subcategory__icontains=searchlist) | Q(place__icontains=searchlist))
            print(srch_products)
            if srch_products.exists():
                return render(request,'search.html',{'searchproduct':srch_products})
            else:
                return render(request,'home.html',{'msg':' No Result Found '}) 
        else:
            return redirect('/user/home')    
    else:
        return redirect('/user/home')   
        



       
def fnwrkpro(request,selected_workerid):
    if request.method=='POST':
        reviewmessage=request.POST['reviewmessage']
        # workerid=request.POST['workerid']
        userid=request.session['userid']
        print(reviewmessage,userid)
        userreviewid=UserDetails.objects.get(userlogin=userid)
        viewworkerreview=WorkerDetails.objects.get(workerlogin_id=selected_workerid)
        reviewmodel = Review(details=reviewmessage,login_user=userreviewid, worker=viewworkerreview)
        reviewmodel.save()
        return redirect('/user/home')
    else:
        print(selected_workerid)
        viewworker=WorkerDetails.objects.get(workerlogin_id=selected_workerid)
        # workersec=request.session['workerid']
        # print(workersec)
        galleryimg = Gallery.objects.filter(login_id=selected_workerid)
        print(galleryimg)
        reviewdetails= Review.objects.select_related('login_user').filter(worker_id=viewworker)
        print(reviewdetails)
        return render(request,'wrkpro.html',{'viewworker':viewworker,'galleryimg':galleryimg,'reviewdetails':reviewdetails}) 


def booking(request):
    if request.method=='POST':
        bookingdate=request.POST['bookingdate']
        bookingtime=request.POST['bookingtime']
        workerid=request.POST['workerid']
        userid=request.session['userid']
        print(userid)
        user_id=UserDetails.objects.get(userlogin_id=userid)
        print(user_id)
        worker_id=WorkerDetails.objects.get(id=workerid)
        workerbooking = Booking(date=bookingdate, time=bookingtime, worker=worker_id, user=user_id)
        workerbooking.save()
        print(workerbooking)
        print(bookingdate,bookingtime,userid,workerid)

        return redirect('/user/home')  




def quickbooking(request):
    if request.method=='POST':
        print('***************')
        incity=request.POST['city']
        location=request.POST['location']
        landmark=request.POST['landmark']
        date=request.POST['date']
        time=request.POST['time']
        pin=request.POST['pin']
        uid=request.session['userid']
        userid=UserDetails.objects.get(userlogin_id=uid)
        print(userid)
        quick=Quick_booking(landmark=landmark, city=incity,location=location,date=date, time=time,login_id=userid  )
        quick.save()

        print(incity,location,landmark,date,time,pin)
        selected_pincode=WorkerDetails.objects.filter(w_pincode=pin)
        print(selected_pincode)
        return redirect('/user/view') 


@user_login_required
def fnview(request, selected_subcategory):
    viewlist=WorkerDetails.objects.filter(subcategory=selected_subcategory)
    uid=request.session['userid']
    viewpincode = UserDetails.objects.get(userlogin__id=uid)
    # print(viewpincode)

    return render(request,'viework.html',{'viewlist':viewlist,'viewpincode':viewpincode}) 






def review(request):
    if request.method=='POST':
        reviewmessage=request.POST['reviewmessage']
        workerid=request.POST['workerid']
        userid=request.session['userid']
        print(reviewmessage,workerid,userid)

        return redirect('/user/wrkpro')
    


        
def fnservice(request):
    return render(request,'service.html') 
         
def fnregistration(request):
    return render(request,'registration.html')  
                                          
def fncontact(request):
    if request.method=='POST':
        message=request.POST['mess']
        pid=request.session['userid']
        print(pid)
        userr=UserDetails.objects.get(userlogin__id=pid)
        reqmessage = Contact(message=message, user=userr)
        reqmessage.save()
    return render(request,'contact.html') 

def fnpayment(request):
    return render(request,'payment.html')      


def gallery(request):
    pic= Gallery.objects.select_related('login').all()
    return render(request,'gallery.html',{'pic':pic})                                       


def price(request):
    if request.method=='POST':
        print('hi')
        standard=request.POST['standard']
        print(standard)
        pid=request.session['userid']
        print(pid)
        ud=UserDetails.objects.get(userlogin_id=pid)
        print(ud)
        pack = Package(user=ud, selected_Package=standard)
        pack.save()
        return redirect('/user/home')