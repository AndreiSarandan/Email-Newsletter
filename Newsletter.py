import smtplib


def send_email(user, pwd, recipient, subject, body):
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient] #single or multiple addresses
    SUBJECT = subject
    CTEXT = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, CTEXT)
    try:
        server = smtplib.SMTP('smtp.gmail.com:587') #initialize connection to server
        server.ehlo() 
        server.starttls()
        server.login(user, pwd) #google account log-in
        server.sendmail(FROM, TO, message)#send email
        server.close() #close connection
        print('successfully sent the mail')
    except:
        print("failed to send mail")


user = 'newstester778@gmail.com'
pwd = 'dtfhspgkytcvyxju' #
subject = 'Test email'
with open('message.txt', 'r') as e:
    text = e.readlines()
with open('database.txt', 'r') as f:
    recipient = [line.strip() for line in f]

print(recipient)

send_email(user, pwd, recipient, subject, text)
