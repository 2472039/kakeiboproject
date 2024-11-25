from django.urls import path
from . import views

app_name = 'kakeiboapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('addtotal', views.AddTotalView.as_view(), name='addtotal'),
    path('addpost', views.AddPostView.as_view(), name='addpost'),
    path('addsuccess', views.AddSuccessView.as_view(), name='add_success'),
    path('kakeibolist', views.KakeiboListView.as_view(), name='kakeibo_list'),
    path('kakeibolist/<str:category>', views.CategoryView.as_view(), name='category'),
    path('kakeibolist/detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('kakeibolist/<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
