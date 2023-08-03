import requests
from bs4 import BeautifulSoup
import time
import urllib3
from twilio.rest import Client

# Disable SSL certificate verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Twilio credentials
account_sid = 'AC4d2854118cd617f64e51ada8c08cea20'
auth_token = '63e037aa73b67632ff0538ed4263aa10'
twilio_phone_number = '+16672708587'
your_phone_number = '+923364424135'

def web_crawler(url):
    # Send a GET request to the website
    response = requests.get(url, verify=False)
    
    # Parse the HTML content of the website
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Get the initial state of the website's data
    initial_data = soup.get_text()
    
    while True:
        # Send a GET request to the website
        response = requests.get(url, verify=False)
        
        # Parse the HTML content of the website
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get the current state of the website's data
        current_data = soup.get_text()
        
        # Compare the current data with the initial data
        if current_data != initial_data:
            print("New data detected!")
            
            # Initialize the Twilio client
            client = Client(account_sid, auth_token)
            
            # Make a phone call
            call = client.calls.create(
                twiml='<Response><Say>New data detected on the website!</Say></Response>',
                to=your_phone_number,
                from_=twilio_phone_number
            )
            
            print("Phone call made!")
            
            # Update the initial data to the current data
            initial_data = current_data
        
        # Wait for a certain period of time before checking again
        time.sleep(1)  # Adjust the time interval as per your requirement

# Example usage
web_crawler("https://appointment24.w3spaces.com/")
