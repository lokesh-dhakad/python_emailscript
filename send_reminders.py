import datetime
import email
import smtplib
import sys

def usage():
    print("send_reminders: Send Meeting Reminders")
    print()
    print("Invocation:")
    print("    send_reminders 'date|Meeting Title|Emails' ")
    return 1

def dow(date):
    dateobj=datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strftime("%A")

def message_template(date, title):
    message=email.message.EmailMessage()
    weekday=dow(date)
    message['Subject']=f'Meeting reminder:"{title}"'
    message.set_content(f'''
Hi all!
This is a a quickmail remind you about a quick meeting:"{title}"
the {weekday} {date}.

See you there....
''')
    return message

def send_message(message, emails):
    smtp=smtplib.SMTP('localhost')
    message['From']='noreply@example.com'
    for email in emails.split(','):
        del message['To']
        message['To'] = email
        smtp.send_message(message)
    smtp.quit()
    pass

def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split('|')
        message=message_template(date, title)
        send_message(message, emails)
        print("Successfully send to: ", emails)
    except Exception as e:
        print("Failure to send email with: {}".format(e), file=sys.stderr)

if __name__=="__main__":
    sys.exit(main())
