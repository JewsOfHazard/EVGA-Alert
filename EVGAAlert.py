#Must use pip intall slackclient
#Github link: https://github.com/JewsOfHazard/EVGA-Alert

import imaplib
import time
import email
from slackclient import SlackClient

def send_slack_message(message):
	slackBot = SlackClient(slack_client_secret)
	slackBot.api_call("chat.postMessage", channel=slack_channel_id, text="{}".format(message), username=slack_username)


if __name__ == "__main__":

	from_email = 'WHATEVER EMAIL YOU WANT TO CHECK FOR'
	slack_message = 'WHATEVER YOU WANT TO SAY IN SLACK'
	slack_username = "YOUR SLACK BOT'S USERNAME HERE"
	slack_channel_id = 'YOUR SLACK CHANNEL ID HERE'
	slack_client_secret = "YOUR SLACK BOT's CLIENT SECRET HERE (xoxo-something)"
	email_username = 'YOUR GMAIL ACCOUNT LOGIN (with @gmail.com)'
	email_password = 'YOUR GMAIL PASSWORD'


	imap_conn = imaplib.IMAP4_SSL("imap.gmail.com")
	imap_conn.login(email_username,email_password)
	imap_conn.select("INBOX")

	esp, items = imap_conn.search(None, "(UNSEEN)")
	items = items[0].split()

	print "Message Checked"

	for emailid in items:
		resp, data = imap_conn.fetch(emailid, "(RFC822)") 
		email_body = data[0][1] 
		
		mail = email.message_from_string(email_body) 
		if mail["From"].find(from_email) is not -1:
			for i in range(10):
				send_slack_message(slack_message)
				time.sleep(.1)
		temp = imap_conn.store(emailid,'+FLAGS', '\Seen')
		imap_conn.expunge()
