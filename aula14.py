a = 'A'
b = 'B'
c = 1.1
string = 'a={} b={} c={:.2f}'
formato = string.format(a,b,c)
string2 = 'a={0} b={0} c={2:.2f}'
formato2 = string2.format(a,b,c)
string3 = 'a={nome3} b={nome1} c={nome3:.2f}'
formato3 = string3.format(nome1=a, nome2=b, nome3=c)
print(formato)
print(formato2)
print(formato3)
