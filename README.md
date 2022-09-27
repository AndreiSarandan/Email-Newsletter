This newsletter app takes advantage of the smtplib python library. Simple Mail Transfer Protocol is perfectly suited for this application.
We are using port 587 which is perfect for the secure submission of emails.
Here, the program loops through a database of email addresses and sends each of them a standard message.
However the text can easily be personalized for each address using python formatted strings.
For example we can call each reader by his name if it is stored in a database.

It is important to know that Gmail only allows user to log-in through a third party app using a generated 'App-password'
