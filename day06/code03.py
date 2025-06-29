"""
从1到100的整数求和
"""
total = 0
i = 1

while i <= 100:
    total += i
    i += 1
print(total)

"""
从1到100的偶数求和
"""
total = 0
i = 2
while i <= 100:
    total += i
    i += 2
print(total)

"""
从1到100的偶数求和
break和continue
"""
total = 0
i = 1
while True:
    if i > 100: break
    if i % 2 == 0: total += i
    i += 1

print(total)
