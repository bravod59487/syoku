from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .models import Storemenu
from django.http import HttpResponse

# Create your views here.
def index(request):
    title = "菜單管理"
    #todo 讀取會員資料傳給index.html
    storemenu = Storemenu.objects.all()
    return render(request,'storemenu/index.html',locals())

def create(request):
    if 'Company_email' in request.COOKIES:
        if request.method == 'POST' and request.FILES["cimg"]:
            myfile = request.FILES['cimg']
            fs = FileSystemStorage()
            fs.save(myfile.name,myfile)

            Company_email =request.COOKIES['Company_email']
            cimg = myfile.name
            # cimg = request.POST["cimg"] #美食圖片
            cname = request.POST["cname"] #美食名稱
            ctype = request.POST["ctype"] #美食類型
            ccal = request.POST["ccal"] #美食熱量
            cprice = request.POST["cprice"] #美食價錢
            cintroduction = request.POST["cintroduction"] #美食介紹

            Storemenu.objects.create(cname=cname,ctype=ctype,cimg=cimg,ccal=ccal,cprice=cprice,cintroduction=cintroduction,Company_email=Company_email)
            return redirect ("/storemenu/userindex")

        title = "菜單新增" 
        return render(request,'storemenu/create.html',locals())
    else:
        return HttpResponse ("<script>alert('請先登入');location.href='/jabo/login'</script>") 


def update(request,id):
    if 'Company_email' in request.COOKIES:
        if request.method == 'POST':        
            cname = request.POST["cname"] #美食名稱
            ctype = request.POST["ctype"] #美食類型
            ccal = request.POST["ccal"] #美食熱量
            cprice = request.POST["cprice"] #美食價錢
            cintroduction = request.POST["cintroduction"] #美食介紹
            # Company_email =request.COOKIES['Company_email']#廠商email

            storemenu = Storemenu.objects.get(id = int(id))
            try:
                request.FILES["cimg"]
            except:
                pass
            else:
                myfile = request.FILES['cimg']
                fs = FileSystemStorage()
                fs.save(myfile.name,myfile)
                # cimg = request.POST["cimg"] #美食圖片
                storemenu.cimg = (myfile.name)      

            storemenu.cname = cname
            storemenu.ctype = ctype
            storemenu.ccal = ccal
            storemenu.cprice = cprice
            storemenu.cintroduction = cintroduction 

            storemenu.save()
            return redirect('/storemenu/userindex')
        Company_email =request.COOKIES['Company_email']
        title = "菜單修改"
        storemenu = Storemenu.objects.filter(Company_email=Company_email,id = int(id)).values('id','cname','ctype','ccal','cprice','cintroduction','cimg')
        storemenu =storemenu[0]
        # storemenu = Storemenu.objects.get(id = int(id))
        # print(storemenu[0])
        return render(request,'storemenu/update.html',locals())
    else:
        return HttpResponse ("<script>alert('請先登入');location.href='/jabo/login'</script>") 
def delete(request,id):
    if 'Company_email' in request.COOKIES:
        Company_email =request.COOKIES['Company_email']
        storemenu = Storemenu.objects.filter(Company_email=Company_email,id = int(id))
        storemenu.delete()
        return redirect('/storemenu/userindex')
    else:
        return HttpResponse ("<script>alert('請先登入');location.href='/jabo/login'</script>") 

def userindex(request):
        # 如果cookie裡面沒有name的存在 就會跳回登入頁面  
    if 'Company_email' in request.COOKIES:
        title = "菜單管理"
        Company_email =request.COOKIES['Company_email']
        storemenu = Storemenu.objects.filter(Company_email=Company_email).values('id','cname','ctype','ccal','cprice','cintroduction','cimg')
        # print(len(userall))
        # userall = Member.objects.all()
        return render(request,'storemenu/userindex.html',locals())
    else:
        return HttpResponse ("<script>alert('請先登入');location.href='/jabo/login'</script>") 
        # return redirect("/member/login")name




