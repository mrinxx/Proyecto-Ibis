from django.conf.urls import url
from django.urls import path
from news import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.news, name="news"),
    path('details/<int:id>/',views.details,name="details"),
    path('getfirstnews',views.firstNews,name="getfirstnews"),   
    path('getnews',views.getNews,name="getnews"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)