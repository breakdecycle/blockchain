from hashlib import sha256
import sys
 
digits58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
 
def decode_base58(bc, length):
    n = 0
    for char in bc:
        n = n * 58 + digits58.index(char)
    return n.to_bytes(length, 'big')

def check_bc(bc):
	# function to check whether public address is valid
    bcbytes = decode_base58(bc, 25)
    return bcbytes[-4:] == sha256(sha256(bcbytes[:-4]).digest()).digest()[:4]


if __name__ == "__main__":
	print(check_bc(sys.argv[1]))