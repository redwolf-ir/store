from datetime import datetime
import hashlib

def make_token(username, useremail):
	username = username
	useremail = useremail
	token = (username+useremail).encode('utf-8')

	return hashlib.md5(token).hexdigest()
