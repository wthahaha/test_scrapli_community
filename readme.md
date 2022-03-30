## 演示通过scrapli-community连接网络设备

### 优点
#### 比netmiko更快，输出比paramiko更友好

### 缺点
#### 兼容性还不够好，支持的设备型号不如netmiko丰富，但应付常用的网络设备足够了

### 使用方法

```shell

pip install -r requirements.txt

python test_scrapli.py

```

### 代码中有额外连接参数使用示例