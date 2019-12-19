import mailgun1
from boltiot import Email, Bolt
import json, time

minimum_limit = 30#the minimum threshold of light value 
maximum_limit = 50 #the maximum threshold of light value 


mybolt = Bolt(mail.API_KEY, mail.DEVICE_ID)
mailer = Email(mail.MAILGUN_API_KEY, mail.SANDBOX_URL, mail.SENDER_EMAIL, mail.RECIPIENT_EMAIL)


while True: 
    print ("Reading sensor value")
    response = mybolt.analogRead('A0') 
    data = json.loads(response) 
    print ("Sensor value is: " + str(data['value']))
    try: 
        sensor_value = int(data['value']) 
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Making request to Mailgun to send an mail")
            response = mailer.send_email("Alert", "The Current temperature sensor value is " +str(sensor_value))
            response_text = json.loads(response.text)
            print("Response received from Mailgun is: " + str(response_text['message']))
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(10)
