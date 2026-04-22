import socket
import json
from dice import RandomDice

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server socket to an IP address and port
server_socket.bind(('localhost', 8081))

# Start listening for incoming connections
server_socket.listen(1)
print("Server is listening on port 8081...")

# Accept incoming client connections
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} established.")

    # Receive the HTTP request from the client
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Request received ({len(request)}):")
    print("*"*50)
    print(request)
    print("*"*50)

    # Check if the request is a POST request to /roll_dice
    if request.startswith("POST /roll_dice"):
        try:
            body_start = request.find('\r\n\r\n')
            if body_start != -1:
                json_body = request[body_start + 4:]
                payload = json.loads(json_body)
                if not isinstance(payload, dict):
                    response_data = {"status": "error", "message": "Invalid JSON format"}
                else:
                    probabilities = payload.get('probabilities')
                    if probabilities is None:
                        response_data = {"status": "error",
                                         "message": "Missing probabilities"}
                    else:
                        number_of_rolls = payload.get('number_of_random', 1)

                        dice = RandomDice(probabilities)
                        dice_rolls = dice.Roll(number_of_rolls)

                        response_data = {
                            "status": "success",
                            "probabilities": probabilities,
                            "number_of_rolls": number_of_rolls,
                            "dices": dice_rolls
                        }
            else:
                response_data = {"status": "error",
                                 "message": "Invalid request format"}
        except (json.JSONDecodeError, ValueError) as e:
            response_data = {"status": "error", "message": str(e)}

        # Convert dictionary to JSON string
        response_json = json.dumps(response_data)

        # HTTP response with JSON content
        response = f"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: {len(response_json)}\r\n\r\n{response_json}"
    elif request.startswith("GET"):
        # Prepare an HTTP response (basic HTML)
        response = f"""HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Hello, World!</h1><hr>{request}</body></html>"""
    else:
        # Respond with a 405 Method Not Allowed if not a GET or POST request
        response = "HTTP/1.1 405 Method Not Allowed\r\n\r\n"

    # Send the HTTP response to the client
    client_socket.sendall(response.encode('utf-8'))

    client_socket.close()  # Close the client connection

    print("Waiting for the next TCP request...")
