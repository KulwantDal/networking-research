from scapy.all import *
hostname = "google.com"

pkt = IP(dst=hostname, options=IPOption('\x07\x27\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')) / UDP(dport=33434)
print(pkt.show2())
print(sr1(pkt))