import json


class RBAC_config_base(object):
	"""docstring for RBAC_config"""

	def __init__(self):
		super(RBAC_config_base, self).__init__()
		self.__rbac_port = None
		self.__auth_enabled = False
		self.__db_host = None
		self.__db_username = None
		self.__db_password None
		self.__db_port = None
		self.__encrpt_key = None
		self.__server_url = None
		self.__log_level = None
		self.__log_output = None

class RBAC_config(RBAC_config_Base):
	""""""
	__instance = None

	def getInstance(filename):
      """ Static access method. """
      if RBAC_config.__instance == None:
         RBAC_config()
      return RBAC_config.__instance

	def __init__(self, filename):
		if RBAC_config.__instance != None:
			raise Exception("This class is a singleton!")
		else:
			RBAC_config.__instance = self
			super(RBAC_config_Base).__init__()
			self.filename = filename
			self._parse_config(self.filename)


	def _parse_config(self, filename: str):
		with open(filename) as f:
			data = json.load(f)
		self.__rbac_port = data['RBAC_PORT']
		self.__auth_enabled = data['AUTHENTICATION_ENABLE']
		self.__db_host = data['DB_HOST']
		self.__db_username = data['DB_USERNAME']
		self.__db_password = data['DB_PASSWORD']
		self.__db_port = data['DB_PORT']
		self.__encrpt_key = data['ENCRYPTION_KEY']
		self.__server_url = data['SERVER_URL']
		self.__log_level = data['LOG_LEVEL']
		self.__log_output = data['LOG_OUTPUT']





