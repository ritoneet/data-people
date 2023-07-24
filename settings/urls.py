from django.contrib import admin
from django.urls import path
# from people.views import index_view
# from people.views import people_list
from people.views import ListPeopleView
from people.views import RatePeopleView
# from people.views import people_rate
# from people.views import people_details
from people.views import DetailsPeopleView
# from people.views import people_update
from people.views import UpdatePeopleView
# from people.views import people_delete
from people.views import DeletePeopleView
from people.views import HomePeopleView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePeopleView.as_view(), name="home-link"),
    path('list-people/', ListPeopleView.as_view(), name="people-list-link"),
    path('create-people/', RatePeopleView.as_view(), name="people-rate-link"),
    path('details-people/<int:pk>', DetailsPeopleView.as_view(), name="people-details-link"),
    path('update-people/<int:pk>', UpdatePeopleView.as_view(), name="people-update-link"),
    path('delete-people/<int:pk>', DeletePeopleView.as_view(), name="people-delete-link")
]
