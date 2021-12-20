from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()

# router.register(r'order', views.OrderViewSet)
# router.register(r'order_details', views.OrderDetailViewSet)
# router.register(r'product', views.ProductViewSet)
# router.register(r'factory_table', views.FtyTableViewSet)



urlpatterns = [
    path('', views.home, name="home"),
    path('login/',views.app_login, name="login"),
    path('logout/',views.app_logout, name="logout"),
    path('register/',views.register, name="register"),

    path('pimodel/create/', views.create_PIModel, name="create_PIModel"), 
    path('pimodel/update/<str:model_pk>', views.update_PIModel, name="update_PIModel"),
    path('pimodel/delete/<str:model_pk>', views.delete_PIModel, name="delete_PIModel"),
    path('pimodel/show/', views.show_PIModel, name="show_PIModel"), 

    path('pisubmodel/create/<str:pk>', views.create_PISubModel, name="create_PISubModel"), 
    path('pisubmodel/update/<str:sub_model_pk>', views.update_PISubModel, name="update_PISubModel"),
    path('pimodel/delete/<str:model_pk>/<str:sub_model_pk>', views.delete_PISubModel, name="delete_PISubModel"),
    path('pisubmodel/show/<str:model_pk>', views.show_PISubModel, name="show_PISubModel"), 
    path('pisubmodel/open/<str:sub_model_pk>', views.open_PISubModel, name="open_PISubModel"), 

    # path('api/',include(router.urls)),
]