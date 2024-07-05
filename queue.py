class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if not self.is_full():
            self.queue.append(item)
            return f"Элемент '{item}' добавлен"
        else:
            return "Очередь полна"

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Очередь пуста"

    def show(self):
        if not self.is_empty():
            return "Очередь: " + ' '.join(map(str, self.queue))
        else:
            return "Очередь пуста"


if __name__ == '__main__':
    def main_menu():
        q = Queue(3)
        while True:
            print("\n1. Добавить элемент")
            print("2. Удалить элемент")
            print("3. Показать очередь")
            print("4. Проверить, пуста ли очередь")
            print("5. Проверить, полна ли очередь")
            print("0. Выход")

            choice = input("Выберите операцию: ")
            if choice == '1':
                item = input("Введите символ для добавления: ")
                print(q.enqueue(item))
            elif choice == '2':
                print(q.dequeue())
            elif choice == '3':
                print(q.show())
            elif choice == '4':
                print("Очередь пуста" if q.is_empty() else "Очередь не пуста")
            elif choice == '5':
                print("Очередь полна" if q.is_full() else "Очередь не полна")
            elif choice == '0':
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    main_menu()
