



from django.urls import path

from tutorial import views



urlpatterns = [
	path( '', views.index, name = 'index' )
]


