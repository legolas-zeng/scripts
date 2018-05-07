import uuid
import hashlib

s_uuid=str(uuid.uuid1())
l_uuid=s_uuid.split('-')
s_uuid=''.join(l_uuid)

print s_uuid

code = str(uuid.uuid1())
abc = code.split('-')
code = ''.join(abc)
print code
# print code


m = hashlib.md5()
m.update("cn-beijing")
print m.hexdigest()

