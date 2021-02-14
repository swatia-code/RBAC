import mysql.connector
from db.db_conn import get_db_session
from data import tables_data
from log import logger

logObj = logger.getLogger()
conn = get_db_session()

def create_table(table_dict: dict):
    for table_name in tables_data.TABLES:
        table_description = tables_data.TABLES[table_name]
        try:
            logObj.debug("Creating table {}: ".format(table_name), end='')
            conn.query(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                logObj.error("already exists.")
            else:
                logObj.error(err.msg)
        else:
            logObj.debug("OK")

def get_emp_data():
    query = `SELECT * FROM employees`
    return conn.query(query)
    