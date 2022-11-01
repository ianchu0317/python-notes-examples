
def odd_num(num):
    if divmod(num, 2)[1] == 0:
        return num


array = [x for x in range(20+1)]

odd = filter(odd_num, array)

print("array is: ", array)
print("odd num are: ", list(odd))
