from scapy.all import sniff

def analyze_packet(packet):
    if packet.haslayer('IP'):
        print(f"Source: {packet['IP'].src}, Dest: {packet['IP'].dst}, Proto: {packet['IP'].proto}")

sniff(prn=analyze_packet, count=10)
