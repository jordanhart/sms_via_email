import smtplib

class SendMessage:

    def __init__(self, address, password):
        self.username = address
        self.password = password

    def send_message(self, email, message, subject = "Text Message", from_address = "The Doctor"):

        fromaddr = self.username
        toaddrs  = email
        msg = "\n".join([
	  "From: " + from_address,
	  "To: "+email,
	  "Subject: " + subject,
	  "",
	  message
	  ])
        username = self.username
        password = self.password 
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        print('sent')

