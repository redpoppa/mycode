#!/user/bin/env python3

import paramiko

def commandissue(command_to_issue):
  ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
  return ssh_stdout



ssh = paramiko.SSHClient()
ssh.connect(server, username=unsername, password=password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("ps aux | grep")
print("Results of your command was", ssh_stdout)




####### IF USING KEYS ######


mykey = paramiko.RSAKey.from_private_key_file(keyfilename)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username= user, pkey=mykey)

james_cmds = ["cd", "df -k", "ps aux | grep neutron"]


for cmd in james_cmds:
  print(commandissue(cmd)
