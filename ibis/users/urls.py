#Este archivo URL es solo válido para la aplicación en la que está, en este caso Users
from django.urls import path
from users import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #Mis URL
    #Aqui voy a poner una para que la principal sea el perfil del usuario
    #en principio si el usuario no está logueado aparece el login y si no pues su página de inicio
    path('', views.login, name="userschange"),
    path('login/', views.login, name="users"),
    path('register/',views.register,name="register"),
    path('guardiandetails/',views.guardianDetails,name="guardiandetails"),
    path('userpanel/<str:username>',views.guardianPanel,name="userpanel")

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



