def convert(gram):
    ounce = gram / 28.3495231
    return ounce

weight = int(input())
weight = convert(weight)
print(weight)
