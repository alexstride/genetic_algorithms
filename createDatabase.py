import sqlite3
from sqlite3 import Error
import logging as lg
lg.basicConfig(level=lg.DEBUG)


def create_connection(db_file):
	""" create a database connection to the SQLite database spec
	ified by db_file
	:param db_file: database file:
	:return: connection object or None
	"""

	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)

	return None

def create_project(conn,project):
	"""
	Create a new project into the projects table
	:param conn: 
	:param project:
	:return: project id
	"""
	sql = """ INSERT INTO projects(name,begin_date,end_date)
			Values("Do something)