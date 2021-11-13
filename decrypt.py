from encdec import encdec
import argparse

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        'Script for decrypting files with Private GPG key')
    arg_parser.add_argument(
        '--key',
        help='Str, Path to the destination of private key',
        required=True
        )
    arg_parser.add_argument(
        '--file', 
        help='Str, Path of the encrypted file',
         required=True
         )
    arg_parser.add_argument(
        '--destination', 
        help='Str, Path of the destination to store decrypted file', 
        required=True
        )
    arg_parser.add_argument(
        '--passd',
        help='Str, Password for private key',
        required=True
        )

    args = arg_parser.parse_args()

    encdc = encdec.EncDec(key=args.key)
    res = encdc.decrypt_file(
        file=args.file, 
        password=args.passd,
        destination=args.destination
        )
        
    print(res)
