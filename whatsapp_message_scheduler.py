# Step-1 install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Step-2 Twilio Credentials
account_sid = 'ACb205801dc2cc242867860793cf654de6d'
auth_token = '3057665b5c8c801411c0c866ca6480d70b'

client = Client(account_sid, auth_token)

# Step-3 design send message function
def send_whatsapp_message(recepient_number,message_body):
    try:
        message = client.messages.create(
            from_= 'whatsapp:+14155238886',
            body = message_body,
            to = f'whatsapp:{recepient_number}'
        )
        print(f'Message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An Error occurred..')    


# Step-4 User Input

name = input('Enter the recepient name = ')
receipent_number = input('Enter the receipent whatsapp number with country code (e.g, +91): ')
message_body = input(f'Enter the message you want to send to {name}: ')

# Step-5 parse Date/Time and calculate Delay

date_str =input('Enter the date to send the message (YYYY-MM-DD): ')
time_str =input('Enter the time to send the message (HH:MM in 24hour format): ')

# Datetime
schedule_datetime =datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")
current_datetime =datetime.now()

# Calculate Delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time: ')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

    #wait until the schedule time
    time.sleep(delay_seconds)

    #Send the message
    send_whatsapp_message(receipent_number,message_body)