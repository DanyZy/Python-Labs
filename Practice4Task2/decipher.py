# the same problem with decrypt, but it should work
import Practice4Task1
import sys


def main(to_decrypt, decrypted, password):
    text_for_read = open(to_decrypt, 'r')
    text_for_write = open(decrypted, 'w')
    text_for_write.write(Practice4Task1.decrypt(text_for_read.read(), password))
    text_for_read.close()
    text_for_write.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
