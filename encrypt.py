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
        '--recipients',
        help='Str/list(Str), Recipients for encrypted file',
        required=True
        )

    args = arg_parser.parse_args()

    encdc = encdec.EncDec(key=args.key)
    res = encdc.encrypt_file(
        file=args.file,
        recipients=args.recipients,
        destination=args.destination
        )

    print(res)