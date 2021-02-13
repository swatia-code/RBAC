import logging

LOGLEVEL = 3 #TODO: this should be taken from config 
LOGOBJ = None

def getLogger():
	global LOGOBJ
	if LOGOBJ is None:
		logging.basicConfig(format='%(levelname)s:%(message)s',filename='logFile.log', level=logging.ERROR)
		LOGOBJ = logging.getLogger(__name__)
		LOGOBJ.setLevel(LOGLEVEL)
	return LOGOBJ