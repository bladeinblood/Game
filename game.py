import socket
import random

print('Hello, in this game you will hack')

random_open_ports = random.choice(ports)
ports = ['Port 80\n', 'Port 70\n', 'Port 52\n', 'Port 28\n']

process = 1

def command():
  first_command = input('')

if first_command == 'help':
  print('Hah, first command a ip')
  command()
  
if first_command == 'ip':
  hostname = socket. gethostname()
  local_ip = socket. gethostbyname(hostname)
  print(local_ip)

print('Nice, type port')
command()

if first_command == 'port':
  print(ports)
  print(random_open_ports + "Open")
  print('Type hack Name port')
  
  hack_port = input()
  
  if hack_port == 'Port 80':
    print('It is not possible to hack a computer using this port')
  
  if hack_port == 'Port 70':
    print('WOHO HACKED')
  
  if hack_port == 'Port 52':
    print('It is not possible to hack a computer using this port')
    
  if hack_port == 'Port 28':
    print('WOHO HACKED')
    
print('oki, can you delete system? Yes. Type delete_system for delete files')
command()

if first_command == 'delete_system':
  print('deleted process...')
  while process < 101:
    print(process)
    process += 1
  
 
