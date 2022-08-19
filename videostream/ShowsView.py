from django.shortcuts import render
from . import pool
import os
import time
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def ShowsInterface(request):
    return render(request,"showsInterface.html")

@xframe_options_exempt
def SubmitShows(request):
    try:
        db,cmd=pool.ConnectionPooling()
        categoryid=request.POST["categoryid"]
        showname = request.POST["showname"]
        type = request.POST["type"]
        description = request.POST["description"]
        year = request.POST["year"]
        rating = request.POST["rating"]
        artist = request.POST["artist"]
        status = request.POST["status"]
        showstatus = request.POST["showstatus"]
        episodes = request.POST["episodes"]
        poster=request.FILES["poster"]
        trailerurl = request.FILES["trailerurl"]
        videourl = request.FILES["videourl"]
        poster2 = request.FILES["poster2"]
        q="insert into shows(categoryid,showname,type,description,year,rating,artist,status,showstatus,episodes,poster,trailerurl,videourl,poster2) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}')".format(categoryid,showname,type,description,year,rating,artist,status,showstatus,episodes,poster.name,trailerurl.name,videourl.name,poster2.name)
        cmd.execute(q)
        db.commit()
        F=open("D:/VideoStream/assets/"+poster.name,"wb")
        for chunk in poster.chunks():
            F.write(chunk)
        F.close()
        F=open("D:/VideoStream/assets/" + trailerurl.name, "wb")
        for chunk in trailerurl.chunks():
            F.write(chunk)
        F.close()
        F=open("D:/VideoStream/assets/" + videourl.name, "wb")
        for chunk in videourl.chunks():
            F.write(chunk)
        F.close()
        F = open("D:/VideoStream/assets/" + poster2.name, "wb")
        for chunk in poster2.chunks():
            F.write(chunk)
        F.close()
        db.close()
        return render(request, "showsInterface.html", {'status': True})

    except Exception as e:
        print("errrr", e)
        return render(request, "showsInterface.html", {'status': False})

@xframe_options_exempt
def DisplayShows(request):
    try:
        db, cmd = pool.ConnectionPooling()
        q="select S.*,(select C.categoryname from category C where C.categoryid=S.categoryid) from shows S"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"displayAllShows.html",{'rows':rows})
    except Exception as e:
        print("errrrrrrrrr", e)
        return render(request,"displayAllShows.html",{'rows': []})

@xframe_options_exempt
def ShowById(request):
    try:
        sid=request.GET['sid']
        db, cmd = pool.ConnectionPooling()
        q="select S.*,(select C.categoryname from category C where C.categoryid=S.categoryid) from shows S where S.showid='{}'".format(sid)
        cmd.execute(q)
        row = cmd.fetchone()
        db.close()
        return render(request, "ShowById.html", {'row': row})
    except Exception as e:
        print("errrrrrrrrr", e)
        return render(request, "ShowById.html", {'row': []})

@xframe_options_exempt
def EditDeleteShowData(request):
    try:
        db, cmd = pool.ConnectionPooling()
        btn=request.GET['btn']
        if(btn=="Edit"):
            categoryid=request.GET["categoryid"]
            showid = request.GET["showid"]
            showname = request.GET["showname"]
            type = request.GET["type"]
            description = request.GET["description"]
            year = request.GET["year"]
            rating = request.GET["rating"]
            artist = request.GET["artist"]
            status = request.GET["status"]
            showstatus = request.GET["showstatus"]
            episodes = request.GET["episodes"]
            q="update shows set categoryid='{}',showname='{}',type='{}',description='{}',year='{}',rating='{}',artist='{}',status='{}',showstatus='{}',episodes='{}' where showid='{}'".format(categoryid,showname,type,description,year,rating,artist,status,showstatus,episodes,showid)
            cmd.execute(q)
            db.commit()
        elif(btn=="Delete"):
            showid = request.GET["showid"]
            q="delete from shows where showid='{}'".format(showid)
            cmd.execute(q)
            db.commit()
        # time.sleep(5)
        # return DisplayShows(request)
        return render(request, "ShowById.html", {'status': True})
    except Exception as e:
        print("errrr", e)
        return render(request, "ShowById.html", {'status': False})

@xframe_options_exempt
def EditPosterurl(request):
    try:
        db,cmd=pool.ConnectionPooling()
        showid=request.POST['showid']
        filename1=request.POST['filename1']
        poster=request.FILES["poster"]

        q="update shows set poster='{}' where showid='{}'".format(poster.name,showid)
        cmd.execute(q)
        db.commit()
        F=open("D:/VideoStream/assets/"+poster.name,"wb")
        for chunk in poster.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/" + filename1)
        db.close()

        return render(request, "ShowById.html", {'status': True})

    except Exception as e:
        print("er", e)
        return render(request, "ShowById.html", {'status': False})

@xframe_options_exempt
def EditTrailerurl(request):
    try:
        db,cmd=pool.ConnectionPooling()
        showid=request.POST['showid']
        filename2=request.POST['filename2']
        trailerurl = request.FILES["trailerurl"]
        q="update shows set trailerurl='{}' where showid='{}'".format(trailerurl.name,showid)
        cmd.execute(q)
        db.commit()
        F = open("D:/VideoStream/assets/" + trailerurl.name, "wb")
        for chunk in trailerurl.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/" + filename2)
        db.close()
        return render(request, "ShowById.html", {'status': True})

    except Exception as e:
        print("errrr", e)
        return render(request, "ShowById.html", {'status': False})

@xframe_options_exempt
def EditVideourl(request):
    try:
        db,cmd=pool.ConnectionPooling()
        showid=request.POST['showid']
        filename3=request.POST['filename3']
        videourl = request.FILES["videourl"]

        q="update shows set videourl='{}' where showid='{}'".format(videourl.name,showid)
        cmd.execute(q)
        db.commit()
        F = open("D:/VideoStream/assets/" + videourl.name, "wb")
        for chunk in videourl.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/" + filename3)
        db.close()

        return render(request, "ShowById.html", {'status': True})

    except Exception as e:
        print("errrrrrrr  ", e)
        return render(request, "ShowById.html", {'status': False})

@xframe_options_exempt
def EditPoster2url(request):
    try:
        db,cmd=pool.ConnectionPooling()
        showid=request.POST['showid']
        filename4=request.POST['filename4']
        poster2=request.FILES["poster2"]

        q="update shows set poster2='{}' where showid='{}'".format(poster2.name,showid)
        cmd.execute(q)
        db.commit()
        F=open("D:/VideoStream/assets/"+poster2.name,"wb")
        for chunk in poster2.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/" + filename4)
        db.close()

        return render(request, "ShowById.html", {'status': True})

    except Exception as e:
        print("er", e)
        return render(request, "ShowById.html", {'status': False})


@xframe_options_exempt
def DisplayAllShowJSON(request):
    try:
        cid=request.GET['cid']
        db, cmd = pool.ConnectionPooling()
        q="select * from shows where categoryid='{}'".format(cid)
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print("err:",e)
        return JsonResponse([],safe=False)