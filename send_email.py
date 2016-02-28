import smtplib

class SendEmail:

    def __init__(self, address, password):
        self.username = address
        self.password = password

    def send_mail(self, email, message):

        fromaddr = self.username
        toaddrs  = email
        msg = "\r\n".join([
          "To: "+email,
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

