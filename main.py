from random import randint
import pyglet


N = 100000  # количество элементов в списке
a = []
for i in range(N):
    a.append(randint(0, 10))

# Сама сортировка методом "пузырька"
for i in range(N-1):
    for j in range(N-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)  # вывод отсортированного списка
song = pyglet.media.load('Готов.mp3')
song.play()
pyglet.app.run()