from django.conf.urls import url
from miapp3 import views #hay que poner aqui from la aplicacion

urlpatterns = [

	url(r'^$',views.indice,name='indice'),
#    cadena vacia, llama a la vista idice, con el nombre de enlace: indice

 	url(r'^registro$', views.registro, name='registro'),
    	url(r'^login$', views.loginpage, name='login'),
    	url(r'^logout$', views.logoutpage, name='logout'),
	url(r'^addarticulo$', views.addarticulo, name='addarticulo'),
	url(r'^clasificacion/(?P<NuevoUsado_id>\w+)/$',views.nuevoUsado, name='NuevoUsado'),
#explicacion url de la linea anterior:
#escribimos clasificacion para diferenciar de las url anteriores
#NuevoUsado_id es una variable que contendrá un caracter 'U' o 'N' por eso ponemos \w+
#views.nuevoUsado accedemos a la funcion nuevoUsado de views
#el nombre de la variable que se usara en el html es 'NuevoUsado'(creo que es el nombre del enlace)	
]
