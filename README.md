# sms_via_email
Send sms via gmail account

example of use for T-Mobile:

send = SendMessage("GMAIL USERNAME@GMAIL.COM", "PASSWORD")
send.send_message("+1NUMBER@tmomail.net", "MESSAGE")

should print "sent"

If login does not work, or gives you weird long error, go to 
this link https://www.google.com/settings/security/lesssecureapps
and turn on "Access for less secure apps"
