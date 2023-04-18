frutas = ["uva", "morango", "maça", "kiwi"]
frutas[1] = 'abacate'
frutas.insert(2, 'abacaxi')
print(frutas)
frutas.insert(3, 'cebola') #não é fruta
print(frutas)
del frutas[3]
print(frutas)
frutas.insert(4, 'laranja')
print(frutas)
print(f'o que é o {frutas.index ("laranja")}')
del frutas[frutas.index('laranja')]
print(frutas)
frutas.remove("kiwi")
print(frutas)
frutas.insert(10, 'ameixa')
print(frutas)
frutas.pop(frutas.index('ameixa'))
print(f'pop fruta - {pop_frutas} ')
print(frutas)

