from django.conf.urls import url, include
from rest_framework import routers
from pokeapi import views
from django.contrib import admin
 
router = routers.DefaultRouter()
router.register(r'pokemon', views.PokemonViewSet)
 
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]