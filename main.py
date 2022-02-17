import os


def get_data(file_path, file_encoding='UTF-8'):
    with open(file_path, encoding=file_encoding) as file:
        buffer = file.read().split('\n\n')

    r_data = {}

    for line in buffer:
        ing_buffer = []
        lst_buffer = line.split('\n')

        for ln in lst_buffer[2:]:
            ing = ln.split(' | ')
            ing_buffer.append({'ingredient_name': ing[0], 'quantity': ing[1], 'measure': ing[2]})

        r_data[lst_buffer[0]] = ing_buffer

    return r_data

def get_shop_list_by_dishes(data, dishes, person_count):

    r_data = {}
    for dish in dishes:
        try:
            ing_list = data[dish]
        except KeyError:
            return 'Error'

        for ing in ing_list:
            if ing['ingredient_name'] in r_data:
                r_data[ing['ingredient_name']]['quantity'] += int(ing['quantity']) * person_count
            else:
                r_data[ing['ingredient_name']] = {'measure': ing['measure'], 'quantity': int(ing['quantity']) * person_count }

    return r_data

# #Задание №3
def merge_files(dir_path):

    files_list = []

    if os.path.exists(os.path.join(dir_path, 'result.txt')):
        os.remove(os.path.join(dir_path, 'result.txt'))

    files = os.listdir(dir_path)

    for file in files:
        with open(os.path.join(dir_path, file), encoding='UTF-8') as f:
            buffer = f.readlines()

        files_list.append({'filename': file, 'buffer': buffer, 'str_count': len(buffer)})

    files_list.sort(key=lambda val: val['str_count'])

    with open(os.path.join(dir_path, 'result.txt'), mode='w+', encoding='UTF-8') as f:

        for file in files_list:
            f.write(file['filename'] + '\n')
            f.write(str(file['str_count']) + '\n')
            f.writelines(file['buffer'])
            f.write('\n')


def main(): pass
    data_path = os.path.join(os.getcwd(), 'recipes.txt')
    data = get_data(data_path)
    print(data)
    print('+++++++++++++++++++++++++++++++++++++++++++++')

    ingredients = get_shop_list_by_dishes(data,['Омлет', 'Запеченный картофель'], 3)
    print(ingredients)


# #Задание №3
    _dir = os.path.join(os.getcwd(), 'files')
    merge_files(_dir)


main()