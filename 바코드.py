def check(barcode):
    odd_sum = sum(barcode[::2])  
    even_sum = sum(barcode[1::2])  
    total = odd_sum + even_sum * 3
    target = (10 - (total % 10)) % 10
    return target


barcode = list(map(int, input().split()))


print(check(barcode))


'''
barcode = list(map(int, input().split()))

odd_sum = 0
for i in range(0, len(barcode), 2):
    odd_sum += barcode[i]

even_sum = 0
for i in range(1, len(barcode), 2):
    even_sum += barcode[i]

total = odd_sum + even_sum * 3

check = (10 - (total % 10)) % 10

print(check)
'''
