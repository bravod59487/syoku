import requests

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from .models import Comment,Plan
from .forms import CommentForm
from storemenu.models import Storemenu
from recipe.models import Recipe

# Create your views here.


def index(request):
    if request.method =='POST':
        if 'uid' in request.COOKIES:
            useremail = request.COOKIES["uid"]
            mon1 = request.POST["1-1"]
            mon2 = request.POST["1-2"]
            mon3 = request.POST["1-3"]
            tue1 = request.POST["2-1"]
            tue2 = request.POST["2-2"]
            tue3 = request.POST["2-3"]
            wed1 = request.POST["3-1"]
            wed2 = request.POST["3-2"]
            wed3 = request.POST["3-3"]
            thu1 = request.POST["4-1"]
            thu2 = request.POST["4-2"]
            thu3 = request.POST["4-3"]
            fri1 = request.POST["5-1"]
            fri2 = request.POST["5-2"]
            fri3 = request.POST["5-3"]
            sat1 = request.POST["6-1"]
            sat2 = request.POST["6-2"]
            sat3 = request.POST["6-3"]
            sun1 = request.POST["7-1"]
            sun2 = request.POST["7-2"]
            sun3 = request.POST["7-3"]
            title = request.POST["title"]
            
            # 新增資料進DB
            Plan.objects.create(
            useremail=useremail,
            title=title,
            mon1=mon1,mon2=mon2,mon3=mon3,
            tue1=tue1,tue2=tue2,tue3=tue3,
            wed1=wed1,wed2=wed2,wed3=wed3,
            thu1=thu1,thu2=thu2,thu3=thu3,
            fri1=fri1,fri2=fri2,fri3=fri3,
            sat1=sat1,sat2=sat2,sat3=sat3,
            sun1=sun1,sun2=sun2,sun3=sun3)
            response = HttpResponse("<script>alert('儲存成功');location.href='/'</script>")
            return response
        
        else:
            response = HttpResponse("<script>alert('請先登入');location.href='/member/login'</script>")
            return response

    storemenu = Storemenu.objects.all()
    recipes   = Recipe.objects.all()
    return render(request, 'gary/index.html', locals())


def comments(request):
    comments_list = Comment.objects.order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''

            if result['success']:
                form.save()
                messages.success(request, 'New comment added with success!')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            return redirect('gary/comments')
    else:
        form = CommentForm()

    return render(request, 'gary/comments.html', {'comments': comments_list, 'form': form})


def login(request):
    return render(request, 'gary/login.html')


def history(request):
    
    usercook = request.COOKIES['uid']

    history = Plan.objects.filter(useremail=usercook)


    return render(request, 'gary/history.html',locals())


def historydata(request,id):
    
    
    history = Plan.objects.filter(id=int(id))
    
    
    for historys in history:
        if historys.mon1:
            a=historys.mon1.split(']')[1]
            b=historys.mon1.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)

                        img_gary_mon1 = storemenuss.cimg
                        
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)

                        img_gary_mon1 = recipess.reccover
        else:
            img_gary_mon1 = "blank.jpg"
    for historys in history:
        if historys.mon2:
            a=historys.mon2.split(']')[1]
            b=historys.mon2.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_mon2 = storemenuss.cimg
                        
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_mon2 = recipess.reccover
        else:
            img_gary_mon2 = "blank.jpg"
            
    for historys in history:
        if historys.mon3:
            a=historys.mon3.split(']')[1]
            b=historys.mon3.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_mon3 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_mon3 = recipess.reccover
        else:
            img_gary_mon3 = "blank.jpg"
            
    for historys in history:
        if historys.tue1:
            a=historys.tue1.split(']')[1]
            b=historys.tue1.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_tue1 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_tue1 = recipess.reccover
        else:
            
            img_gary_tue1 = "blank.jpg"
    for historys in history:
        if historys.tue2:
            a=historys.tue2.split(']')[1]
            b=historys.tue2.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_tue2 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_tue2 = recipess.reccover

        else:
            
            img_gary_tue2 = "blank.jpg"
    for historys in history:
        if historys.tue3:
            a=historys.tue3.split(']')[1]
            b=historys.tue3.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_tue3 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_tue3 = recipess.reccover
        else:
            img_gary_tue3 = "blank.jpg"
    for historys in history:
        if historys.wed1:
            a=historys.wed1.split(']')[1]
            b=historys.wed1.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_wed1 = storemenuss.cimg

            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_wed1 = recipess.reccover
        else:
            img_gary_wed1 = "blank.jpg"
    for historys in history:
        if historys.wed2:
            a=historys.wed2.split(']')[1]
            b=historys.wed2.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_wed2 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_wed2 = recipess.reccover
        else:
            img_gary_wed2 = "blank.jpg"
    for historys in history:
        if historys.wed3:
            a=historys.wed3.split(']')[1]
            b=historys.wed3.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_wed3 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_wed3 = recipess.reccover
        else:
            img_gary_wed3 = "blank.jpg"
    for historys in history:
        if historys.thu1:
            a=historys.thu1.split(']')[1]
            b=historys.thu1.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_thu1 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_thu1 = recipess.reccover
        else:
            img_gary_thu1 = "blank.jpg"
    for historys in history:
        if historys.thu2:
            a=historys.thu2.split(']')[1]
            b=historys.thu2.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_thu2 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_thu2 = recipess.reccover
        else:
            img_gary_thu2 = "blank.jpg"
    for historys in history:
        if historys.thu3:
            a=historys.thu3.split(']')[1]
            b=historys.thu3.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_thu3 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_thu3 = recipess.reccover
        else:
            img_gary_thu3 = "blank.jpg"
    for historys in history:
        if historys.fri1:
            a=historys.fri1.split(']')[1]
            b=historys.fri1.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_fri1 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_fri1 = recipess.reccover
        else:
            img_gary_fri1 = "blank.jpg"
    for historys in history:
        if historys.fri2:
            a=historys.fri2.split(']')[1]
            b=historys.fri2.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_fri2 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_fri2 = recipess.reccover
        else:
            img_gary_fri2 = "blank.jpg"
    for historys in history:
        if historys.fri3:
            a=historys.fri3.split(']')[1]
            b=historys.fri3.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_fri3 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_fri3 = recipess.reccover
        else:
            img_gary_fri3 = "blank.jpg"
    for historys in history:
        if historys.sat1:
            a=historys.sat1.split(']')[1]
            b=historys.sat1.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_sat1 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_sat1 = recipess.reccover
        else:
            img_gary_sat1 = "blank.jpg"
    for historys in history:
        if historys.sat2:
            a=historys.sat2.split(']')[1]
            b=historys.sat2.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_sat2 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_sat2 = recipess.reccover
        else:
            img_gary_sat2 = "blank.jpg"
    for historys in history:
        if historys.sat3:
            a=historys.sat3.split(']')[1]
            b=historys.sat3.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_sat3 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_sat3 = recipess.reccover
        else:
            img_gary_sat3 = "blank.jpg"

    for historys in history:
        if historys.sun1:
            a=historys.sun1.split(']')[1]
            b=historys.sun1.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_sun1 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_sun1 = recipess.reccover
        else:
            img_gary_sun1 = "blank.jpg"
    for historys in history:
        if historys.sun2:
            a=historys.sun2.split(']')[1]
            b=historys.sun2.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_sun2 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_sun2 = recipess.reccover
        else:
            img_gary_sun2 = "blank.jpg"
    for historys in history:
        if historys.sun3:
            a=historys.sun3.split(']')[1]
            b=historys.sun3.split(']')[0]
            c=b.split('[')[1]
            print(c)
            print(a)
            if c == "店家":
                storemenus = Storemenu.objects.all()
                for storemenuss in storemenus:
                    if a == storemenuss.cname:
                        print(storemenuss.cimg)
                        img_gary_sun3 = storemenuss.cimg
            elif c == "食譜":
                recipes = Recipe.objects.all()
                for recipess in recipes:
                    if a == recipess.recname:
                        print(recipess.reccover)
                        img_gary_sun3 = recipess.reccover
        else:
            img_gary_sun3 = "blank.jpg"



    return render(request, 'gary/historydata.html',locals())

def delete(request,id):
    
    #todo 根據會員編號刪除會員資料
    history = Plan.objects.get(id=int(id))
    history.delete()
    
    #todo 刪除完成後轉到http://localhost:8000/member
    return redirect('/history')
