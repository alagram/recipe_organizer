from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recipe_organizer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.recipes.urls')),
)

urlpatterns += [
url(r'^api-auth/', include('rest_framework.urls',
                            namespace='rest_framework')),
]
