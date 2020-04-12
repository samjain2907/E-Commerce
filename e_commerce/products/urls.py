from django.urls import path , include
from products.views import productallview , producteachview 

urlpatterns = [
    path('',productallview.as_view()),
    path('<pk>',producteachview.as_view()),
]