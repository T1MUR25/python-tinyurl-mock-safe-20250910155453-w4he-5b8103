import hashlib
s='safecloud'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
