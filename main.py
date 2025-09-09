import hashlib
s='netcloud'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
