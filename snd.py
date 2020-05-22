# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY='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'

message = Mail(
    from_email='god@nachorny.design',
    to_emails='astroboye50@gmail.com',
    subject='touchmethere',
    html_content='<strong>frogs</strong>')
try:
    sg = SendGridAPIClient(os.environ.get(SENDGRID_API_KEY))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
