"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
from mitmproxy import ctx, http
from typing import Iterable, Union

class Counter:

    def modify(self, data: bytes) -> Union[bytes, Iterable[bytes]]:
        print('----------------------------------------->', 'modify')
        data2 = data.replace(b"https://201.151.252.116:9105", b"http://201.151.252.116:9105")
        print('data2 ready')
        return data2

    def request(self, flow):

        # url = flow.request.url.split('/')[:3]
        # print('\n\n\n\n', url, '\n\n\n\n\n')
        # if url[-1] == '192.168.1.199:8000':
        #     flow.request.url = 'http://example.com'

        if flow.request.pretty_host == "201.151.252.116":

            if flow.request.port == 9105:
                flow.request.port = 80

            flow.request.host = "192.168.1.199"
            ctx.log.info("\n-----> Cached redirect\n")


    def responseheaders(self, flow):
        # print(other)
        flow.response.stream = self.modify

addons = [
    Counter()
]
