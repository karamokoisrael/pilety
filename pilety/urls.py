from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler500, handler400, handler403, handler404
# from wholesale.views import ProductApi

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



admin.site.site_header = "Pilety Admin"
admin.site.site_title = "Pilety Admin Portal"
admin.site.index_title = "Pilety, Logistics and Transport Solution"

handler500 = 'allin.views.error_handler'
handler404 = 'allin.views.error_handler'
handler403 = 'allin.views.error_handler'
handler400 = 'allin.views.error_handler'

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dev@pilety.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('ac/api/', include('users.api_urls', namespace='users_api')),

    path('', include('allin.urls', namespace='allin')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
# if not settings.DEBUG:
#     handler500 = 'allin.views.error_handler'
#     handler404 = 'allin.views.error_handler'
#     handler403 = 'allin.views.error_handler'
#     handler400 = 'allin.views.error_handler'

if settings.DEBUG:
    # import debug_toolbar
    # urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

