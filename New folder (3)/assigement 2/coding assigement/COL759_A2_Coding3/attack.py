def attack(ciphertext, decrypt):    
    newct= ciphertext[0:16] + ([0] * 16) + ciphertext[0:16]
    message = list(decrypt(newct))
    start, last = message[:16], message[-16:]
    result = bytes([start[i] ^ last[i] for i in range(len(start))])
    return result
