from netmiko import ConnectHandler

#dictionary, object
Router = {
    "device_type": "cisco_ios",
    "ip": "10.18.8.150",
    "username": "vnpro",
    "password": "vnpro#123",
    "secret": "vnpro#321"
}
#user, privileges, config

# ConnectHandler(**Router)
# ConnectHandler(**Router).send_command("show ip interface brief")
# print(ConnectHandler(**Router).send_command("show ip interface brief"))

connect = ConnectHandler(**Router)
connect.enable()

#send command function
#print(connect.send_command("show run")

#send config set functio
#print(connect.send_config_set("hostname R1-AnhND"))
      
#print(connect.send_config_set(["int e0/2","no shut","ip add 192.168.100.100 255.255.255.0"]))

# use for loop
for i in range(1, 4):
    print(connect.send_config.set(["int e0/" + str(i),"no shut","ip add 192.168." + str(i)"100 255.255.255.0"]))




#disconnect
connect.disconnect()