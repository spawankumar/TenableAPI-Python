import requests
from requests.auth import HTTPBasicAuth
# For in house hosted API
# Replace these values with your SecurityCenter information
Tenable_SERVER = 'https://securitycenter-server'
ACCESS_KEY = 'your-access-key'
SECRET_KEY = 'your-secret-key'
SCAN_ID = 1  # Replace with the ID of the scan you want to initiate

# API endpoint for initiating a scan
SCAN_ENDPOINT = f'{Tenable_SERVER}/rest/scan/{SCAN_ID}/launch'

# Set up the headers and authentication
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}
auth = HTTPBasicAuth(ACCESS_KEY, SECRET_KEY)

# Initiate the scan
try:
    response = requests.post(SCAN_ENDPOINT, headers=headers, auth=auth, verify=False)
    response.raise_for_status()
    print(f'Scan initiation successful. Response: {response.text}')
except requests.exceptions.HTTPError as err:
    print(f'Error initiating scan: {err}')
except Exception as e:
    print(f'An error occurred: {e}')
