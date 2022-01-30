from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from patient.models import Patient_Profile
from doctor.models import Doctor_Profile
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request, 'default/home.html', {})

def contact(request):
    try:
        if(request.method=="POST"):
            name = request.POST['name']
            subject = request.POST['subject']
            email = request.POST['email']
            message = request.POST['message']

            obj=Contact(name=name,subject=subject,email=email,message=message)
            obj.save()
            messages.success(request,"Message sent successfully")

            return redirect('contact')


        return render(request, 'default/contact-us.html', {})

    except:
        pass

    



def register(request):
    if request.method=="POST":
        email = request.POST["email"]
        fname = request.POST["fn"]
        lname = request.POST["ln"]

        dob = request.POST["dob"]
        contact = request.POST["contact"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        select = request.POST["select"]
        

        
        if User.objects.filter(email=email):
            messages.error(request,"Email already exist")
            return redirect('register')

        

        if pass1 != pass2:
            messages.error(request,"password did not match")
            return redirect('register') 

        if len(pass1)<6:
            messages.error(request,"Minimum length of password shuold be 6")
            return redirect('register')

        if len(pass1)>16:
            messages.error(request,"Maximun length of password shuold be 15")
            return redirect('register')

        
        myuser = User.objects.create_user(email,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname

        
        
        myuser.save()
        messages.success(request,"Account created sucessfully")

        
        if select=="1":
            Patient_Profile(
                user=myuser,
                First_name=fname,
                Last_name=lname,
                email = email,
                dob=dob,
                contact_no=contact,
                designation="Patient"
            ).save()
        else:
            Doctor_Profile(
                user=myuser,
                First_name=fname,
                Last_name=lname,
                email = email,
                dob=dob,
                contact_no=contact,
                designation="Doctor"
            ).save()


        

        
        return redirect('login')
    
    return render(request, 'default/register.html', {})



def Login(request):
    if request.method=='POST':
        
        username = request.POST["email"]
        pass1 = request.POST["password"]

        user = authenticate(username=username,password=pass1)
        if user is not None:
            user_obj = User.objects.filter(email=user.username).first()

            profile_obj = Patient_Profile.objects.filter(email = username ).first()

            if profile_obj is None:
                profile_obj = Doctor_Profile.objects.filter(email = username ).first()
                if not profile_obj.verify:
                    messages.error(request,"Account not verified!!!")
                    return redirect('login')

            messages.success(request,"Login Sucessfull!!!")
            return redirect('login') 

                
        else:
            messages.error(request,"Email or Password is wrong!!!")
            return redirect('login')

    return render(request, 'default/login.html', {})
