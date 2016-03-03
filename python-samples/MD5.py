import hashlib

md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


sha = hashlib.sha1()
sha.update('how to use shal in'.encode('utf-8'))
sha.update('python hashlib?'.encode('utf-8'))
print(sha.hexdigest())
