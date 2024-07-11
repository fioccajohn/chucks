import requests
from requests.exceptions import HTTPError
from functools import wraps

class APIError(Exception):
    """Base class for API errors."""
    pass

class APIClientError(APIError):
    """Exception raised for client errors (4xx)."""
    pass

class APIServerError(APIError):
    """Exception raised for server errors (5xx)."""
    pass

def handle_api_errors(func):
    """Decorator to handle API errors."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            response = func(self, *args, **kwargs)
            if 200 <= response.status_code < 300:
                return response.json()
            elif 400 <= response.status_code < 500:
                raise APIClientError(f"Client error: {response.status_code} - {response.text}")
            elif 500 <= response.status_code < 600:
                raise APIServerError(f"Server error: {response.status_code} - {response.text}")
            else:
                response.raise_for_status()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            # Handle other HTTP errors
        except APIClientError as client_err:
            print(f"API client error occurred: {client_err}")
            # Optionally, log or take specific actions based on the error
        except APIServerError as server_err:
            print(f"API server error occurred: {server_err}")
            # Optionally, log or take specific actions based on the error
        except Exception as err:
            print(f"An unexpected error occurred: {err}")
    return wrapper

class APIClient:
    """A class-based API client."""

    def __init__(self, base_url):
        self.base_url = base_url

    @handle_api_errors
    def request(self, method, endpoint, **kwargs):
        """General method for making API requests."""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, **kwargs)
        return response

    def get_data(self):
        """Fetch data from the /data endpoint and process the response."""
        response = self.request('GET', '/data')
        # Process the response as needed
        processed_data = self.process_data(response)
        return processed_data

    def get_user(self, user_id):
        """Fetch user data from the /users/{user_id} endpoint and process the response."""
        response = self.request('GET', f'/users/{user_id}')
        # Process the response as needed
        user_info = self.process_user(response)
        return user_info

    def create_user(self, user_data):
        """Create a new user with the provided user_data and process the response."""
        response = self.request('POST', '/users', json=user_data)
        # Process the response as needed
        created_user = self.process_user_creation(response)
        return created_user

    def process_data(self, data):
        """Process the data response."""
        # Example processing logic
        return data.get("results", [])

    def process_user(self, user_data):
        """Process the user response."""
        # Example processing logic
        return {
            "id": user_data.get("id"),
            "name": user_data.get("name"),
            "email": user_data.get("email"),
        }

    def process_user_creation(self, creation_response):
        """Process the user creation response."""
        # Example processing logic
        return {
            "id": creation_response.get("id"),
            "status": "User created successfully",
        }

# Example usage
if __name__ == "__main__":
    api_client = APIClient(base_url="https://api.example.com")
    try:
        data = api_client.get_data()
        print(data)
        
        user = api_client.get_user(user_id=1)
        print(user)
        
        new_user = {"name": "John Doe", "email": "john.doe@example.com"}
        created_user = api_client.create_user(new_user)
        print(created_user)
    except APIError as e:
        print(f"Failed to retrieve API data: {e}")
