import smtplib
import ssl


server = "smtp.gmail.com"
port = 465

senderEmail = "mymail@mail.com"
password = "my key"

addresses = open('emailAddresses.txt', 'r').readlines()

context = ssl.create_default_context()
with smtplib.SMTP(server, port) as mailer:
    # Setting debug level in order to get detailed information for debugging
    mailer.set_debuglevel(1)
    mailer.starttls(context=context)

    # Authentication
    mailer.login(senderEmail, password)
    if mailer.login == True:
        print("Successfully logged in")
    elif mailer.login == False:
        print("Could'nt Login")
    else:
        print("Network Disconnected")
    
    # Sending the email
    for line in addresses:
        firstName, lastName, address = line.split('\t')
        #toaddr = address
        receiverEmail = address #"receiver@mail.com"

        subject = "Subject: I'm Testing a mass mailer script\n"
        greeting = "Dear " + firstName + " " + lastName + ",\n"
        
        messageBody = open('textMessageBody.txt', 'r').read() #"\n Text email from Python."
        
        signature = "\n Best Regards,\n ParrotIghub"

        message = subject + "\n" + greeting + "\n" + messageBody + "\n" + signature
        
        mailer.sendmail(senderEmail, receiverEmail, message)
        
        if mailer.login == True:
            print("Successfully logged in")
        elif mailer.login == False:
                print("Could'nt Login")
        else:
            print("Network Disconnected")