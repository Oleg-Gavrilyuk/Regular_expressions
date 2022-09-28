import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
news = []
# функция приведения файла к необходимому виду
def name_sort():
    pat_all = r'^([А-я]+)(\s|,)([А-я]+)(\s|,)([А-я]*)(\,{0,3})([А-я]*)(\,)([^\,]*)' \
              r'(\,)((\+7|8)?)(\s?)(\(?)((\d{3})?)(\)?)(\s?)(\-?)((\d{3})?)(\-?)((\d{2})?)' \
              r'(\-?)((\d{2})?)(\s?)(\(?)([а-я]*)(\.?)(\s?)(\d*)(\)?)(\,)?(\S*)(\s?)'
    sub_all = r'\1,\3,\5,\7,\9,+7(\16)\21-\24-\27\30\31\33,\36'

    for i in contacts_list:
        i_new = (','.join(i))
        new_t = re.sub(pat_all, sub_all, i_new)
        string = new_t.split(',')
        news.append(string)
    return(news)

# фуекция соединения имени, фамилии и отчества
def name_split():
    for i in news:
        # print(i)
        x = f'{i[0]} {i[1]} {i[2]}'
        i[0] = x
        i.remove(i[1])
        i.remove(i[1])

# функция соединения одинаковых записей по фамилии и имени
def merge_list():
    count = 0
    while count <= len(news) - 1:
        p = news[count]
        for i in news[count + 1:]:
            if i[0] in p[0] :
                count_2 = 0
                while count_2 <= 4:
                    if len(p[count_2]) < len(i[count_2]):
                        p[count_2] = i[count_2]
                    count_2 += 1
                news.remove(i)
        count += 1

if __name__=="__main__":
    name_sort()
    name_split()
    merge_list()
    print(news)
# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(news)