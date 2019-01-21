



import os
import sys
import json
import re



if __name__ == '__main__':
	os.environ.setdefault( 'DJANGO_SETTINGS_MODULE', 'dockerdj.settings' )
	## Set remaining environment variables
	with open( 'vault.json' ) as vault:
		formula = re.compile( r'([a-z0-9])([A-Z])' )
		for key, value in json.load( vault ).items( ):
			setting = formula.sub( r'\1_\2', key ).upper( )
			os.environ.setdefault( setting, value )
	## Boot up the Django application server
	try:
		from django.core.management import execute_from_command_line
	except ImportError as exc:
		raise ImportError(
			'Couldn\'t import Django. Are you sure it\'s installed and '
			'available on your PYTHONPATH environment variable? Did you '
			'forget to activate a virtual environment?'
		) from exc
	execute_from_command_line( sys.argv )


