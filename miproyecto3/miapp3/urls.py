from django.conf.urls import url
from miapp3 import views #hay que poner aqui from la aplicacion

urlpatterns = [

	url(r'^$',views.indice,name='indice'),
#    cadena vacia, llama a la vista idice, con el nombre de enlace: indice

 	url(r'^registro$', views.registro, name='registro'),
    	url(r'^login$', views.loginpage, name='login'),
    	url(r'^logout$', views.logoutpage, name='logout'),
	url(r'^addarticulo$', views.addarticulo, name='addarticulo'),	
]
