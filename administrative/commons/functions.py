import os
import sys
import traceback
from datetime import datetime, date, timedelta

def is_double(valor):
	try:
		nuevo = float(valor)
		return True
	except:
		return False

def is_dir(path):
	try:
		if os.path.isdir(path):
			return True
		else:
			return False
	except:
		return False

def create_dir(path):
	try:
		if os.mkdir(path):
			return True
		else:
			return False
	except:
		return False

def is_file(path):
	try:
		if os.path.isfile(path):
			return True
		else:
			return False
	except:
		return False

def validate_date(value):
	try:
		return datetime.strptime(value, "%Y-%m-%d")
	except:
		raise Exception(f"La fecha '{value}' no es valida.")