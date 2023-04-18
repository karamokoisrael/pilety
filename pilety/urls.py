from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from wholesale.views import ProductApi


admin.site.site_header = "Pilety Admin"
admin.site.site_title = "Pilety Admin Portal"
admin.site.index_title = "Pilety, Logistics and Transport Solution"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('ac/api/', include('users.api_urls', namespace='users_api')),
    path('fn/api/', include('finance.api_urls', namespace='finance_api')),
    path('sh/api/', include('shipping.api_urls', namespace='shipping_api')),
    path('', include('shipping.urls', namespace='shipping')),
    # path('3', ProductApi.as_view()),

]

if settings.DEBUG:
    # import debug_toolbar
    # urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

