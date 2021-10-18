# Encryption detour

name = "Sim"
cipher = 3
encrypted = ""

for letter in name:
  print(letter)
  print(ord(letter))
  encrypted += chr(ord(letter)+cipher)


print(encrypted)

decrypted = ""
for letter in encrypted:
  decrypted += chr(ord(letter)-cipher)

print(decrypted)