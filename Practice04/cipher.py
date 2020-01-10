import Practice04.VigenereCipher as vigenereCipher
import sys


def main(to_encrypt, encrypted, password):
    text_for_read = open(to_encrypt, 'r')
    text_for_write = open(encrypted, 'w')
    text_for_write.write(vigenereCipher.encrypt(text_for_read.read(), password))
    text_for_read.close()
    text_for_write.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
