import unittest


def add_spaces(text_w_space, text_wo_space, alphabet='abcdefghijklmnopqrstuvwxyz'):
    for i, el in enumerate(text_w_space):
        if not alphabet.__contains__(el):
            text_wo_space.insert(i, el)
    return text_wo_space


def del_surplus_symbols_in_text(text, alphabet='abcdefghijklmnopqrstuvwxyz'):
    text = list(text)
    clear_text = []
    for el in text:
        if alphabet.__contains__(el):
            clear_text.append(el)
    return clear_text


def del_surplus_symbols_in_password(password, len_pas):
    for i in range(len_pas):
        del password[-1]
    return password


def encrypt(open_text, password, alphabet='abcdefghijklmnopqrstuvwxyz'):
    alphabet = list(alphabet)
    text = open_text
    open_text = del_surplus_symbols_in_text(open_text, alphabet)
    password = del_surplus_symbols_in_password(list(password) + open_text, len(password))
    i = 0
    for el in open_text:
        open_text[i] = alphabet[(alphabet.index(el) + alphabet.index(password[i])) % len(alphabet)]
        i += 1
    open_text = add_spaces(text, open_text, alphabet)
    return ''.join(open_text)


def decrypt(ciphered_text, password, alphabet='abcdefghijklmnopqrstuvwxyz'):
    alphabet = list(alphabet)
    text = ciphered_text
    ciphered_text = del_surplus_symbols_in_text(ciphered_text, alphabet)
    len_pass = len(password)
    if len(ciphered_text) > len(password):
        password = list(password)
        j = 0
        for el in ciphered_text:
            if j < len(ciphered_text) - len_pass:
                if alphabet.__contains__(el):
                    password.append(alphabet[(alphabet.index(el) - alphabet.index(password[j])) % len(alphabet)])
                    j += 1
    i = 0
    for el in ciphered_text:
        if alphabet.__contains__(el):
            ciphered_text[i] = alphabet[(alphabet.index(el) - alphabet.index(password[i])) % len(alphabet)]
            i += 1
    ciphered_text = add_spaces(text, ciphered_text, alphabet)
    return ''.join(ciphered_text)


class TestVigener(unittest.TestCase):
    def test_empty(self):
        text = ''
        pwd = ''
        cipher = ''
        self.assertEqual(decrypt(cipher, pwd), text)
        self.assertEqual(encrypt(text, pwd), cipher)

    def test_one(self):
        text = 'codewars'
        pwd = 'password'
        cipher = 'rovwsoiv'
        self.assertEqual(decrypt(cipher, pwd), text)
        self.assertEqual(encrypt(text, pwd), cipher)

    def test_two(self):
        text = 'waffles'
        pwd = 'password'
        cipher = 'laxxhsj'
        self.assertEqual(decrypt(cipher, pwd), text)
        self.assertEqual(encrypt(text, pwd), cipher)

    def test_third(self):
        text = 'amazingly few discotheques provide jukeboxes'
        pwd = 'password'
        cipher = 'pmsrebxoy rev lvynmylatcwu dkvzyxi bjbswwaib'
        self.assertEqual(decrypt(cipher, pwd), text)
        self.assertEqual(encrypt(text, pwd), cipher)

    def test_fourth(self):
        text = 'amazingly few\n discotheques\n provide\n jukeboxes'
        pwd = 'password'
        cipher = 'pmsrebxoy rev\n lvynmylatcwu\n dkvzyxi\n bjbswwaib'
        self.assertEqual(decrypt(cipher, pwd), text)
        self.assertEqual(encrypt(text, pwd), cipher)


if __name__ == '__main__':
    unittest.main()
