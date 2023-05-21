import random

sea = [

]
izmers = int(input("Izvēlies jūras izmēru(minimums 3): "))  # присваиваем размер игрового поля

for listi in range(izmers):  # создаём клетки с морем
    kletka = [0] * izmers
    sea.append(kletka)

counter = 0
while counter < izmers + izmers // 2:  # добавляем в клетки с морем корабли
    kugu_garumi = random.randint(1, izmers // 2)
    kugu_pagrieziens = random.randint(1, 4)
    kugis_list = random.randrange(0, izmers)
    kugis_element = random.randrange(0, izmers)
    if sea[kugis_list][kugis_element] == 0:
        for garums in range(kugu_garumi):
            if kugu_pagrieziens == 1:
                if kugis_list <= izmers - 1 - kugu_garumi or sea[kugis_list][kugis_element] != 1:
                    sea[kugis_list + garums][kugis_element] = 1
                    counter += 1
                else:
                    kugu_pagrieziens += 1
            elif kugu_pagrieziens == 2:
                if kugis_element >= izmers - 1 - kugu_garumi or sea[kugis_list][kugis_element] != 1:
                    sea[kugis_list][kugis_element - garums] = 1
                    counter += 1
                else:
                    kugu_pagrieziens += 1
            elif kugu_pagrieziens == 3:
                if kugis_list >= izmers - 1 - kugu_garumi or sea[kugis_list][kugis_element] != 1:
                    sea[kugis_list - garums][kugis_element] = 1
                    counter += 1
                else:
                    kugu_pagrieziens += 1
            elif kugu_pagrieziens == 4:
                if kugis_element <= izmers - 1 - kugu_garumi or sea[kugis_list][kugis_element] != 1:
                    sea[kugis_list][kugis_element + garums] = 1
                    counter += 1
                else:
                    kugu_pagrieziens = 1
    else:
        sea[kugis_list][kugis_element] = 1

savieni = izmers * izmers // 2
while True:  # рисуем игровое поле и меняем его после выстрела
    for index, row in enumerate(sea):
        print(index, end='')
        for element in row:
            if element == 0 or element == 1:
                print('🌊', end='')
            elif element == 2:
                print('🔵', end='')
            elif element == 3:
                print('🔥', end='')
        print('')
    print('Šeit ir ' + str(counter) + ' kuģu punkti.')
    print('Tev atlika ' + str(savieni) + ' šāvieni.')
    if counter == 0:  # если нет кораблей то победа
        print('Visi kuģi tika likvidēti. Tu uzvarēji')
        break
    if savieni == 0:  # если нет выстрелов то поражение
        print('Šeit vel ir kuģi, bet tev vairs nav šāvienu. You lose.')
        for index, row in enumerate(sea):  # показываем расположение оставшихся корабликов
            print(index, end='')
            for element in row:
                if element == 0:
                    print('🌊', end='')
                elif element == 1:
                    print('🚢', end='')
                elif element == 2:
                    print('🔵', end='')
                elif element == 3:
                    print('🔥', end='')
            print('')
        break
    shoot_vert = int(input('Izvēlies vertikāli(⬇)(0-' + str(izmers - 1) + '): '))
    shoot_hor = int(input('Izvēlies horizontāli(➡)(0-' + str(izmers - 1) + '): '))
    if sea[shoot_hor][shoot_vert] == 0:
        sea[shoot_hor][shoot_vert] = 2
        savieni -= 1
    elif sea[shoot_hor][shoot_vert] == 1:
        sea[shoot_hor][shoot_vert] = 3
        counter -= 1
        savieni -= 1
