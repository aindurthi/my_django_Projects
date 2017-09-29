from django.conf.urls import include, url
from .views import YoMamaChatView,index

urlpatterns = [
                  url(r'^73c8d5d79e78f9daaf593f5ff9dbd9b62a925d03feff48c275/?$', YoMamaChatView.as_view()),
                  url(r'^73c8d5d79e78f9daaf593f5ff9dbd9b62a925d03feff48c275/books/', index)
               ]