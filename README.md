# sms_via_email
Send sms via gmail account

example of use for T-Mobile:

sendmail = SendEmail("GMAIL USERNAME@GMAIL.COM", "PASSWORD")
sendmail.send_email("+1NUMBER@tmomail.net", "MESSAGE")

should print "sent"
