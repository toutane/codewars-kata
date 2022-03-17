def decrypt(encrypted_text, n):
    if encrypted_text == '' or n <= 0:
        return encrypted_text
    l = len(encrypted_text)
    for i in range(n):
        temp, i, j, k = '', 0, int(l / 2), 0
        while i < l:
            if i % 2 == 0:
                temp += encrypted_text[j]
                j += 1
            else:
                temp += encrypted_text[k]
                k += 1
            i += 1
        encrypted_text = temp
    return encrypted_text


def encrypt(text, n):
    if text == '' or n <= 0:
        return text
    l = len(text)
    for i in range(n):
        odd, even, j = '', '', 0
        while j < l:
            even += text[j]
            j += 2
        j = 1
        while j < l:
            odd += text[j]
            j += 2
        text = odd + even
    return text


print(decrypt("hsi  etTi sats!", 1))
