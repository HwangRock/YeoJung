import requests

BASE_URL = "http://localhost:8080"

def fetch_test():
    try:
        response = requests.post(f"{BASE_URL}/test")
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Exception: {str(e)}"
