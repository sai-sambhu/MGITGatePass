"""users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from basic_app import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.index,name='index'),   
    
    url(r'^admin/', admin.site.urls),
    
    url(r'^register/$',views.register,name='register'),
    
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^logout/$',views.user_logout,name='logout'),
    
    url(r'^student/$',views.student,name='student'),
    url(r'^student/securityClick$',views.securityClick,name='studentSecurityClick'),
    url(r'^student/requestGP$',views.gpValidate,name='studentRequestGP'),
    
    url(r'^incharge/$',views.incharge,name='incharge'),
    url(r'^incharge/Approve',views.inchargeApprove,name='inchargeApprove'),
    url(r'^incharge/Disapprove$',views.inchargeDispprove,name='inchargeDisapprove'),
    url(r'^incharge/disapproveAllStudents$',views.disapproveAllStudents,name='disapproveAllStudents'),
    url(r'^incharge/refreshAllStudents$',views.refreshAllStudents,name='refreshAllStudents'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
