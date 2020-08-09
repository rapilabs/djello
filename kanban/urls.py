from django.conf.urls import url

from .views import drop, index, new_card, new_column, view_card

urlpatterns = [
    url(r"^new-column/$", new_column),
    url(r"^new-card/$", new_card),
    url(r"^cards/(?P<card_id>\d+)/(?P<card_slug>[\w-]+)/$", view_card),
    url(r"^drop/$", drop),
    url(r"^$", index),
]
