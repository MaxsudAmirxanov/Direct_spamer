data_base = 'test_data'
#Удаление строк ID, которым сообщение отправилось
with open("data_for_user/{data_base}.txt", 'r') as f:
    lines = f.readlines()

with open("data_for_user/{data_base}.txt", 'w') as f:
    f.writelines(lines[5:])
