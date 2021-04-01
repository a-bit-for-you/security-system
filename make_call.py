# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC0a9374cb2c0f3a81e930d11ff0d4a925'
auth_token = '22c0ec0ebc3596a42306e73e769000d8'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+918087387116',
                        from_='+14158257003'
                    )

print(call.sid)
