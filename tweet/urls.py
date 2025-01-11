from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        # epath('', views. name='tasks'),
        path('tweet/', views.tweet_post, name='tweet'),
        path('', views.tweet_list, name='tweet_list'),
        path('create/', views.tweet_create, name='tweet_create'),
        path('<int:tweet_id>/edit', views.tweet_edit, name='tweet_edit'),
        path('<int:tweet_id>/delete', views.tweet_delete, name='tweet_delete'),
        path('<int:tweet_id>/post', views.tweet_post, name='tweet_post'),
        path('accounts/register',views.register,name='accounts'),
    ]
if settings.DEBUG:
          urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
