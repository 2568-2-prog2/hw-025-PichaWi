import requests


def call_api(base_url, payload):
    """
    Calls the API to get a biased random number.

    Parameters:
        base_url (str): The base URL of the API.
        payload (dict): A dictionary containing the probability distribution.

    Returns:
        dict: The response from the API as a Python dictionary.
    """
    try:
        # Using POST method for proper HTTP protocol
        response = requests.post(base_url, json=payload)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        return None


if __name__ == "__main__":
    url = "http://127.0.0.1:8081/roll_dice"  # API URL

    # Example payload: Probabilities for dice faces 1 to 6
    data = {
        # Must sum to 1, requested by the user
        "probabilities": [0.1, 0.2, 0.3, 0.1, 0.2, 0.1],
        "number_of_random": 10  # Number of random values requested by the user
    }

    print("Calling the API with the following payload:")
    print(data)

    # Call the API and get the result
    result = call_api(url, data)
    print(f"Response type: {type(result)}")
    print(f"Response:\n{result}")

    if result and result.get('status') == 'success':
        print(f"\nRolled dice results: {result.get('dices')}")
        print(f"Number of rolls: {result.get('number_of_rolls')}")
        print(f"Probabilities used: {result.get('probabilities')}")
