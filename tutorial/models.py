



from django.db import models



class Word( models.Model ):
	word = models.CharField( max_length = 50, blank = True )
	created_at = models.DateTimeField( auto_now_add = True )
	modified_at = models.DateTimeField( auto_now = True )
	
	def __str__( self ):
		return self.word
	
	
	class Meta:
		db_table = 'words'


