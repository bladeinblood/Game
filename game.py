import socket
import random
import os

print('Hello, in this game you will hack')

random_open_ports = random.choice(ports)
ports = ['Port 80\n', 'Port 22\n', 'Port 52\n', 'Port 28\n']

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
  
  if hack_port == 'Port 22':
    print('WOHO HACKED')
  
  if hack_port == 'Port 52':
    print('It is not possible to hack a computer using this port')
    
  if hack_port == 'Port 28':
    print('It is not possible to hack a computer using this port')
    
print('oki, can you delete system? Yes. Type delete_system for delete files, or.... GO TO FILES, ahahhaahhah, for files go file_check')
command()

if first_command == 'file_check':
  with open('chatlog.txt', 'w') as file:
    file.write('[SNOWLORD] Hello streamer\n')
    file.write('[SNOWLORD] How are you?\n')
    file.write('[STREAMER] Fine... wbu?\n')
    file.write('[SNOWLORD] Me fine too\n')
    file.write('[SNOWLORD] Ohhh, sorry but i have to exit, bye\n')
    file.write('[STREAMER] Bye, Snowlord\n')
    
    lines = f.read()
    
  print(lines)

if first_command == 'delete_system':
  print('deleted process...')
  while process < 101:
    print(process)
    process += 1
  
 
