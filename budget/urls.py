from django.conf.urls import url
from . import views

app_name = 'budget'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'new/', views.NewExpenseView.as_view(), name='new')
]