# a. the individual linguistic unit of spy's words.
spy_message_encrypted = ['r', 'e', 'b', 'D', 'ng', ' ', 'w', 'D', 'q', ' ', 'l', 'D', 'gh', 'j', 'D', 'p']

# b. the corresponding value of the spy's message
values = ['a', 'b', 'ch', 'D', 'e', 'gh', 'H', 'I', 'j', 'l', 'm', 'n', 'ng', 'o', 'p', 'q', 'Q', 'r', 'S',
          't', 'tlh', 'u', 'v', 'w', 'y', '\'']
keys = [i for i in range(len(values))]
translation = dict(zip(values, keys))

print("encoding table:")
for i in spy_message_encrypted:
    if i == ' ':
        continue
    print(i, ":", translation[i])
# c. find the inverse of m (which is w)
n = 26
m = 15
k = 3
w = 0
for w in range(n):
    if (w * m) % n == 1:
        break

# d. decryption
decrypted = spy_message_encrypted
print("the decrypted values:")
for i in range(len(spy_message_encrypted)):
    if spy_message_encrypted[i] == ' ':
        continue
    y = translation[spy_message_encrypted[i]]
    print(w * (y - k) % n)

# e. decoding base on the table
    decrypted[i] = values[w * (y - k) % n]
print("".join(decrypted))

# f.
'''
the message is tlhIngan maH Qapla', in english "We are Klingon! Success!".
the spy is from the Star Trek and speaks Klingon.
'''
