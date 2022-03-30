from netmiko import Netmiko
import os


cisco_host = {
    'host':   os.getenv("cisco_host"),
    'device_type': os.getenv("cisco_device_type"),
    "username": os.getenv("cisco_auth_username", "xxxx"),
    "password": os.getenv("cisco_auth_password", "xxxx"),
    "secret": os.getenv("cisco_auth_secondary", "xxxx"),
    'port': '22',
    "global_delay_factor": 0.1
}


net_connect = Netmiko(**cisco_host)
print("Connected to:", net_connect.find_prompt()
      )

v4_commands = ["show arp"]

display = net_connect.send_config_set(
    config_commands=v4_commands, enter_config_mode=False)

print(display)

net_connect.disconnect()
