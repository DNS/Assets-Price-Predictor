
import hashlib
import bech32


sha256 = hashlib.new('sha256')
sha256.update(b'0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798')


a = sha256.hexdigest()

print(a)
