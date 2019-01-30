
from django.contrib import admin
from django.urls import path
from weltest import views
from mobiletest import mobviews
from jylive import liveviews
from testmap import tmap
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mobile_app/', mobviews.mobile_app),
    path('mobtest_report/', mobviews.mobtest_report),
    path('run_dataform/', mobviews.run_dataform),
    path('param_app/', mobviews.param_app),
    path('Data_Verify/', mobviews.Data_Verify),
    path('ajax_c/', mobviews.ajax_c),
    path('log_info/', mobviews.log_info),
    path('param_save/', mobviews.param_save),
    path('check_save/', mobviews.check_save),
    path('check_run/', mobviews.check_run),
    path('cap_save/', mobviews.cap_save),
    path('envtest/', mobviews.envtest),
    path('medit_app/', mobviews.medit_app),
    path('cnosearch/', mobviews.cnosearch),
    path('map_app/', tmap.map_app),
    path('run_apptest/', mobviews.run_apptest),
    path('login/', views.login),
    path('', views.login),
    path('logout/', views.logout),
    path('home/', views.home),
    path ('welcome/', views.welcome),
    path('left/', views.left),
    path('livetest_report/', liveviews.livetest_report),
    path('live_run/', liveviews.live_run),
    path('live_param/', liveviews.live_param),
    path('live_param_save/', liveviews.live_param_save),
    path('run_livetest/', liveviews.run_livetest),
]
