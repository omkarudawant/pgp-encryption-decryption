import gnupg

class EncDec:
    def __init__(self, key) -> None:
        self.gpg = gnupg.GPG()
        with open(key, 'rb') as f:
            key_data = f.read()

        result = self.gpg.import_keys(key_data)
        print(result.results)

    def encrypt(self, data, recipients):
        encrypted_data = self.gpg.encrypt(data=data, recipients=[recipients])
        return encrypted_data, (encrypted_data.ok, encrypted_data.stderr)

    def decrypt(self, data, password):
        decrypted_data = self.gpg.decrypt(data, passphrase=password)
        return decrypted_data, (decrypted_data.ok, decrypted_data.stderr)

    def encrypt_file(self, file, recipients, destination):
        with open(file, 'rb') as f:
            result = self.gpg.encrypt_file(
                f,
                recipients=[recipients],
                output=destination
                )

        if not result.ok:
            raise ValueError(f'Could not encrypt file !\n{result.stderr}')
        else:
            return result.ok, result.status

    def decrypt_file(self, file, password, destination):
        with open(file, 'rb') as f:
            result = self.gpg.decrypt_file(
                f, 
                passphrase=password,
                output=destination
                )

        if not result.ok:
            raise ValueError(f'Could not encrypt file !\n{result.stderr}')
        else:
            return result.ok, result.status

    