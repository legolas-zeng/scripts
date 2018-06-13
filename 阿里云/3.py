import uuid
import hashlib

s_uuid=str(uuid.uuid1())
l_uuid=s_uuid.split('-')
s_uuid=''.join(str(uuid.uuid1()).split('-'))

print s_uuid

code = str(uuid.uuid1())
abc = code.split('-')
code = ''.join(abc)
print code
# print code

m = hashlib.md5()
m.update("/dev/release")
print m.hexdigest()

