"""django_issue_tracker URL Configuration

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

from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from .settings import MEDIA_ROOT
from issue_tracker.views import get_issue_tracker_list, create_an_issue, edit_an_issue, toggle_status
from accounts import urls as accounts_urls
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from posts import urls as posts_urls
from accounts.views import index
from products.views import all_products



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),


    url(r'^issues$', get_issue_tracker_list),
    url(r'^add$', create_an_issue),
    url(r'^edit/(?P<id>\d+)$', edit_an_issue),
    url(r'^toggle/(?P<id>\d+)$', toggle_status),
    
    
    url(r'posts/', include(posts_urls)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),

]
