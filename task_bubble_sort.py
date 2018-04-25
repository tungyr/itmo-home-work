def bubble_sort(lst):   #объявление функции
    for i in range(len(lst)):      #перебор диапазона с длиной lst
        for j in range(len(lst) - 1, i, -1):      #перебор диапазона lst c обменом значений
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]

    return lst

bubble_sort([14, 8, 3, 1, 89, 2, 45])
