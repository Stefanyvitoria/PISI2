import random
dados = [ele for ele in range(10000)]
#dados = [ele for ele in range(10000,0,-1)]
#dados = [random.randint(0,20) for _ in range(10000)]

a = dados.copy()
b = dados.copy()

b = sorted(b)
(a,0,len(a)-1)


print(a)

print(a == b)