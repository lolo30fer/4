from scapy.all import *

from scapy.layers import http
from bs4 import BeautifulSoup
soup = BeautifulSoup()
def ssf(x):
    if x and x.haslayer('UDP') and x.haslayer('DNS') and not x=="":
        print(x[2].show())
        #ssi=x[2].split("rrname")
        #print(ssi)
    
sniff(prn=ssf)