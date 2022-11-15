from django.urls import path
from . import views

app_name = "cards"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/indiv/", views.create_indiv, name="create_indiv"),
    path("create/group/", views.create_group, name="create_group"),
    # 주소 정리해야함
    path("detail/group/<int:pk>", views.group_detail, name="group_detail"),
    path("detail/indiv/", views.indiv_detail, name="indiv_detail"),
    path("<int:pk>/indiv/update/", views.card_update, name="card_update"),
    path("<int:pk>/group/update/", views.groupcard_update, name="groupcard_update"),
    path("<int:pk>/group/delete/", views.groupcard_delete, name="groupcard_delete"),
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    path("<int:pk>/gcomments/", views.gcomment_create, name="gcomment_create"),
    path(
        "<int:cards_pk>/group/<int:comment_pk>/delete/",
        views.gcomments_delete,
        name="gcomments_delete",
    ),
]
