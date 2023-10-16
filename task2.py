import collections


pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
}


def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False


def get_suffix(age_pet):
    if age_pet in [11, 12, 13, 14]:
        return 'лет'
    elif age_pet % 10 in [2, 3, 4]:
        return 'года'
    elif age_pet % 10 == 1:
        return 'год'
    else:
        return 'лет'


def pets_list():
    for i in pets.items():
        print(i)


def create():
    last = collections.deque(pets, maxlen=1)[0]
    name_pet = input('Кличка питомца: ')
    info = {}
    pets[last + 1] = {name_pet: info}
    tip_pet = 'Вид питомца'
    age_pet = 'Возраст питомца'
    owner = 'Имя владельца'
    info[tip_pet] = input('Вид питомца: ')
    info[age_pet] = int(input('Возраст питомца: '))
    info[owner] = input('Имя владельца: ')
    return print('Новая запись добавлена')


def read(ID):
    if get_pet(ID) == False:
        return print('Такого ID в системе нет!')
    else:
        for name_pet, info in get_pet(ID).items():
            tip_pet = info['Вид питомца']
            age_pet = info['Возраст питомца']
            owner = info['Имя владельца']
            return print(f'Это {tip_pet} по кличке "{name_pet}". Возраст питомца: {age_pet} {get_suffix(age_pet)}. Имя владельца: {owner}')


def update(ID):
    if get_pet(ID) == False:
        return print('Такого ID в системе нет!')
    else:
        info = {}
        name_pet = input('Кличка питомца: ')
        pets[ID] = {name_pet: info}
        for name_pet, info in get_pet(ID).items():
            info['Вид питомца'] = input('Вид питомца: ')
            info['Возраст питомца'] = int(input('Возраст питомца: '))
            info['Имя владельца'] = input('Имя владельца: ')
            return print('Запись обновлена')


def delete(ID):
    if get_pet(ID) == False:
        return print('Такого ID в системе нет!')
    else:
        pets.pop(ID)
        return print(f'Запись с ид {ID} удалена!')


print("База данных для ветеринарной клиники.\n "
      "Команда 'create' - создание новой записи.\n "
      "Команда 'read' - чтение записи по ид. \n "
      "Команда 'update' - обновление записи по ид. \n "
      "Команда 'delete' - удаление записи по ид. \n "
      "Команда 'pets_list' - отображение всего списка питомцев\n "
      "Команда 'stop' - остановка программы.\n")


command = ''
while command != 'stop':
    command = input('Введите команду: ')
    if command == 'create':
        create()
    elif command == 'read':
        ID = int(input('Введите ид питомца: '))
        read(ID)
    elif command == 'update':
        ID = int(input('Введите ид питомца: '))
        update(ID)
    elif command == 'delete':
        ID = int(input('Введите ид питомца: '))
        delete(ID)
    elif command == 'pets_list':
        pets_list()
    else:
        print('Неверная команда! Выберите команду из списка(create, read, update, delete, pets_list)!')


