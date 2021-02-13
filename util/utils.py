from datetime import datetime

def getuUid():
	currentTime = str(datetime.now())
	uUid  = currentTime.replace(" ",'')
	uUid  = uUid.replace(":",'-')
	uUid  = uUid.replace(".",'-')
	return uUid
