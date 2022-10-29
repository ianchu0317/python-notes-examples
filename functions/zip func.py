# zip() el primero empareja con el primero del otro
even = [x for x in range(1, 10+1) if x % 2 == 0]
odd = [x for x in range(10+1) if x % 2 != 0]

print("even: {}".format(even))
print("odd: {}".format(odd))

merged = [x for x in zip(odd, even)]

print(merged)
