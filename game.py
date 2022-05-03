import socket
import random
import os

print('Hello, in this game you will hack')

ports = ['Port 80\n', 'Port 22\n', 'Port 52\n', 'Port 28\n']
random_open_ports = random.choice(ports)

process = 1

first_command = input('')

if first_command == 'help':
  print('Hah, first command a ip')
  first_command = input('')
  
if first_command == 'ip':
  hostname = socket.gethostname()
  local_ip = socket.gethostbyname(hostname)
  print(local_ip)

print('Nice, type port')
first_command = input('')

if first_command == 'port':
  print(ports)
  print(random_open_ports + "Open")
  print('Type hack Name port')
  
  hack_port = input()
  
  if hack_port == 'Port 80':
    print('It is not possible to hack a computer using this port')
  
  if hack_port == 'Port 22':
    print('WOHO HACKED')
  
  if hack_port == 'Port 52':
    print('It is not possible to hack a computer using this port')
    
  if hack_port == 'Port 28':
    print('It is not possible to hack a computer using this port')
    
print('oki, can you delete system? Yes. Type delete_system for delete files, or.... GO TO FILES, ahahhaahhah, for files go file_check')
first_command = input('')

if first_command == 'file_check':
  with open('chatlog.txt', 'r') as file:
    lines = file.read()

  with open('logs.txt', 'w') as file:
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    file.write(f'File Cheks, ip - {local_ip}')
    
  print(lines)
  print('wow... delete logs please) logs_delete, type this 2, oki?')
  first_command = input('')

if first_command == 'delete_system':
  print('deleted process...')
  while process < 101:
    print(process)
    process += 1


first_command = input('')

if first_command == 'logs_delete':
  os.remove('logs.txt')
  first_command = input('')
  
 
