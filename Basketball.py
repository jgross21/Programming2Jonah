list = []
for i in range(1, 69):
    x = i / (i + 283)
    list.append(x)

print(list)

def multiply_list(list):
    result = 1
    for x in list:
        result = result * x
    return result

result = (multiply_list(list))
print(result)

otra = (1/2) ** 63
print(otra)
print(otra/result/100)