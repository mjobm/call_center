from django.conf.urls import url

from call_center_scheduler.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name="index"),
]