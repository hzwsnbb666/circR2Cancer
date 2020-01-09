"""cirRNA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from cirRNAInfo import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name="index"),
    url(r'^index/$', views.index, name="index"),

    url(r'^browse/$', views.browse, name="browse"),
    url(r'^browse/circRNA-Cancer', views.browse, name="circRNA-Cancer"),
    url(r'^browse/circRNA-miRNA', views.browse2, name="circRNA-miRNA"),
    url(r'^browse/miRNA-Cancer', views.browse3, name="miRNA-Cancer"),

    url(r'^detail/', views.detail, name="detail"),

    url(r'^download/', views.download, name="download"),

    url(r'^search/', views.search, name="search"),
    # url(r'^search2',views.search2,name="search2"),
    url(r'^all/', views.all, name="all"),
    url(r'^all2/', views.all2, name="all2"),
    url(r'^all3/', views.all3, name="all3"),

    url(r'^about/', views.about, name="about"),

    url(r'^getcirrna/(\d+)/$', views.getcirrna, name="getcirrna"),

    url(r'^getdisease/(\d+)/$', views.getdisease, name="getdisease"),

    url(r'^displaydisease/(.+)/$', views.displaydisease, name="displaydisease"),

    url(r'^displaycirrna/(.+)/$', views.displaycirrna, name="displaycirrna"),

    url(r'^displayiframe/$', views.displayiframe, name="displayiframe"),

    url(r'^searchcirrna/(.+)/$', views.searchcirrna, name="searchcirrna"),

    url(r'^searchdisease/(.+)/$', views.searchdisease, name="searchdisease"),

    url(r'^drawfigure/', views.drawfigure, name="drawfigure")

]
