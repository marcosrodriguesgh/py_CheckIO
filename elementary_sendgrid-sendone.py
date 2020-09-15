import sendgrid
from sendgrid.helpers.mail import Mail, Content

API_KEY = ''
SUBJECT = 'Welcome'
BODY = 'Hi {}'

sg = sendgrid.SendGridAPIClient(API_KEY)


def send_email(email, name):
    msg = Mail(
        from_email='marcos@mettecnologia.com.br',
        to_emails=email,
        subject=SUBJECT,
        plain_text_content=BODY.format(name)
    )

    try:
        response = sg.send(msg)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    send_email('somebody@gmail.com', 'Some Body')
    print('Done')
