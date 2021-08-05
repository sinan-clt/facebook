from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import signupp,login

# Create your views here.
def test1(request):
    return HttpResponse ('<h1 align="center">hellloooo</h1>')


def facebook(request):
    try:    
      # if request.method=="POST":
        emaill=request.POST['email']
        user_exist=login.objects.filter(email=emaill).exists()
        if user_exist==False:
            fname=request.POST['f_name']
            print(fname)
            lname=request.POST['l_name']
            print(lname)
            mobile=request.POST['mob']
            print(mobile)


            passwordd=request.POST['password']
            print(passwordd)

            year=request.POST['year']
            print(year)
            month=request.POST['month']
            print(month)
            day=request.POST['day']
            print(day)
                    
            date=year+'-'+month+'-'+day
            print(date)

            gender=request.POST['gender']
            print(gender)

            objj=signupp(firstname=fname,lastname=lname,mobilenumber=mobile,birthday=date,gender=gender)
            print(objj.firstname,objj.lastname,objj.mobilenumber,objj.birthday,objj.gender)
            objj.save()

            loginObj=login(email=emaill,password=passwordd,user_id_id=objj.id)
            print(loginObj.email,loginObj.password)
            loginObj.save()

            return render(request,'facebook.html',{"message1":"user registered :)"})
            
        return render(request,'facebook.html',{"message2":"user already exist :("})
            
                
    except Exception as e:
        print(e)    
    # return render(request,'facebook.html',{"message":"user registration failed :("})
        
    return render(request,'facebook.html')


def fnlogin(request):
    try:
        username=request.POST['user_name']
        password=request.POST['user_password']
        obj=login.objects.get(email=username,password=password)
        request.session['user']=obj.id
        print(obj.user_id_id)
        
        nameobj=signupp.objects.get(id=obj.user_id_id)
        print(nameobj.firstname)
        # print(obj.id)

        return render(request,'home.html',{"user_name":nameobj})
        
    except Exception as e:
        print(e)
    return render(request,'facebook.html',{"message2":"invalid username or password"})

    # return render(request,'facebook.html')


def changepass(request):
    try:
        user_id=request.session['user']
        user_obj=login.objects.get(id=user_id)

        old=request.POST['curr_pass']
        new=request.POST['new_pass']

        if old==user_obj.password:
            user_obj.password=new
            user_obj.save()
            return render(request,'changepass.html',{"mssg1":"Password Changed"})
        else:
            return render(request,'changepass.html',{"mssg2":"Password cant change"})
            
        

    except Exception as e:
        print(e)
    return render(request,'changepass.html')




def profile(request):
    try:
        getvalues=request.session['user']
        userObj=login.objects.get(id=getvalues)
        print(userObj)
        objUser=signupp.objects.get(id=userObj.user_id_id)
       
        return render(request,'profile.html',{"user1":objUser,"userlogin":userObj})
    
    except Exception as e:
        print(e)
    return render(request,'profile.html')