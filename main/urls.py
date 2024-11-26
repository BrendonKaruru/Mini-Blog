from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('create-blog', views.createBlog, name='create_blog'),
    path('blog/<int:pk>/update', views.updateBlog, name='update_blog'),
    path('bloginfo/<int:pk>', views.bloginfo, name='bloginfo' ),
    path('deleteblog/<int:pk>', views.deleteblog, name='deleteblog' ),
    path('loginuser', views.loginuser, name='login'),
    path('logout', views.logout_user, name='logout' )
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)