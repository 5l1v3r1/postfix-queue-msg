import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
import os
import sys

# @dalvarez_s 2016/03/07
# based on http://masnun.com/2010/01/01/sending-mail-via-postfix-a-perfect-python-example.html

def sendMail(to, fro, subject, text, files=[],server="localhost"):

    msg = MIMEMultipart()
    msg['From'] = fro
    msg['To'] = to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text) )

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'
                       % os.path.basename(file))
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(msg['From'], msg['To'], msg.as_string() )
    smtp.close()



if len(sys.argv) < 6:
    print "Usage: "+sys.argv[0]+" <From> <To> <Subject> <Message text> <path attachment>"
    sys.exit(0)
else:
    sendMail(sys.argv[1],sys.argv[2], sys.argv[3], sys.argv[4], [sys.argv[5]])


