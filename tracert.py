from scapy.all import *
hostname = "google.com"
for i in range(1, 255):
    pkt = IP(dst=hostname, ttl=i) / UDP(dport=33434)
    print(pkt.show())
    # Send the packet and get a reply
    reply = sr1(pkt, verbose=0)
    if reply is None:
        # No reply =(
        break
    elif reply.type == 3:
        # We've reached our destination
        print("Done!", reply.src)
        break
    else:
        # We're in the middle somewhere
        print("%d hops away: " % i , reply.src)