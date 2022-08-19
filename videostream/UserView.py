from django.shortcuts import render
from . import pool
from django.http import JsonResponse
def UserView(request):
    try:
        ses = ''
        user = ''

        try:
            if (request.session['USER']):
                ses = True
                user = request.session['USER']
            else:
                ses: False
                user = []
            print("USER", user)
        except:
            pass
        db, cmd = pool.ConnectionPooling()
        q = "select * from category"
        cmd.execute(q)
        rows = cmd.fetchall()

        q = "select * from shows where status='Trending'"
        cmd.execute(q)
        trows = cmd.fetchall()

        q = "select * from shows where categoryid in(select categoryid from category where categoryname='Tv Shows')"
        cmd.execute(q)
        tvrows = cmd.fetchall()

        q = "select * from shows where categoryid in(select categoryid from category where categoryname='English Movies')"
        cmd.execute(q)
        hrows = cmd.fetchall()

        q = "select * from shows where categoryid in(select categoryid from category where categoryname='Sports')"
        cmd.execute(q)
        srows = cmd.fetchall()

        q = "select * from shows where categoryid in(select categoryid from category where categoryname='Webseries')"
        cmd.execute(q)
        wrows = cmd.fetchall()

        db.close()
        return render(request, "UserInterface.html", {'rows': rows,'trows': trows,'tvrows': tvrows,'hrows': hrows,'srows': srows,'wrows': wrows,'ses':ses,'user':user})
    except Exception as e:
        print("err:", e)
        return render(request, "UserInterface.html", {'rows': []})

def Preview(request):
    ses = ''
    user = ''
    try:
        if(request.session['USER']):
            ses = True
            user=request.session(['USER'])
        else:
            ses = False
            user=[]
        print("USER", user)
    except:
        pass
    row=request.GET['row']
    row=eval(row)

    db, cmd = pool.ConnectionPooling()

    # More like this
    q = "select * from shows where categoryid in(select categoryid from category where categoryname='Hindi Movies')"
    cmd.execute(q)
    hmovies = cmd.fetchall()

    db.close()

    return render(request, "Preview.html",{'row': row,'hmovies':hmovies,'ses':ses,'user':user})


def TvPreview(request):
    ses = ''
    user = ''
    try:
        if (request.session['USER']):
            ses = True
            user = request.session(['USER'])
        else:
            ses = False
            user = []
        print("USER", user)
    except:
        pass
    row = request.GET['row']
    # conversion of string into tuple
    row = eval(row)

    db, cmd = pool.ConnectionPooling()

    # episodes
    q = "select * from episodes where categoryid=3 and showid={}".format(row[1])
    cmd.execute(q)
    episodes = cmd.fetchall()

    # More like this
    q = "select * from shows where categoryid in(select categoryid from category where categoryname='Tv Shows')"
    cmd.execute(q)
    tvshows = cmd.fetchall()

    db.close()

    return render(request, "TvPreview.html", {'row': row,'episodes':episodes,'tvshows':tvshows,'ses':ses,'user':user})

def EnglishPreview(request):
    ses = ''
    user = ''
    try:
        if (request.session['USER']):
            ses = True
            user = request.session(['USER'])
        else:
            ses = False
            user = []
        print("USER", user)
    except:
        pass
    db, cmd = pool.ConnectionPooling()
    row = request.GET['row']
    # conversion of string into tuple
    row = eval(row)

    # More like this
    q = "select * from shows where categoryid in(select categoryid from category where categoryname='English Movies')"
    cmd.execute(q)
    emovies = cmd.fetchall()

    db.close()

    return render(request, "EnglishPreview.html", {'row': row,'emovies':emovies,'ses':ses,'user':user})

def WebseriesPreview(request):
    ses = ''
    user = ''
    try:
        if(request.session['USER']):
            ses = True
            user=request.session(['USER'])
        else:
            ses = False
            user=[]
        print("USER", user)
    except:
        pass
    row=request.GET['row']
    row=eval(row)

    db, cmd = pool.ConnectionPooling()

    # episodes
    q = "select * from episodes where categoryid=5 and showid={}".format(row[1])
    cmd.execute(q)
    wepisodes = cmd.fetchall()
    # More like this
    q = "select * from shows where categoryid in(select categoryid from category where categoryname='Webseries')"
    cmd.execute(q)
    webrows = cmd.fetchall()

    db.close()

    return render(request, "webseriesPreview.html",{'row': row,'webrows':webrows,'wepisodes':wepisodes,'ses':ses,'user':user})

def SportsPreview(request):
    ses = ''
    user = ''
    try:
        if (request.session['USER']):
            ses = True
            user = request.session(['USER'])
        else:
            ses = False
            user = []
        print("USER", user)
    except:
        pass
    db, cmd = pool.ConnectionPooling()
    row = request.GET['row']
    # conversion of string into tuple
    row = eval(row)

    # More like this
    q = "select * from shows where categoryid in(select categoryid from category where categoryname='Sports')"
    cmd.execute(q)
    sports = cmd.fetchall()

    db.close()

    return render(request, "SportsPreview.html", {'row': row,'sports':sports,'ses':ses,'user':user})

def UserDetailSubmit(request):
    try:
        db, cmd = pool.ConnectionPooling()
        mobileno = request.GET['mobileno']
        username = request.GET['username']
        age = request.GET['age']
        gender = request.GET['gender']
        status=request.GET['status']
        q="insert into clientdetails (mobilenumber,username,age,gender,status) values('{0}','{1}',{2},'{3}','{4}')".format(mobileno,username,age,gender,status)
        cmd.execute(q)
        db.commit()
        db.close()
        return JsonResponse("Registration Completed Successfully",safe=False)
    except Exception as e:
        print("errrr",e)
        return JsonResponse("Fail to Submit",safe=False)


def CheckMobileNumber(request):
    try:
        db, cmd = pool.ConnectionPooling()
        mobileno = request.GET['mobileno']
        q="select * from clientdetails where mobilenumber='{}'".format(mobileno)
        print(q)
        cmd.execute(q)
        row=cmd.fetchone()
        db.close()
        return JsonResponse(row, safe=False)
    except Exception as e:
        print("errrr",e)
        return JsonResponse(None,safe=False)

def UserSession(request):
    try:
        db, cmd = pool.ConnectionPooling()
        mobileno = request.GET['mobileno']
        username=request.GET['username']

        request.session["USER"]=[mobileno,username]
        return JsonResponse(True, safe=False)
    except Exception as e:
        print("errrr",e)
        return JsonResponse(False,safe=False)

def UserLogout(request):
    try:
        del request.session['USER']
        return UserView(request)
    except Exception as e:
        print("er:",e)

def Searching(request):
    try:
        db, cmd = pool.ConnectionPooling()
        search = request.GET['search']
        q = "select * from shows where showname like '{}%'".format(search)
        print(q)
        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        return JsonResponse(rows, safe=False)
    except Exception as e:
        print("errrr", e)
        return JsonResponse(None, safe=False)


# def AccountActivation(request):
#     try:
#         db, cmd = pool.ConnectionPooling()
#         mobileno = request.GET['mobileno']
#         status=request.GET['status']
#         q="update clientdetails set status='activate' where mobilenumber='{}'".format(mobileno)
#         cmd.execute(q)
#         db.commit()
#         db.close()
#         return JsonResponse("Registration Completed Successfully",safe=False)
#     except Exception as e:
#         print("errrr",e)
#         return JsonResponse("Fail to Submit",safe=False)