import os
import binascii
import ecdsa
import hashlib
import base58


def gen_add():
	s = binascii.hexlify(os.urandom(32))

	Private_key = bytes.fromhex(s.decode())
	print("this is the private key: " + str(Private_key))

	signing_key = ecdsa.SigningKey.from_string(Private_key, curve = ecdsa.SECP256k1)
	print("this is the signing key: " + signing_key.to_string().hex())

	verifying_key = signing_key.get_verifying_key()
	print("this is the vk: " + verifying_key.to_string().hex())

	public_key = bytes.fromhex("04") + verifying_key.to_string()
	print ("this is the public key: " + public_key.hex())


	sha256_1 = hashlib.sha256(public_key)

	ripemd160 = hashlib.new("ripemd160")
	ripemd160.update(sha256_1.digest())

	hashed_public_key = bytes.fromhex("00") + ripemd160.digest()
	print("this is the hashed public key: " + hashed_public_key.hex())

	checksum_full = hashlib.sha256(hashlib.sha256(hashed_public_key).digest()).digest()
	print("this is my full checksum (32 bytes, I only need 4 bytes): " + checksum_full.hex())

	checksum = checksum_full[:4]
	print ("this is the real check sum only 4 bytes long: " + checksum.hex())

	bin_addr = hashed_public_key + checksum
	print("this is my bin_addr: " + bin_addr.hex())


	FINAL_BTC_ADDRESS = base58.b58encode(bin_addr)
	print ("this is my bitcoin address: " + FINAL_BTC_ADDRESS)

	return(FINAL_BTC_ADDRESS, signing_key.to_string().hex())


def check_key(publicKey, privateKey):
	if type(publicKey) == str and type(privateKey) == str:
		new_key =  bytes.fromhex(privateKey)
		print('New Key is {}'.format(new_key))
		signing_key = ecdsa.SigningKey.from_string(new_key, curve=ecdsa.SECP256k1)
		print("this is the signing key: " + signing_key.to_string().hex())

		verifying_key = signing_key.get_verifying_key()
		public_key = bytes.fromhex("04") + verifying_key.to_string()
		sha256_1 = hashlib.sha256(public_key)
		ripemd160 = hashlib.new("ripemd160")
		ripemd160.update(sha256_1.digest())
		hashed_public_key = bytes.fromhex("00") + ripemd160.digest()
		checksum_full = hashlib.sha256(hashlib.sha256(hashed_public_key).digest()).digest()
		checksum = checksum_full[:4]
		bin_addr = hashed_public_key + checksum
		FINAL_BTC_ADDRESS = base58.b58encode(bin_addr)

		if FINAL_BTC_ADDRESS == publicKey:
			return True
		return False

	else:
		print('Wrong argument type. String expected.')



if __name__ == "__main__":
	print(gen_add())

	# print(check_key('1nHD21SgMYph5izGqKmrwHKvHekbeBwdj', '0eb4c2a4cfc6916ec159486e6ad1f1bdb5181a9e9c576382d9146edb57002c0c'))