import os

class HobbyDiary:
    entries = []
    file_path = 'hobby_diary.txt'

    def addEntry(self, entry):
        self.entries.append(entry)
        print("Захоплення додано!")

    def showEntries(self):
        print("Ваші захоплення:")
        for i, entry in enumerate(self.entries, start=1):
            print(f"Захоплення {i}: {entry}")

    def saveToFile(self):
        with open(self.file_path, 'w') as file:
            for entry in self.entries:
                file.write(f"{entry}\n")
        print("Захоплення збережено у файлі.")

    def loadFromFile(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                self.entries = [line.strip() for line in file]
            print("Захоплення завантажено з файлу.")
            return True
        else:
            print("Файл із захопленнями не знайдено.")
            return False

    def run(self):
        self.loadFromFile()

        while True:
            print("1. Переглянути свої захоплення")
            print("2. Додати нове захоплення")
            print("3. Зберегти захоплення у файл")
            print("4. Завершити роботу")

            choice = input("Оберіть опцію: ")

            if choice == '1':
                self.showEntries()
            elif choice == '2':
                entry = input("Напишіть, що ви сьогодні відкрили для себе або зробили: ")
                self.addEntry(entry)
            elif choice == '3':
                self.saveToFile()
            elif choice == '4':
                print("Дякуємо за використання Щоденника захоплень. До побачення!")
                break
            else:
                print("Некоректний вибір. Спробуйте знову.")

hobby_diary = HobbyDiary()
hobby_diary.run()
