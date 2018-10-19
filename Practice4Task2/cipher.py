# it's a bit confusing, but i can not properly import my last lab without any errors in cmd
# I mast leave the import as it is, with annoying red underline
import Practice4Task1
import sys


def main(to_encrypt, encrypted, password):
    text_for_read = open(to_encrypt, 'r')
    text_for_write = open(encrypted, 'w')
    text_for_write.write(Practice4Task1.encrypt(text_for_read.read(), password))
    text_for_read.close()
    text_for_write.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
