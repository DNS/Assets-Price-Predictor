
import base58

a = base58.b58encode(b'hello world')
b = base58.b58decode(b'StV1DL6CwTryKyV')

c = base58.b58encode_check(b'hello world')
d = base58.b58decode_check(b'3vQB7B6MrGQZaxCuFg4oh')

print(a)
print(b)
print(c)
print(d)




'''
def SHA256 ():
	

def RIPEMD160 ():
	

def p2pkh (ECDSA_publicKey):
	return RIPEMD160(SHA256(ECDSA_publicKey))

def p2sh (redeemScript):
	return RIPEMD160(SHA256(redeemScript))
'''

'''
Range of valid ECDSA private keys

Nearly every 256-bit number is a valid ECDSA private key. Specifically, any 256-bit number from 0x1 to 0xFFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFE BAAE DCE6 AF48 A03B BFD2 5E8C D036 4140 is a valid private key.

The range of valid private keys is governed by the secp256k1 ECDSA standard used by Bitcoin.



'''

