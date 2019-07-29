import os
import smtplib
import requests
from linode_api4 import LinodeClient, Instance



EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')


# for linode in client.linode.instance():
#     print(f'{linode.label}: {linode.id}') to get the server instance


def notify_user():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = 'YOUR SITE IS DOWN'
        body = 'Site is down, do the necessary check.'
        msg = f'Subject: {subject} \n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS, 'jrumpe@parl.co.ke', msg)


def reboot_server():
    client = LinodeClient(LINODE_TOKEN)
    my_server = client.load(Instance, 376715)
    my_server.reboot()

try:
    r = requests.get('https://parl.co.ke', timeout=5)

    if r.status_code != 200:
        notify_user()
        reboot_server()

except Exception as e:
    notify_user()
    reboot_server()




