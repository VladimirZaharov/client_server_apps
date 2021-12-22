import csv


files_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']

def edit_data(some_str):
    new_str = some_str.replace(' ', '')
    new_str = new_str.replace('\n', '')
    return new_str


def get_data(some_list):
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for file in some_list:
        with open(file, 'r', encoding='cp1251') as s:
            data_list = s.readlines()
            for data in data_list:
                new_data = data.split(':')
                if new_data[0] =='Название ОС':
                    temp_data = edit_data(new_data[1])
                    os_name_list.append(temp_data)
                elif new_data[0] == 'Изготовитель ОС':
                    temp_data = edit_data(new_data[1])
                    os_prod_list.append(temp_data)
                elif new_data[0] == 'Код продукта':
                    temp_data = edit_data(new_data[1])
                    os_code_list.append(temp_data)
                elif new_data[0] == 'Тип системы':
                    temp_data = edit_data(new_data[1])
                    os_type_list.append(temp_data)
    data_list = list(zip(os_prod_list, os_name_list, os_code_list, os_type_list))
    for s in range(len(some_list)):
        main_data.append(list(data_list[s]))
    return main_data


def write_to_csv(some_file, some_list):
    with open(some_file, 'w', encoding='cp1251') as csv_file:
        data = get_data(some_list)
        csv_file_writer = csv.writer(csv_file)
        for row in data:
            csv_file_writer.writerow(row)

write_to_csv('csv_file.csv', files_list)
