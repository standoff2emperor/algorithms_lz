import random 
list=[]
for i in range(100):
    list.append(random.randint(0, 1000000))#задаем список со случайными значениями 
print(list)#вывод
print(len(list))#проверка количества элементов количества
bubble_list=list#создаем новый список
a=0#счетчик интераций
stop_flag = True#флаг для закрытия цикла
while stop_flag is True:
    stop_flag=False
    for i in range(0, len(bubble_list) - 1):
        if bubble_list[i] < bubble_list[i + 1]:#условия для перемены элементов местами
            swap = bubble_list[i]
            bubble_list[i] = bubble_list[i + 1]
            bubble_list[i + 1] = swap
            print(bubble_list)#вывод после каждой интерации
            a+=1#увеличение количества интераций
            stop_flag = True#закрытие цикла
print(bubble_list)#вывод
sort_list=list#новый список
sort_list = []
b=0#счетчик вторых интераций
while len(bubble_list) > 0:#условие для отсортировки выбором в порядке убывания 
    max = bubble_list[0]
    for i in range(0, len(bubble_list)):
        if bubble_list[i] > max:
            max = bubble_list[i]
    sort_list.append(max)
    bubble_list.remove(max)
    print(sort_list)#вывод после каждой интерации
    b+=1#увеличение количества интераций 
    print("отсортированный список",sort_list)#вывод
    print("количество интераций в пузырьковой сортировке",a)#вывод
    print("количество интераций в сортировке выбором",b)#вывод
