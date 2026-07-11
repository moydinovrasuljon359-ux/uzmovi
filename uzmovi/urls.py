from django import views
from django.urls import path
from .views import * 
urlpatterns = [
    path('navigation/', navigation, name='navigation'),
    path('footer/', footer, name='footer'),
     path('index/', index, name='index'),
   path('serial/', serial, name='serial'),
   path('kinoyangilik/',  kinoyangilik, name='kinoyangilik'),
   path('primyera/',  primyera, name='primyera'),
    path('film/',  film, name='film'),
    path('sms/', sms, name='sms'),
    path('qoida/', qoida, name='qoida'),
    path('royhat/', royhat, name='royhat'),
    path('videoichi/', videoichi, name='videoichi'),
    path("", splash, name='splash'),
   path('category/', category, name='category'),
   path('detali/<int:id>/', detali, name='detali'),

]