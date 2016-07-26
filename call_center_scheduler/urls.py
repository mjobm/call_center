from django.conf.urls import url

from call_center_scheduler.views import HomePageView, RequestSlotView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name="index"),
    url(r'^request_slot/$', RequestSlotView.as_view(), name="slotview")
]