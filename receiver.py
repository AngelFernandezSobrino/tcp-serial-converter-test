
import socket

# Create a socket
print('Creating a socket')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)
print('Done')
# Connect to the remote host and port
print('Connecting to remote host...')
sock.connect(('10.40.0.5', 4196))
print('Done')



while True:
    try:
        # Get the host's response, no more than, say, 1,024 bytes
        print('Receiving data from host...')
        response_data = sock.recv(2049)
        response_string = str(response_data, 'utf-8')
        print("Received data: ", *[f'{char} ' for char in response_data])
        print("Received data type: ", type(response_data))
        print("Received data string: ", response_string)
        print("Received data string type: ", type(response_string))
        print('Done')
    except socket.timeout:
        print('No response from host')
    except KeyboardInterrupt:
        print('User interrupted')
        break

# Terminate
sock.close()