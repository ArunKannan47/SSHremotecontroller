
from paramiko import SSHClient, AutoAddPolicy

client = SSHClient()
# host key is a cryptographic key used for authenticating computers in the SSH protocol 
client.set_missing_host_key_policy(AutoAddPolicy())
#connecting to client
client.connect('169.254.16.134',username='pi', password='raspberry')
#remote command execution on client
stdin, stdout, stderr = client.exec_command("python3 /home/pi/hello.py")
#decoding stdout
print(f'STDOUT: {stdout.read().decode("utf8")}')

stdin.close()
stdout.close()
stderr.close()
client.close()
