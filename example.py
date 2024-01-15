from flyCode import encode, decode

# 7~4_
code = "4"

encoded = encode("Hello, World!", code)
decoded = decode(encoded, code)

print(decoded)