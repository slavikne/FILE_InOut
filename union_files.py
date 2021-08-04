with open("1.txt", "r") as file_1, open("2.txt", "r") as file_2, open("3.txt", "r") as file_3:
        count_1 = sum(1 for line in file_1)
        count_2 = sum(1 for line in file_2)
        count_3 = sum(1 for line in file_3)
        dict_count = {"1.txt": count_1, "2.txt": count_2, "3.txt": count_3}
        list_counts = []
for count in dict_count.values():
        list_counts.append(count)
with open("union_file.txt", "w", encoding="utf-8") as file_union:
        for count in sorted(list_counts):
                for key, value in dict_count.items():
                        if value == count:
                                with open(key, "r") as file:
                                         file_union.write(f'{key}\n{value}\n{file.read()}\n')
                                break

