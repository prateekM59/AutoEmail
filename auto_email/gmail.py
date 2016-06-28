import smtplib
import sys
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Defining Globals
uname = 'colt0anaconda@gmail.com'
pswd = None
receiverList = ['prateekmahajan59@gmail.com', 'colt0anaconda@gmail.com']
receiverString = ", ".join(receiverList)
content = "This is a test mail by Prateek."

# MIME multipart message
msg = MIMEMultipart()
msg['Subject'] = "Test Mail"
msg['From'] = uname
msg['To'] = receiverString
msg.attach(MIMEText(content))

def main():
	global pswd
	smtpObj = None
	getCredentials()
	try:
		smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
		smtpObj.starttls()
		smtpObj.login(uname,pswd)
		smtpObj.sendmail(uname, receiverList, msg.as_string())
		print "Sent Successfully"
	except Exception as e:
		print "Error: Not able to send"
   		print str(e)
   		return

def getCredentials():
	global pswd
	promptString = 'Enter password for ' + uname + ': '
	
	if sys.stdin.isatty():
	    pswd = getpass.getpass(prompt = promptString)
	else:
		print "Warning!!! Password may be echoed. Use a terminal for suppressing echo.\nAbort by Ctrl+Z.\n"
		print promptString
		sys.stdout.flush()
		pswd = sys.stdin.readline().rstrip()

main()