# 1
name = input('Введите имя')
(lambda name: print('Привет,' + name))(name)

# 2
greetings = list(map(lambda name: f"Hello, {name}", ['Alice', 'Bob', 'Charlie']))
print(greetings)

# 3 (используя гинератор списка)
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
s1 = [i for i in numbers if i > 0]
print(s1)


# с использованием функции генератор
def only_positive_numbers(numbers, result):
    for i in numbers:
        if i > 0:
            result.append(i)
    yield result


print(next(only_positive_numbers([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7], [])))


# 4
def find_len_sentence(sentence):
    word_lengths = []
    for word in sentence.split():
        try:
            if word != "the":
                word_lengths.append(len(word))
        except:
            pass
    print(word_lengths)


find_len_sentence("the quick brown fox jumps over the lazy dog")


#  работает на русском и английском языках и использует свой собственный шифр и сохраняет исходный регистр.
def encode(sentence, shift):
    encoded_sentence = ""
    for i in sentence:
        if i.isalpha():
            if i.isupper():
                if 'А' <= i <= 'Я':
                    encoded_char = chr((ord(i) - ord('А') + shift) % 33 + ord('А'))
                else:
                    encoded_char = chr((ord(i) - ord('A') + shift) % 26 + ord('A'))
            else:
                if 'а' <= i <= 'я':
                    encoded_char = chr((ord(i) - ord('а') + shift) % 33 + ord('а'))
                else:
                    encoded_char = chr((ord(i) - ord('a') + shift) % 26 + ord('a'))
        else:
            encoded_char = i
        encoded_sentence += encoded_char
    return encoded_sentence


def decode(word, shift):
    return encode(word, -shift)
word = "Hello, Мир!"
shift = 5
encoded_sentence = encode(word, shift)
print("Encoded sentence:", encoded_sentence)
decoded_sentence = decode(encoded_sentence, shift)
print("Decoded sentence:", decoded_sentence)