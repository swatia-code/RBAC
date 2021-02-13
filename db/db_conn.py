import mysql.connector
from mysql.connector import errorcode
import db_const


class MySQL(object):
	_instance = None
	def __new__(cls):
		if cls._instance is None:
			cls._instance = object.__new__(cls)
			# TODO: take this value from db_config.yml
			db_config = {'database': 'rbac', 'host': '127.0.0.1', 
			'password': 'swatiArora@1', 'port': 3306, 'user': 'swati'}
			try:
				print('connecting to MySQL database...')
				connection = MySQL._instance.connection = mysql.connector.connect(**db_config)
				cursor = MySQL._instance.cursor = connection.cursor()
				cursor.execute('SELECT VERSION()')
				db_version = cursor.fetchone()
			except Exception as error:
				print('Error: connection not established {}'.format(error))
				MySQL._instance = None
			else:
				print('connection established\n{}'.format(db_version[0]))

		return cls._instance

	def __init__(self):
		self.connection = self._instance.connection
		self.cursor = self._instance.cursor

	def query(self, query):
		try:
			result = self.cursor.execute(query)
		except Exception as error:
			print('error execting query "{}", error: {}'.format(query, error))
			return None
		else:
			return result

	def __del__(self):
		self.connection.close()
		self.cursor.close()
		
my_sql = MySQL()
print("Created class {}".format(my_sql))