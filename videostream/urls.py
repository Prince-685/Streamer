"""videostream URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import CategoryView
from . import ShowsView
from . import EpisodesView
from . import AdminView
from . import UserView
from . import Movies

urlpatterns = [
    path('admin/', admin.site.urls),
    # user
    path('userview/',UserView.UserView),
    path('preview/',UserView.Preview),
    path('englishpreview/',UserView.EnglishPreview),
    path('sportspreview/',UserView.SportsPreview),
    path('tvpreview/',UserView.TvPreview),
    path('userdetailsubmit/',UserView.UserDetailSubmit),
    path('checkmobilenumber/',UserView.CheckMobileNumber),
    path('usersession/',UserView.UserSession),
    path('userlogout/',UserView.UserLogout),
    path('searching/',UserView.Searching),
    path('webseriespreview/',UserView.WebseriesPreview),
    # path('accountactivation/',UserView.AccountActivation),

    # Movies
    path('hindimovies/',Movies.HindiMovies),
    path('englishmovies/',Movies.EnglishMovies),
    path('webseries/',Movies.Webseries),
    # Admin
    path('adminlogin/',AdminView.AdminLogin),
    path('checklogin',AdminView.CheckLogin),
    # category
    path('categoryinterface/', CategoryView.CategoryInterface),
    path('submitcategory', CategoryView.SubmitCategory),
    path('displayallcategory', CategoryView.DisplayAll),
    path('categorybyid/', CategoryView.CategoryById),
    path('editdeletecategorydata/', CategoryView.EditDeleteCategoryData),
    path('editicon',CategoryView.EditIcon),
    path('displayallcategoryjson/',CategoryView.DisplayAllJSON),
    # shows
    path('showsinterface/', ShowsView.ShowsInterface),
    path('submitshows', ShowsView.SubmitShows),
    path('displayshows', ShowsView.DisplayShows),
    path('showbyid/',ShowsView.ShowById),
    path('editdeleteshowdata/',ShowsView.EditDeleteShowData),
    path('editposterurl',ShowsView.EditPosterurl),
    path('edittrailerurl',ShowsView.EditTrailerurl),
    path('editvideourl',ShowsView.EditVideourl),
    path('editposter2url',ShowsView.EditPoster2url),
    path('displayallshowjson/',ShowsView.DisplayAllShowJSON),
    # episodes
    path('episodesinterface/',EpisodesView.EpisodesInterface),
    path('submitepisodes',EpisodesView.SubmitEpisodes),
    path('displayallepisodes',EpisodesView.DisplayAllEpisodes),
    path('episodebyid/',EpisodesView.EpisodeById),
    path('editdeleteepisodedata/',EpisodesView.EditDeleteEpisodeData),
    path('editposter',EpisodesView.EditPoster),
    path('edittrailer',EpisodesView.EditTrailer),
    path('editvideo',EpisodesView.EditVideo),

]
