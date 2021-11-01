import scapy.all as scapy
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast.arp_request
    answer_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=false)[0]

    client_list = []
    for packet in answer_list:
        client_dt = {"ip": packet[1].psrc, "mac": packet[1].hwsrc}
        client_list.append(client_dt)
        return client_list
def print_result(result):
     print("++++++++++++++++++++++++++++++++++++++++++++++++")
    print("IP\t\t\tMAC Address\n-----------------------")
    for users in result_list:
        print(users["ip"] + "\t\t" + users["mac"])

scan_result = scan("10.0.2.1/24")
print_result(scan_result)
