# importing binascii to be able to convert hexadecimal strings to binary data
import binascii, hashlib, base58

# Step 1: here we have the private key
#private_key_static = "29a59e66fe370e901174a1b8296d31998da5588c7e0dba860f11d65a3adf2736"
#private_key_static = "0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D"
private_key_static = "0000000000000000000000000000000000000000000000000000000000000000"
# Step 2: let's add 80 in front of it
extended_key = "80"+private_key_static
# Step 3: first SHA-256
first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
# Step 4: second SHA-256
second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
# Step 5-6: add checksum to end of extended key
final_key = extended_key+second_sha256[:8]
# Step 7: finally the Wallet Import Format is the base 58 encode of final_key
WIF = base58.b58encode(binascii.unhexlify(final_key))
print (WIF)

