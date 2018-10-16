import unittest


def del_surplus_symb(password, len_pas):
    for i in range(len_pas):
        del password[-1]
    return password


def encrypt(open_text, password, alphabet='abcdefghijklmnopqrstuvwxyz'):
    alphabet = list(alphabet)
    open_text = open_text.split(' ')
    open_text = ''.join(open_text)
    open_text = list(open_text)
    password = del_surplus_symb(list(password) + open_text, len(open_text))
    i = 0
    for el in open_text:
        open_text[i] = alphabet[(alphabet.index(el) + alphabet.index(password[i])) % len(alphabet)]
        i += 1
    return ''.join(open_text)


def decrypt(ciphered_text, password, alphabet='abcdefghijklmnopqrstuvwxyz'):
    alphabet = list(alphabet)
    ciphered_text = ciphered_text.split(' ')
    ciphered_text = ''.join(ciphered_text)
    ciphered_text = list(ciphered_text)
    if len(ciphered_text) > len(password):
        password = list(password)
        j = 0
        for el in ciphered_text:
            if j < len(ciphered_text) - len(password):
                if alphabet.__contains__(el):
                    # добавлять не зашифрованный хвост к ключу, а просто кучок открытого сообщения
                    password.append(alphabet[(alphabet.index(el) - alphabet.index(password[j])) % len(alphabet)])
                    j += 1
    i = 0
    for el in ciphered_text:
        if alphabet.__contains__(el):
            ciphered_text[i] = alphabet[(alphabet.index(el) - alphabet.index(password[i])) % len(alphabet)]
            i += 1
    return ''.join(ciphered_text)


class TestVigener(unittest.TestCase):
    def test_empty(self):
        text = ''
        pwd = ''
        self.assertEqual((decrypt(text, pwd)), text)
        self.assertEqual((encrypt(text, pwd)), text)

    def test_one(self):
        text = 'codewars'
        pwd = 'password'
        cipher = 'rovwsoiv'
        self.assertEqual(encrypt(text, pwd), cipher)

    def test_two(self):
        text = 'waffles'
        pwd = 'password'
        cipher = 'laxxhsj'
        self.assertEqual(decrypt(cipher, pwd), text)

    def text_third(self):
        text = 'amazingly few discotheques provide jukeboxes'
        pwd = 'password'
        cipher = 'pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib'
        self.assertEqual(decrypt(cipher, pwd), text)
        self.assertEqual(encrypt(text, pwd), cipher)


if __name__ == '__main__':
    unittest.main()
