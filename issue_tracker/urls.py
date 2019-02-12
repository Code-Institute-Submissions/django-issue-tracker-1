from django.conf.urls import url
from issue_tracker.views import get_issue_tracker_list, edit_an_issue, toggle_status, create_an_issue


urlpatterns = [
    url(r'^$', get_issue_tracker_list, name='get_issue_tracker_list'),
    url(r'^add$', create_an_issue, name='create_an_issue'),
    url(r'^edit/(?P<id>\d+)$', edit_an_issue, name='edit_an_issue'),
    url(r'^toggle/(?P<id>\d+)$', toggle_status, name='toggle_status')
]