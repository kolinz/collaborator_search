from django.urls import path
from .import views

# URLパターンの逆引きに使う
app_name = 'hrdb'

# URLパターンの登録
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post_persondata/', views.CreatePersonView.as_view(), name='post_persondata'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
    path('person_detail/<int:pk>',views.DetailPersonView.as_view(), name='person_detail'),
    path('person_title/<int:title>',views.TitleView.as_view(), name='person_title'),
    path('person_occupation/<int:occupation>',views.OccupationView.as_view(), name='person_occupation'),
    path('person_org/<int:org>',views.OrgView.as_view(), name='person_org'),
    path('mypage_person/', views.MyPersonPageView.as_view(), name='mypage_person'),
    path('myperson_detail/<int:pk>',views.DetailMyPersonView.as_view(), name='myperson_detail'),
    path('result/create/<int:pk>/', views.ResultCreateView.as_view(), name='resultdata_create'),
    path('mypage_person/<int:pk>/delete/', views.PersonDeleteView.as_view(), name='persondata_delete'),
    path('mypage_result/<int:pk>/delete/', views.ResultDeleteView.as_view(), name='resultdata_delete'),
]