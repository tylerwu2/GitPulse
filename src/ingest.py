import requests

def fetch_data(url: str):
    response = requests.get(url)
    # automatically throws HTTPException if error occurs
    response.raise_for_status()
    # convert response to json output
    return response.json()