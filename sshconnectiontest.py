# import paramiko

# p = paramiko.SSHClient()
# p.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # This script doesn't work for me unless this line is added!
# p.connect("ubuntu.local", port=22, username="arunkannan", password="sherlockholmes")
# stdin, stdout, stderr = p.exec_command("your command")
# opt = stdout.readlines()
# opt = "".join(opt)
# print(opt)


# remote = paramiko.SSHClient()
# remote.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# remote.connect("host", username="uname", password="pwd")
 
# # myScript produces continuous output, that I want to capture as it appears    
# stdin, stdout, stderr = remote.exec_command("python myScript.py")
# stdin.close()
# for line in stdout.read().splitlines():
#     print(line)

# import subprocess
# proc = subprocess.call(["ssh","pi@192.168.4.1","python3 /home/pi/desktop/python_server/python_server.py"],stdout=subprocess.PIPE)
# while True:
#    line = proc.stdout.readline()
#    if not line:
#       break
#    print("test:", line.rstrip())
# def execute():
#        stdin.write('xcommand SystemUnit Boot Action: Restart\n')
#        print('success')

# execute()


import paramiko
import time

client = paramiko.SSHClient()
#ssh.load_system_host_keys()
# host key is a cryptographic key used for authenticating computers in the SSH protocol     
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('169.254.16.134', port=22, username='pi', password='raspberry')

time.sleep(5)
print('connected')
stdin, stdout, stderr = client.exec_command("python3 /home/pi/hello.py")
print(f'STDOUT: {stdout.read().decode("utf8")}')
stdin.close()
stdout.close()
stderr.close()
client.close()


