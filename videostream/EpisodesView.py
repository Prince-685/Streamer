from django.shortcuts import render
from . import pool
import time
import os
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def EpisodesInterface(request):
    return render(request,"EpisodesInterface.html")

@xframe_options_exempt
def SubmitEpisodes(request):
    try:
        db, cmd = pool.ConnectionPooling()
        categoryid=request.POST['categoryid']
        showid = request.POST['showid']
        episodeno = request.POST['episodeno']
        description = request.POST['description']
        poster=request.FILES['poster']
        trailer = request.FILES['trailer']
        video = request.FILES['video']
        q="insert into episodes (categoryid,showid,episodeno,description,poster,trailer,video) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(categoryid,showid,episodeno,description,poster.name,trailer.name,video.name)
        cmd.execute(q)
        db.commit()
        F = open("D:/VideoStream/assets/" + poster.name, "wb")  # wb(write bytes)
        for chunk in poster.chunks():
            F.write(chunk)
        F.close()
        F = open("D:/VideoStream/assets/" + trailer.name, "wb")  # wb(write bytes)
        for chunk in trailer.chunks():
            F.write(chunk)
        F.close()
        F = open("D:/VideoStream/assets/" + video.name, "wb")  # wb(write bytes)
        for chunk in video.chunks():
            F.write(chunk)
        F.close()
        db.close()
        return render(request, "EpisodesInterface.html", {'status': True})

    except Exception as e:
        print("errrrrrrrrr", e)
        return render(request, "EpisodesInterface.html", {'status': False})

@xframe_options_exempt
def DisplayAllEpisodes(request):
    try:
        db,cmd=pool.ConnectionPooling()
        q="select E.*,(select C.categoryname from category C where C.categoryid=E.categoryid) from episodes E"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"DisplayAllEpisodes.html", {'rows': rows})

    except Exception as e:
        print("err:", e)
        return render(request, "DisplayAllEpisodes.html", {'rows': []})

@xframe_options_exempt
def EpisodeById(request):
    try:
        eid=request.GET['eid']
        db, cmd = pool.ConnectionPooling()
        q = "select E.*,(select C.categoryname from category C where C.categoryid=E.categoryid),(select S.showname from shows S where S.showid=E.showid) from episodes E where episodeid='{}'".format(eid)
        cmd.execute(q)
        row = cmd.fetchone()

        db.close()
        return render(request, "EpisodeById.html", {'row': row})
    except Exception as e:
        print("errrrrrrrrr", e)
        return render(request, "EpisodeById.html", {'row': []})

@xframe_options_exempt
def EditDeleteEpisodeData(request):
    try:
        db, cmd = pool.ConnectionPooling()
        btn=request.GET['btn']
        if(btn=="Edit"):
            categoryid=request.GET["categoryid"]
            showid = request.GET["showid"]
            episodeid = request.GET["episodeid"]
            episodeno = request.GET["episodeno"]
            description = request.GET['description']
            q="update shows set categoryid='{}',showid='{}',episodeno='{}',description='{}' where episodeid='{}'".format(categoryid,showid,episodeno,description,episodeid)
            cmd.execute(q)
            db.commit()
        elif(btn=="Delete"):
            episodeid = request.GET["episodeid"]
            q="delete from shows where episodeid='{}'".format(episodeid)
            cmd.execute(q)
            db.commit()
        time.sleep(5)
        return DisplayAllEpisodes(request)
        #return render(request, "EpisodeById.html", {'status': True})
    except Exception as e:
        print("errrr", e)
        return render(request, "EpisodeById.html", {'status': False})

@xframe_options_exempt
def EditPoster(request):
    try:
        db,cmd=pool.ConnectionPooling()
        episodeid=request.POST['episodeid']
        filename1=request.POST['filename1']
        poster=request.FILES["poster"]

        q="update shows set poster='{}' where episodeid='{}'".format(poster.name,episodeid)
        cmd.execute(q)
        db.commit()
        F=open("D:/VideoStream/assets/"+poster.name,"wb")
        for chunk in poster.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/" + filename1)
        db.close()

        return render(request, "EpisodeById.html", {'status': True})

    except Exception as e:
        print("er", e)
        return render(request, "EpisodeById.html", {'status': False})

@xframe_options_exempt
def EditTrailer(request):
    try:
        db,cmd=pool.ConnectionPooling()
        episodeid=request.POST['episodeid']
        filename2=request.POST['filename2']
        trailer = request.FILES["trailer"]
        q="update shows set trailerurl='{}' where episodeid='{}'".format(trailer.name,episodeid)
        cmd.execute(q)
        db.commit()
        F = open("D:/VideoStream/assets/" + trailer.name, "wb")
        for chunk in trailer.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/" + filename2)
        db.close()
        return render(request, "EpisodeById.html", {'status': True})

    except Exception as e:
        print("errrr", e)
        return render(request, "EpisodeById.html", {'status': False})

@xframe_options_exempt
def EditVideo(request):
    try:
        db,cmd=pool.ConnectionPooling()
        episodeid=request.POST['episodeid']
        filename3=request.POST['filename3']
        video= request.FILES["video"]

        q="update shows set video='{}' where episodeid='{}'".format(video.name,episodeid)
        cmd.execute(q)
        db.commit()
        F = open("D:/VideoStream/assets/" + video.name, "wb")
        for chunk in video.chunks():
            F.write(chunk)
        F.close()
        os.remove("D:/VideoStream/assets/" + filename3)
        db.close()

        return render(request, "EpisodeById.html", {'status': True})

    except Exception as e:
        print("errrrrrrr  ", e)
        return render(request, "EpisodeById.html", {'status': False})
