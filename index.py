import json
with open("dump.json", "r",   encoding = "utf-8") as file:
    read_content = file.read()
    no_json = json.loads(read_content)
count = 0
close_menu = True
def menu():
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")
def all():
    global count
    count += 1
    for item in no_json:
        print("=" * 20, f"Номер записи: {item["id"]}", "=" * 20)
        print(f"Общее название звезды: {item["name"]} \n Название созвездия: {item["constellation"]} \n Можно ли увидеть звезду без телескопа: {item["is_visible"]} \n Солнечный радиус звезды: {item["radius"]}")
def one():
    global count
    count += 1
    record = input("Введите поле: ")
    found = False
    for item in no_json:
        if item["id"] == record:
            print("=" * 20, f"Номер записи: {item["id"]}", "=" * 20,)
            print(f"Общее название звезды: {item["name"]} \n Название созвездия: {item["constellation"]} \n Можно ли увидеть звезду без телескопа: {item["is_visible"]} \n Солнечный радиус звезды: {item["radius"]}")
            found = True
            break
    if not found:
        print("Некорректный ввод")
def new():
    global count
    count +=1
    with open("dump.json", "w",   encoding = "utf-8") as file:
        new = {}
        new["id"] = input("Введите номер записи: ")
        new["name"] = input("Введите название звезды: ")
        new["constellation"] = input("Введите название созвездия: ")
        new["is_visible"] = input("Можно ли увидеть звезду без телескопа (да/нет): ")
        new["radius"] = input("Введите радиус звезды: ")
        no_json.append(new)
        print("Запись добавлена")
        json.dump(no_json, file, indent = 4)
def delete():
    global count
    count += 1
    record = input("Введите поле для удаления: ")
    found = False
    with open("dump.json", "w",   encoding = "utf-8") as file:
        for i, item in enumerate(no_json):
            if item["id"] == record:
                del no_json[i]
                print("Запись удалена")
                found = True
                break
        json.dump(no_json, file, indent = 4)
        if not found:
            print("Некорректный ввод")
def escape():
    global count
    global close_menu
    print(f"{count} выполненных операций")
    close_menu = False
def main():
    while close_menu:
        menu()
        punkt = int(input("Выберете пункт: "))
        if punkt == 1:
            all()
        elif punkt == 2:
            one()
        elif punkt == 3:
            new()
        elif punkt == 4:
            delete()
        elif punkt == 5:
            escape()
        else:
            print("Нет такого пункта")
main()