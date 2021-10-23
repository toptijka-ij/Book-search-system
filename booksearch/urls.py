from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import path, include
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('author/', include('author.urls', namespace='author')),
    path('book/', include('book.urls', namespace='book')),
    path('comment/', include('comment.urls', namespace='comment')),
    path('review/', include('review.urls', namespace='review')),
    path('api/', include('api.urls')),
]
if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = 'main.views.handler_not_found'
handler403 = 'main.views.handler_perm_denied'
handler400 = 'main.views.handler_bad_gateway'
handler500 = 'main.views.handler_server_error'
