from django.urls import path


from places import views

urlpatterns = [
    path("", views.index),
    path("create", views.create),
    path("delete/<place_id>", views.delete)
]
