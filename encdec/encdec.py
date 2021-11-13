import gnupg

class EncDec:
    """
    Module for encrypting and decrypting files and data with assymetric GPG RSA keys

    Parameters
    ----------
        key: Str, Path to the location containing the public key(in case of encryption) or private key(in case of decryption)
    """
    def __init__(self, key: str) -> None:
        self.gpg = gnupg.GPG()
        with open(key, 'rb') as f:
            key_data = f.read()
        result = self.gpg.import_keys(key_data)

    def encrypt(self, data, recipients: str):
        """
        Method to encrypt data using public key

        Parameters
        ----------
            data: Byte like object
                Data to be encrypted
            
            recipients: Str
                Recipients for encrypted file
        
        Returns
        -------
            encrypted_data: Byte like object
                GPG encrypted data
            
            (encrypted_data.ok, encrypted_data.stderr): tuple
                Status of encryption

        """
        encrypted_data = self.gpg.encrypt(data=data, recipients=[recipients])
        return encrypted_data, (encrypted_data.ok, encrypted_data.stderr)

    def decrypt(self, data, password: str):
        """
        Method to decrypt data using private key

        Parameters
        ----------
            data: Byte like object
                Data to be encrypted
            
            password: Str
                Password for private key
        
        Returns
        -------
            decrypted_data: Byte like object
                GPG decrypted data in original data format
            
            (decrypted_data.ok, decrypted_data.stderr): tuple
                Status of decryption

        """
        decrypted_data = self.gpg.decrypt(data, passphrase=password)
        return decrypted_data, (decrypted_data.ok, decrypted_data.stderr)

    def encrypt_file(self, file: str, recipients: str, destination: str):
        """
        Method to encrypt a file using public key

        Parameters
        ----------
            file: Str
                Path to the file to be encrypted
            
            recipients: Str
                Recipients for encrypted file

            destination: Str
                Path to the file to store encrypted file

        Returns
        -------
            ValueError or tuple:
                Status of file encryption
        """
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
        """
        Method to decrypt a file using private key

        Parameters
        ----------
            file: Str
                Path to the file to be encrypted
            
            password: Str
                Password for private key

            destination: Str
                Path to the file to store decrypted file

        Returns
        -------
            ValueError or tuple:
                Status of file decryption
        """
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

    