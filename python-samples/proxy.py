import urllib.request
with urllib.request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data=f.read()
    print('Status',f.status,f.reason)
    for k,v in f.getheaders():
        print('{0}:{1}'.format(k,v))
    print('Data',data.decode('utf-8'))
