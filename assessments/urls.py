from django.urls import path
from .views import enter_scores


urlpatterns = [

    path(
        "enter/<int:assessment_id>/",
        enter_scores,
        name="enter_scores"
    ),

]

from django.urls import path
from .views import assessment_list, enter_scores


urlpatterns = [

    path(
        "",
        assessment_list,
        name="assessment_list"
    ),

    path(
        "enter/<int:assessment_id>/",
        enter_scores,
        name="enter_scores"
    ),

]