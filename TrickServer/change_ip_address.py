import socks
import socket
from urllib.request import urlopen

'''
*** NOTE ***

1) Tor Browser 를 연결해 놓을 것!!
   ㄴ Tor Browser 다운로드 : https://www.torproject.org/download

2) 바뀐 IP 주소로 인터넷 이용 가능
'''

socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
socket.socket = socks.socksocket
print(urlopen('https://icanhazip.com/').read())
