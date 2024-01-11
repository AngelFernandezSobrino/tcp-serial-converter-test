
import socket

# Create a socket
print('Creating a socket')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(0.5)
print('Done')
# Connect to the remote host and port
print('Connecting to remote host...')
sock.connect(('10.40.0.4', 4196))
print('Done')

# Send a request to the host
print('Sending a packet to the host...')
send_message = b'ST,NT 10.00,kg\r\n'
print("Sending data: ", *[f'{char} ' for char in send_message])
sock.send(send_message)
print('Done')

# Terminate
sock.close(  )