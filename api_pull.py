import requests
import os
import json

def get_data_from_api():
    # TODO: Replace 'YOUR_API_ENDPOINT' with the actual API endpoint URL
    api_base_endpoint = 'https://api.sportsdata.io/v3/nfl/scores/json/'

    api_specific_endpoint = ['Timeframes/all']

    api_endpoint = api_base_endpoint + api_specific_endpoint[0]

    print(api_endpoint)
    
    # TODO: Replace 'YOUR_API_KEY' with the actual API key
    api_key = os.environ['api_key']

    # Construct the request headers with the API key
    headers = {
        "Ocp-Apim-Subscription-Key": api_key
    }

    try:
        # Make the HTTP GET request
        response = requests.get(api_endpoint, headers=headers)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Print the response data
            print('Response data:')

            api_response = response.json()

            print(json.dumps(api_response, indent = 2))
        else:
            # Print an error message if the request was not successful
            print(f'Error: Unable to fetch data. Status code: {response.status_code}')

    except requests.exceptions.RequestException as e:
        # Print an error message if an exception occurs during the request
        print(f'Error: {e}')

if __name__ == "__main__":
    get_data_from_api()
