from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .models import Recipe
from member.models import Member
from django.http import HttpResponse
import datetime
import json
import random
import string
from django.db.models import Q

def index(request):
    #取出recipe資料庫所有資料
    recipes=Recipe.objects.all()
    return render(request,'recipe/index.html',locals())

def search(request): 
    #判斷搜取得尋關鍵字
    if request.method == 'GET':      
        srhkey =  request.GET.get('search')       
         
        try:
            recipes = Recipe.objects.filter(Q(recfood__contains=srhkey) | Q(recname__contains=srhkey)) 
        except: 
            recipes=Recipe.objects.all()
            return render(request,'recipe/index.html',locals())
        else:
            return render(request,'recipe/search.html',locals())

def userrecipe(request):
    
    if 'uid' in request.COOKIES:
        user = request.COOKIES['uid']
        recipes=Recipe.objects.filter(userid=user)
    else:
        response = HttpResponse("<script>alert('請先登入');location.href='/member/login'</script>")
        return response
    return render(request,'recipe/userrecipe.html',locals())

def showrecipe(request,id):


   
    recipe=Recipe.objects.get(recid=int(id))
    fodlist = json.loads(recipe.recfood)
    stplist = json.loads(recipe.recstep)
    print(recipe.userid)
    member=Member.objects.get(useremail=recipe.userid)
    print(member.useremail)


    return render(request,'recipe/showrecipe.html',locals())

def create(request):

    if 'uid' in request.COOKIES:
        user = request.COOKIES['uid']
    
        cooktimelist = [10,20,30,45,60,90,120]
        portionlist = [1,2,3,4,5,6,7,8,9,10]
        
        if request.method == 'POST' and request.FILES['recCover']:

            userId = user
            recName = request.POST["recName"]

            myfile = request.FILES['recCover']
            fs = FileSystemStorage()
            filename = userId[0:3]
            rd = str(random.randint(0,9999))
            recCoverName="rec_"+filename+"_"+recName+rd+".jpg"
            fs.save(recCoverName,myfile)
                        
            recDesc = request.POST["recDesc"]
            recTime = request.POST["recTime"]
            recPortion = request.POST["recPortion"]
            recCal = request.POST["recCal"]
            recVegan = request.POST["recVegan"]
            recFood = request.POST["recFood"]
            recStep = request.POST["recStep"]
                 
            Recipe.objects.create(userid=userId,recname=recName,reccover=recCoverName,recdesc=recDesc,rectime=recTime,recportion=recPortion,reccal=recCal,recvegan=recVegan,recfood=recFood,recstep=recStep)
         
            return redirect('/recipe/userrecipe')
        
        return render(request,'recipe/create.html',locals())
    
    else:
        response = HttpResponse("<script>alert('請先登入');location.href='/member/login'</script>")
        return response

def update(request,id):

    if 'uid' in request.COOKIES:
        
        user = request.COOKIES['uid']
       
        
        cooktimelist = [10,20,30,45,60,90,120]
        portionlist = [1,2,3,4,5,6,7,8,9,10]
        veganlist = ["葷食","蛋奶素","素食"]
        
        recipe=Recipe.objects.get(recid=int(id))
        fodlist = json.loads(recipe.recfood)
        stplist = json.loads(recipe.recstep)
        

        if request.method == 'POST':  
            userId = user      
            recName = request.POST["recName"]  
            
            try:
                request.FILES['recCover']
            except:
                pass
            else:
                myfile = request.FILES['recCover']        
                fs = FileSystemStorage()
                filename = userId[0:3]
                rd = str(random.randint(0,9999))
                recCoverName="rec_"+filename+"_"+recName+rd+".jpg"
                fs.save(recCoverName,myfile)
                recipe.reccover=recCoverName
                

            recDesc = request.POST["recDesc"]
            recTime = request.POST["recTime"]
            recPortion = request.POST["recPortion"]
            recCal = request.POST["recCal"]
            recVegan = request.POST["recVegan"]
            recFood = request.POST["recFood"]
            recStep = request.POST["recStep"]    

            recipe.recname=recName
            
            recipe.recdesc=recDesc
            recipe.rectime=recTime
            recipe.recportion=recPortion
            recipe.reccal=recCal
            recipe.recvegan=recVegan
            recipe.recfood=recFood
            recipe.recstep=recStep

            recipe.save()
            return redirect('/recipe/userrecipe')
            
        return render(request,'recipe/update.html',locals())

    else:
        response = HttpResponse("<script>alert('請先登入');location.href='/member/login'</script>")
        return response
    
    

def delete(request,id):

    if 'uid' in request.COOKIES:
        user = request.COOKIES['uid']
        recipes=Recipe.objects.filter(userid=user)

        recipe=Recipe.objects.get(recid=int(id))
        recipe.delete()
        
        return redirect('/recipe/userrecipe')
    
    else:
        response = HttpResponse("<script>alert('請先登入');location.href='/member/login'</script>")
        return response