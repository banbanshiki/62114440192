from django.urls import path, include
from api.views import *
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", users),
    path('api/datatent/', views.tent_data, name='tent_data'),
    path('api/datazipo/', views.zipo_data, name='zipo_data'),
    path('api/datajacket/', views.jacket_data, name='jacket_data'),
    path('api/datamap/', views.map_data, name='map_data'),
    path('api/datacook/', views.cook_data, name='cook_data'),
    path('api/dataLED/', views.LED_data, name='LED_data'),
    path('api/datasleep/', views.sleep_data, name='sleep_data'),
    path('api/dataeqipano/', views.eqipano_data, name='eqipano_data'),
    path('api/databack/', views.back_data, name='back_data'),
    path('api/databoot/', views.boot_data, name='boot_data'),
    path('api/dataknife/', views.knife_data, name='knife_data'),
    path('forests/', ForestList.as_view(), name='forest-list'),
    path('register/', UserCreate.as_view(), name='register'),
    path('api/databookfo/', views.bookfo_data, name='bookfo_data'),
    path('api/datasl/', views.sl_data, name='sl_data'),
    path('api/datatoilet/', views.toilet_data, name='toilet_data'),
    path('api/dataportal/', views.portal_data, name='portal_data'),
    path('api/datacooking/', views.cooking_data, name='cooking_data'),
    path('api/datafirstaid/', views.firstaid_data, name='firstaid_data'),
    path('login/', UserLogin.as_view(), name='login'),
    path('diary-entries/', DiaryEntryList.as_view(), name='diaryentry-list'),
    path('diary-entries/<int:pk>/', DiaryEntryDetail.as_view(), name='diaryentry-detail'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('get-csrf-token/', get_csrf_token, name='get-csrf-token'),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)