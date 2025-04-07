from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  #print(contacts_list)

# Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
# В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О.
# Подсказка: работайте со срезом списка (три первых элемента) при помощи " ".join([:2]) и split(" "), регулярки здесь НЕ НУЖНЫ.

for item in contacts_list:
    initials = ' '.join(item[:3]).split(' ')
    all_initials = [initials[0], initials[1], initials[2]]
    #print(all_initials)

    # Привести все телефоны в формат +7(999)999-99-99.
# Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.
# Подсказка: используйте регулярки для обработки телефонов.

    import re

    phone_pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'

    for contact in contacts_list:
        contact[5] = phone_pattern.sub(phone_substitution, contact[5])
        #pprint(contact[5])

# Объединить все дублирующиеся записи о человеке в одну.
# Подсказка: группируйте записи по ФИО (если будет сложно, допускается группировать только по ФИ).

    all_initials_list = []
    for fio in all_initials:
        if all_initials[0] not in all_initials_list:
            all_initials_list.append(all_initials[0])
            # all_initials_list.append(all_initials[1])
            # all_initials_list.append(all_initials[2])
    print(all_initials_list)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
#with open("phonebook.csv", "w", encoding="utf-8") as f:
  #datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  #datawriter.writerows(contacts_list)