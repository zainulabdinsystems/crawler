import requests
from bs4 import BeautifulSoup
import time
import urllib3

# Disable SSL certificate verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
            # Perform any desired actions when new data is detected
            
            # Update the initial data to the current data
            initial_data = current_data
        
        # Wait for a certain period of time before checking again
        time.sleep(1)  # Adjust the time interval as per your requirement

# Example usage
web_crawler("https://appointment24.w3spaces.com/")
