import requests
from multiprocessing.pool import ThreadPool
import multiprocessing as Pool

url = "http://db.fizyka.pw.edu.pl/pwzn-data/zaj7/rand-data-b"
_iter=9

response = requests.head(url)
resp_len = int(response.headers['Content-Length'])
print(resp_len)
data = []
step = int(resp_len/_iter)

def process(arg):
    start, stop = arg
    response = requests.get("http://db.fizyka.pw.edu.pl/pwzn-data/zaj7/rand-data-b", 
                 headers = {"Range": "bytes={}-{}".format(start,stop)})
    
    return response


data = []
for i in range(_iter):
    data.append((i*step, i*step+step-1))
if data[-1][1] < resp_len:
    data.append((_iter*step, resp_len))    
print(data)

p = ThreadPool(_iter)
result = list(p.map(process, data))

collected = b"".join([d.content for d in result])



import hashlib
hash = hashlib.md5()
hash.update(collected)
print(hash.hexdigest())




    
#print(response.headers)
