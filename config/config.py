import json 
from pathlib import Path

class RBAC_config_base(object):
	def __init__(self):
		self.rbac_port 		= None
		self.auth_enabled 	= False
		self.db_host 		= None
		self.db_username 	= None
		self.db_password 	= None
		self.db_port 		= None
		self.encrpt_key 	= None
		self.server_url 	= None
		self.log_level 		= None
		self.log_output 	= None
		self.database_name 	= None

CONFIGOBJ 	= None
PROJECTPATH = r'C:\\Users\\SWATI ARORA\\RBAC\\config\\'
FILENAME 	= "config.json"

def load_config():
	global CONFIGOBJ
	global PROJECTPATH
	global FILENAME
	if CONFIGOBJ is None:
		CONFIGOBJ = RBAC_config_base()
		file = PROJECTPATH +  FILENAME  
		try:
			with open(file) as f:
				data = json.load(f)
				CONFIGOBJ.rbac_port 	= data['RBAC_PORT']
				CONFIGOBJ.auth_enabled 	= data['AUTHENTICATION_ENABLE']
				CONFIGOBJ.db_host 		= data['DB_HOST']
				CONFIGOBJ.db_username 	= data['DB_USERNAME']
				CONFIGOBJ.db_password 	= data['DB_PASSWORD']
				CONFIGOBJ.db_port 		= data['DB_PORT']
				CONFIGOBJ.encrpt_key 	= data['ENCRYPTION_KEY']
				CONFIGOBJ.server_url 	= data['SERVER_URL']
				CONFIGOBJ.log_level 	= data['LOG_LEVEL']
				CONFIGOBJ.log_output 	= data['LOG_OUTPUT']
				CONFIGOBJ.database_name = data['DATABASE_NAME']
		except Exception as e:
			print("Found error {}".format(e))
			
	return CONFIGOBJ
