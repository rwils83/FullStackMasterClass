from django.urls import path
from . import views

urlpatterns = [
        path('simple_view', views.simple_view, name="simple_view"),
        path('', views.home_view, name="home_view"),
        path('<topic>', views.dynamic_view),
        path('addition/<int:num1><int:num2>',views.add_view_myway),
        path('classaddition/<int:num1>/<int:num2>', views.add_view_classway),
        path('properresponsenotfound/<str:topic>', views.proper_response_not_found),
        path('proper404/<str:topic>', views.proper_404),
            ]

