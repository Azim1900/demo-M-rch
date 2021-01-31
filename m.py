m = [1,2,3,4,5]

r = [n*n for n in m ]
r_l = map(lambda n: n*n ,m)
print(list(r_l))
print(r)
name = input()