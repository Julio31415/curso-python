"""
Sets - Conjuntos em Python (tipo set)
Conjuntos matematicos representados pelo diagrama de venn
Sets em Python são mutáveis, porém aceitam apenas os tipos imutáveis como valor interno.

Criando um Set
Set(iterável) ou {1,2,3}
"""
s1 = set('Luiz')
print(s1)
s2 = set() #set vazio
print(s2)
"""
Sets não garante a ordem
Sets são eficientes para remover valores duplicados de iteráveis
Seus valores serão sempre unicos
não aceitam valores mutáveis
não tem indexes
não garantem ordem
são iteráveis (for, in, not in)
"""
l1 = [1,2,3,3,3,3]
s1 = set(l1)
l2 = list(s1)
print(s1)

"""
Metodos uteis:
add, update, clear, discard
"""
s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá Mundo', 1,2,3))
print(s1)
s1.discard('Olá Mundo') #exclui um valor
print(s1)
s1.clear() #limpa tudo
print(s1)

"""
OPERÇÕES UTEIS:

União | União (union) - Une
Intersecção & (intersection) - itens presentes em ambos
diferença - itens presentes apenas no set da esquerda
diferença simetrica ^- itens que não estão em ambos
"""
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1|s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 - s2
s7 = s1^s2
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)
print(s7)