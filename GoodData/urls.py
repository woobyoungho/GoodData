from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('signup/', views.Signup, name='signup'), #최종적인 url은 127.0.0.1:8000/GoodData/signup.html 이 된다.
    path('social_login_confirm/', views.Social_login_confirm, name='social_login_confirm'),
    path('existing_cus_search/', views.Existing_cus_search, name='existing_cus_search'),
    path('social_login_signup/', views.Social_login_signup, name='social_login_signup'),
    
    path('campaign/', views.Campaign_fn, name='campaign'),
    path('project/', views.Project_all, name='project_all'),
    path('project/<int:campaign_id>/', views.Project_fn, name='project_fn'),
    path('project/<int:campaign_id>/project_detail/<int:project_id>/', views.Project_detail, name='project_detail'),
    
    path('donation/', views.Donation, name='donation'),
    path('user_friends/', views.User_friends, name='user_friends'),
    path('user_friends_search/', views.User_friends_search, name='user_friends_search'),
    path('user_friends_enrollment/', views.User_friends_enrollment, name='user_friends_enrollment'),
    
    path('information/', views.Information, name='information'),
    path('information_update/', views.Information_update, name='information_update'),
    path('information_delete/', views.Information_delete, name='information_delete'),
    
    path('app_version_info/', views.App_version_info, name='app_version_info'),
    path('question/', views.Question, name='question'),
    path('notice/', views.Notice_fn, name='notice'),
    path('notice/<int:notice_id>/', views.Notice_detail, name='notice_detail'),
    path('privacy_policy/', views.Privacy_policy, name='privacy_policy'),
    path('open_source_license/', views.Open_source_license, name='open_source_license'),
    path('etc/', views.Etc, name='etc'),
    
    path('logout/', views.Logout, name='logout'),
    
    path('app_version/<str:type>/', views.App_version, name='app_version'),
    
    path('ios_get_info/<str:key_number>/', views.IOS_get_info, name='ios_get_info'),
    path('login_auto/<str:key_number>/', views.Login_auto, name='login_auto'),
]