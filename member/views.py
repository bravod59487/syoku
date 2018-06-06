from django.shortcuts import render,redirect
from .models import Member
from django.http import HttpResponse
import datetime
import json

import smtplib  #send email

from member import models

# Create your views here.
def index(request):  
    # title = "會員管理"
    # 會員資料傳給 index.html
    # members=Member.objects.all()
    # return render(request,'member/index.html',locals())

    if request.method == 'POST':
        try:
            useremail = request.POST['useremail']
            password = request.POST['password']
            member = Member.objects.filter(useremail=useremail,password=password)
            memberid=member[0].id

        except:
            response = HttpResponse("<script>alert('輸入錯誤');location.href='/member/' </script>")
            return response
        else:
            return redirect("/member/update/%s" %(memberid))

    return render(request,'member/index.html',locals()) 



def home(request):  
    
    return render(request,'member/home.html',locals())


def create(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        userphone = request.POST["userphone"]
        useremail = request.POST["useremail"]
        userbirth = request.POST["userbirth"]
        useraddress = request.POST["useraddress"]
        usergender = request.POST["usergender"]
        

        # email是否已在mysql
        same_email_user = Member.objects.filter(useremail=useremail)
        if same_email_user:  
            response = HttpResponse("<script>alert('email已註冊，請登入or使用其他email註冊！');location.href='/member/create' </script>")
            return response
        

        else:
        # 會員資料寫進資料庫
            Member.objects.create(username=username,password=password,userphone=userphone,useremail=useremail,userbirth=userbirth,useraddress=useraddress,usergender=usergender)
            response = HttpResponse("<script>alert('註冊成功 請登入！');location.href='/member/login' </script>")
            return response



    member = Member.objects.all().values('useremail')
   
    lll = []
    # print(member)
    # 上面的值為 <QuerySet [{'useremail': 'Ann@gmail.com'}, {'useremail': 'Betty@gmail.com'}, {'useremail': 'Cindy@gmail.com'}, {'useremail': 'Hank@gmail.com'}, {'useremail': 'Tom@gmail.com'}, {'useremail': 'John@gmail.com'}, {'useremail': 'xxx@gmail.com'}]>
    for i in member:
        x = i['useremail']
        lll.append(x)
    # print(lll)
    # 上面的值為 ['Ann@gmail.com', 'Betty@gmail.com', 'Cindy@gmail.com', 'Hank@gmail.com', 'Tom@gmail.com', 'John@gmail.com', 'xxx@gmail.com']

    # 為了傳進去js裡面還是LIST
    List=json.dumps(lll)
    


    # title = "會員新增" 
    return render(request,'member/create.html',locals())


def update(request,id):
    if request.method == 'POST':        
        username = request.POST["username"]  
        password = request.POST["password"]    
        useremail = request.POST["useremail"]
        userbirth = request.POST["userbirth"] 
        useraddress = request.POST["useraddress"]

        # 修改資料庫中的會員資料
        member = Member.objects.get(id=int(id))
        member.username = username
        member.password = password
        member.usermail = useremail
        member.userbirth = userbirth
        member.useraddress = useraddress
        
        member.save()

        # return redirect('/member/login')
        response = HttpResponse("<script>alert('修改完成');location.href='/'</script>")
        return response

    # 根據會員編號取得會員資料傳給update.html
    member = Member.objects.get(id=int(id))
    return render(request,'member/update.html',locals())



def delete(request,id):
    # 會員編號刪除會員資料
    member = Member.objects.get(id=int(id))
    member.delete()

    return redirect('/member')


def login(request):    
    # title = "會員登入"
    if request.method == 'POST':
        email = request.POST['useremail']
        pwd = request.POST['userpassword']

        member = Member.objects.filter(useremail=email,password=pwd).values('username','useremail')
        if member:
            # print(member[0])
            response = HttpResponse("<script>alert('登入成功');location.href='/' </script>")
            response.set_cookie("uid",member[0]['useremail'])
                
            # if 'rememberme'in request.POST:
            #     expiresdate = datetime.datetime.now() + datetime.timedelta(days=7)
            #     response.set_cookie("name",member[0]['username'],expires = expiresdate)
            # else:
            #     response.set_cookie("name",member[0]['username'])
                
        else:
            # print("not found")
            response = HttpResponse("<script>alert('登入失敗');location.href='/member/login' </script>")
        return response

    return render(request,'member/login.html',locals())


def logout(request):
    response = HttpResponse("<script>alert('會員登出成功');location.href='/member/login'</script>")
    response.delete_cookie('uid')
    return response


def forgetpwd(request):
    if request.method == 'POST':
        try:
            useremail = request.POST['useremail']
            members = Member.objects.all()
            member = Member.objects.filter(useremail = useremail).values('useremail')
            member2 = Member.objects.filter(useremail = useremail).values('password')
            memberemail = member[0]['useremail']
            memberpwd = member2[0]['password']
            # memberid=member[0].id
            # return redirect("/member/resetpwd/%s" %(memberid))
        except:
            response = HttpResponse("<script>alert('無此信箱');location.href='/member/forgetpwd' </script>")
            return response
        else:

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("syoku03company@gmail.com", "ssyyookkuu03")

            msg = memberpwd
            server.sendmail("syoku03company@gmail.com", memberemail,msg)
            server.quit()
            return redirect("/member/login")
        

    return render(request,'member/forgetpwd.html',locals()) 


def resetpwd(request,id):
    if request.method == 'POST':

        password = request.POST["password"]      
        password2 = request.POST["password2"]

        if password == password2:        
            

        # 修改資料庫中的會員資料
            member = Member.objects.get(id=int(id))
            member.password = password
    
            member.save()

            return redirect('/member/login')
        else:
            response = HttpResponse("<script>alert('密碼不同');location.href='./%s' </script>" %(id))
            return response


    member = Member.objects.get(id=int(id))
    return render(request,'member/resetpwd.html',locals())


