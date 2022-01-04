motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles.insert(3, 'BMW')
print(motorcycles)

del motorcycles[3]
print(motorcycles)

popped_motocycles = motorcycles.pop() #usuwa ostatni element z listy
print(motorcycles)
print(popped_motocycles)

popped_motocycles = motorcycles.pop(2) #usuwa wskazany element z listy
print(motorcycles)
print(popped_motocycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('yamaha') #usuwa według wartości z listy (pierwszy który znajdzie, pozostałe usunięcia trzeba wypetlować - użyć do tego pętli)
print(motorcycles)
