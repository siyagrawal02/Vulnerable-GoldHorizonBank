from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('signup/', views.signup,name='signup'),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('namelist/',views.namelist,name="namelist"),
    # path('success',views.success,name="success"),
    path('id',views.loadid,name="loadid"),
    path('update',views.update, name='update'),
    path('update/updateinfo/<int:id>',views.updateinfo, name='updateinfo'),
    path('displaylist/',views.displaylist,name="displaylist"),
    path('displaylist/display/<int:id>',views.display,name='display'),
    path('displaylist/delete/<int:id>', views.delete, name='delete'),

    path('option', views.option, name='option'),
    
]

urlpatterns += staticfiles_urlpatterns()