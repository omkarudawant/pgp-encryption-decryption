from encdec import encdec

encdc = encdec.EncDec(key='GPG_Testing/private.key')

res = encdc.encrypt_file(file='test_file.txt', recipients='omkar@test.com', destination='encrypted.encrypt')
print(res)