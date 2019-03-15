#Bitwise XOR ^ as a function

a = "1110"
b = "101"
result = "0b"

if len(a) > len(b):
    b = "0" + b
elif len(b) < len(b):
    a = "0" + a

for i in range(max(len(a),len(b))):
    if a[i] == b[i]:
        result += "0"
    elif a[i] == "1" or b[i] == "1":
        result += "1"

print result
