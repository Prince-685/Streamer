from django.shortcuts import render
from . import pool
from django.http import JsonResponse

def HindiMovies(request):
    try:
        db, cmd = pool.ConnectionPooling()
        q = "select * from shows where categoryid in(select categoryid from category where categoryname='Hindi Movies')"
        cmd.execute(q)
        hmovies = cmd.fetchall()
        db.close()
        return render(request,"HindiMovies.html",{'hmovies':hmovies})
    except Exception as e:
        print("errr:",e)


def EnglishMovies(request):
    try:
        db, cmd = pool.ConnectionPooling()
        q = "select * from shows where categoryid in(select categoryid from category where categoryname='English Movies')"
        cmd.execute(q)
        emovies = cmd.fetchall()
        db.close()
        return render(request,"EnglishMovies.html",{'emovies':emovies})
    except Exception as e:
        print("errr:",e)

def Webseries(request):
    try:
        db, cmd = pool.ConnectionPooling()
        q = "select * from shows where categoryid in(select categoryid from category where categoryname='Webseries')"
        cmd.execute(q)
        webrows = cmd.fetchall()
        db.close()
        return render(request, "Webseries.html", {'webrows': webrows})
    except Exception as e:
        print("errr:", e)


