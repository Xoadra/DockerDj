



import socket
from django.shortcuts import render

from tutorial.models import Word



def index( request ):
	words = Word.objects.all( )
	empty = Word( word = '<em>no words available</em>' )
	context = { 'name': 'zoey', 'host': socket.gethostname( ) }
	context[ 'words' ] = words if len( words ) else [ empty ]
	return render( request, 'tutorial/index.html', context )


