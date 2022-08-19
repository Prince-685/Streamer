from django.shortcuts import render
from . import pool
import os
import time
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def CategoryInterface(request):
    return render(request,"CategoryInterface.html")

@xframe_options_exempt
def SubmitCategory(request):
 try:
    db,cmd=pool.ConnectionPooling()

    categoryname = request.POST['categoryname']
    description= request.POST['description']
    icon = request.FILES['icon']
    q="insert into category (categoryname,description,icon) values('{0}','{1}','{2}')".format(categoryname,description,icon.name)
    cmd.execute(q)
    db.commit()
    F=open("D:/VideoStream/assets/"+icon.name,"wb") # wb(write bytes)
    for chunk in icon.chunks():
        F.write(chunk)
    F.close()
    db.close()
    return render(request, "CategoryInterface.html",{'status':True})
 except Exception as e:
     print("errrrrrrrrr",e)
     return render(request, "CategoryInterface.html", {'status': False})

@xframe_options_exempt
def DisplayAll(request):
    try:
        db, cmd = pool.ConnectionPooling()
        q="select * from category"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"DisplayAllCategories.html",{'rows':rows})
    except Exception as e:
        print("err:",e)
        return render(request, "DisplayAllCategories.html", {'rows': []})

@xframe_options_exempt
def CategoryById(request):
    try:
        cid=request.GET['cid']
        db, cmd = pool.ConnectionPooling()
        q="select * from category where categoryid='{}'".format(cid)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return render(request,"CategoryById.html",{'row':row})
    except Exception as e:
        print("err:",e)
        return render(request,"CategoryById.html", {'row': []})

@xframe_options_exempt
def EditDeleteCategoryData(request):
    try:
        btn=request.GET['btn']
        db, cmd = pool.ConnectionPooling()
        if(btn=="Edit"):
            categoryid=request.GET['categoryid']
            categoryname=request.GET['categoryname']
            description = request.GET['description']
            q="update category set categoryname='{}' , description='{}' where categoryid='{}'".format(categoryname,description,categoryid)
            cmd.execute(q)
            db.commit()
            db.close()
        elif(btn=="Delete"):
            categoryid = request.GET['categoryid']
            q = "delete from category where categoryid='{}'".format(categoryid)
            cmd.execute(q)
            db.commit()
            db.close()
        time.sleep(5)
        return DisplayAll(request)
        #return render(request,"CategoryById.html",{'status':True})
    except Exception as e:
        print("err:",e)
        return render(request, "CategoryById.html", {'status':False})

@xframe_options_exempt
def EditIcon(request):
     try:
        db,cmd=pool.ConnectionPooling()
        categoryid = request.POST['categoryid']
        filename = request.POST['filename']
        icon = request.FILES['icon']
        q="update category set icon='{}' where categoryid='{}'".format(icon.name,categoryid)
        cmd.execute(q)
        db.commit()
        F=open("D:/VideoStream/assets/"+icon.name,"wb") # wb(write bytes)
        for chunk in icon.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/"+filename)
        db.close()
        time.sleep(5)
        return DisplayAll(request)
        #return render(request, "CategoryById.html",{'status':True})
     except Exception as e:
         print("errrrrrrrrr",e)
     return render(request, "CategoryById.html", {'status': False})

@xframe_options_exempt
def DisplayAllJSON(request):
    try:
        db, cmd = pool.ConnectionPooling()
        q="select * from category"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print("err:",e)
        return JsonResponse([],safe=False)