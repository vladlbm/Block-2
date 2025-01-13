class MemoryManager:
    def __init__(self, size):
        self.size = size
        self.pool = [None] * size
        self.free_b = list(range(size))


    def allocate(self, value):
        if not self.free_b:
            raise MemoryError('Нет доступной памяти')
        block_index = self.free_b.pop(0) # освобождаю первую ячейку для записи
        self.pool[block_index] = value # запись в эту освобождённую ячейку
        return block_index # возвращение индекса памяти, для того чтобы её можно было освобождать в дальнейшем


    def free(self, index):
        if index < 0 or index >= len(self.pool): # проверка на вхождение индекса, вообще области можем ли мы его использовать
            raise ValueError('Недопустимый индекс')
        if self.pool[index] is None: # проверка на то, пустая ли ячейка эта в памяти, если да, то зачем её освобождать если она уже пустая
            raise ValueError('Ячейка уже пустая')
        self.pool[index] = None
        self.free_b.append(index)
        print(f'Произошло освобождение ячейки: {index} и добавили значение в особождённые {self.pool[index]}')


    def display_pool(self):
        print(f'Значения в пуле: {self.pool}')


test = MemoryManager(5)
p1 = test.allocate('AAA')
p2 = test.allocate('BBB')
print(p1)
print(p2)
print(test.display_pool())

print(test.free(p1))
print(test.display_pool())




