from scrapli import Scrapli
from scrapli.logging import enable_basic_logging
import os
from dotenv import load_dotenv

load_dotenv()

enable_basic_logging(file=True, level="debug")

huawei_device = {
    "host": os.getenv("huawei_host", "xxxx"),
    "auth_username": os.getenv("huawei_auth_username", "xxxx"),
    "auth_password": os.getenv("huawei_auth_password", "xxxx"),
    "auth_strict_key": False,
    "platform": os.getenv("huawei_device_type", "huawei_vrp")
}
conn = Scrapli(**huawei_device)
conn.open()
responses = conn.send_commands(["display arp"])

for response in responses:
    print(response.result)
conn.close()

cisco_device = {
    "host": os.getenv("cisco_host", "xxxx"),
    "auth_username": os.getenv("cisco_auth_username", "xxxx"),
    "auth_password": os.getenv("cisco_auth_password", "xxxx"),
    "auth_secondary": os.getenv("cisco_auth_secondary", "xxxx"),
    "auth_strict_key": False,
    "platform": os.getenv("cisco_device_type", "cisco_iosxe"),
    "transport": "ssh2",
    # transport_options指定额外的ssh连接参数
    "transport_options": {"open_cmd": [
        "-o", "KexAlgorithms=+diffie-hellman-group1-sha1",
        "-o", "Ciphers=aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc"]}
}

conn2 = Scrapli(**cisco_device)

# 自定义正则匹配字符串
# conn2.privilege_levels[
#     'configuration'].pattern = r"^.*\[confirm\]|^[a-zA-Z0-9.\-@\/:]{1,32}\(conf[a-z0-9.\-@\/:]{0,32}\)#$"
# conn2.update_privilege_levels()
##
conn2.open()
responses = conn2.send_commands(["show arp"])

for response in responses:
    print(response.result)
conn2.close()
