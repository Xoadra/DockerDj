



import os
import socket
from django.shortcuts import render

from tutorial.models import Word



def index( request ):
	name = os.getenv( 'SELF', 'zoey' )
	## Name is capitalized differently in the Docker build
	words = list( ) if name.istitle( ) else Word.objects.all( )
	empty = Word( word = '<em>no words available</em>' )
	context = { 'name': name, 'host': socket.gethostname( ) }
	context[ 'words' ] = words if len( words ) else [ empty ]
	return render( request, 'tutorial/index.html', context )



