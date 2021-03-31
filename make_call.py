# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACfcf5e562c6cccfcc76c2679c0ab31ec5'
auth_token = 'ac55d09fe5e59bbe9fc3ae2517e5be54'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+917276317717',
                        from_='+12408580473'
                    )

print(call.sid)
