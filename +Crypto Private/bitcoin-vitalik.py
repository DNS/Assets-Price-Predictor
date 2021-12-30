
from bitcoin import *

priv = '5J8dPySx8e22RAwytUKUyeRCbQw5WXRpqKjjcexC35NHykCkwFr'

pub = privtopub(priv)
addr = pubtoaddr(pub)
wif = encode_privkey(priv, 'wif')
print(addr)
print(wif)

'''
### Listing of main commands:

    privkey_to_pubkey : (privkey) -> pubkey
    privtopub : (privkey) -> pubkey
    pubkey_to_address : (pubkey) -> address
    pubtoaddr : (pubkey) -> address
    privkey_to_address : (privkey) -> address
    privtoaddr : (privkey) -> address
    add : (key1, key2) -> key1 + key2 (works on privkeys or pubkeys)
    multiply : (pubkey, privkey) -> returns pubkey * privkey
    ecdsa_sign : (message, privkey) -> sig
    ecdsa_verify : (message, sig, pubkey) -> True/False
    ecdsa_recover : (message, sig) -> pubkey
    random_key : () -> privkey
    random_electrum_seed : () -> electrum seed
    electrum_stretch : (seed) -> secret exponent
    electrum_privkey : (seed or secret exponent, i, type) -> privkey
    electrum_mpk : (seed or secret exponent) -> master public key
    electrum_pubkey : (seed or secexp or mpk) -> pubkey
    bip32_master_key : (seed) -> bip32 master key
    bip32_ckd : (private or public bip32 key, i) -> child key
    bip32_privtopub : (private bip32 key) -> public bip32 key
    bip32_extract_key : (private or public bip32_key) -> privkey or pubkey
    deserialize : (hex or bin transaction) -> JSON tx
    serialize : (JSON tx) -> hex or bin tx
    mktx : (inputs, outputs) -> tx
    mksend : (inputs, outputs, change_addr, fee) -> tx
    sign : (tx, i, privkey) -> tx with index i signed with privkey
    multisign : (tx, i, script, privkey) -> signature
    apply_multisignatures: (tx, i, script, sigs) -> tx with index i signed with sigs
    scriptaddr : (script) -> P2SH address
    mk_multisig_script : (pubkeys, k, n) -> k-of-n multisig script from pubkeys
    verify_tx_input : (tx, i, script, sig, pub) -> True/False
    tx_hash : (hex or bin tx) -> hash
    history : (address1, address2, etc) -> outputs to those addresses
    unspent : (address1, address2, etc) -> unspent outputs to those addresses
    fetchtx : (txash) -> tx if present
    pushtx : (hex or bin tx) -> tries to push to blockchain.info/pushtx
    access : (json list/object, prop) -> desired property of that json object
    multiaccess : (json list, prop) -> like access, but mapped across each list element
    slice : (json list, start, end) -> given slice of the list
    count : (json list) -> number of elements
    sum : (json list) -> sum of all values


'''
