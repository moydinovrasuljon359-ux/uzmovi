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
   path("category/<str:category_name>/", category, name="category"),
]