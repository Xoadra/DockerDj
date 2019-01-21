



import socket
from django.shortcuts import render



def index( request ):
	context = { 'name': 'zoey', 'host': socket.gethostname( ) }
	return render( request, 'tutorial/index.html', context )



