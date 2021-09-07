from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    
    path('<int:pk>/',views.PostDetail.as_view(),name ='detail'),
    path('login/',views.loginUser,name= 'login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register',views.registerUser,name='register'),
    path('createpost/',views.createPost,name='create-post'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('updatepost/<int:id>/',views.updatePost,name = 'edit-post'),
    path('deletepost/<int:id>/',views.deletePost,name = 'delete-post'),
    path('',views.generalPage,name='general-page'),
    ]