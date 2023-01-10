# Example of how to configure SSH on Cisco switch:

enable
conf t
username konrad pass cisco
username konrad priv 15

line vty 0 4
  login local
  transport input all

ip domian-name cciepython.com
crypto key generate rsa
1024

end
write