from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from authentication.views import AccountViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
    '',
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.recipes.urls')),
)

urlpatterns += [
url(r'^api-auth/', include('rest_framework.urls',
                            namespace='rest_framework')),
]
