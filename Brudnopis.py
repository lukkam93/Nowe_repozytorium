# slownik = {
#     "TODO": [],
#     "IN PROGRESS": [],
#     "DONE": []
# }
# idx = [0]
# print(tabulate(slownik, headers="keys", tablefmt="rounded_grid"))
#
# available_commands = ["D", "E", "U", "W"]
#
# def menu_glowne():
#     print("""
# Co chciałbyś zrobić?
# [D]dodaj
# [E]dytuj
# [U]suń
# [W]yjdź z aplikacji
#     """)
#     wybor_1 = input("Wybierz operację ")
#     wybor_1 = wybor_1.upper()
#     if wybor_1 not in available_commands:
#         print("Podałeś nieprzewidzianą wartość. Co chcesz zrobić?")
#         return None
#
#     if wybor_1 == "D":
#         print("Dodajesz")
#         column_id = wybor_kolumny()
#         status = list(slownik.keys())[column_id - 1]
#         dodaj(status)
#
#     elif wybor_1 == "E":
#         print("Edytujesz")
#         # wybor_kolumny()
#     elif wybor_1 == "U":
#         print("Usuwasz")
#         # wybor_kolumny()
#     else:
#         print("Podałeś nieprzewidzianą wartość. Co chcesz zrobić?")
#     return wybor_1
#
# def wybor_kolumny():
#     print("""
# Na której kolumnie chcesz dokonać operacji?
# 1 - TODO
# 2 - IN PROGRESS
# 3 - DONE
#     """)
#     wybor_2 = int(input("Wybierz kolumne "))
#     if wybor_2 == 1:
#         print("Kolumna TODO")
#     elif wybor_2 == 2:
#         print("Kolumna IN PROGRESS")
#     elif wybor_2 == 3:
#         print("Kolumna DONE")
#     return wybor_2
#
#
# def dodaj(status):
#     lista_taskow = slownik[status]
#     idx[0] += 1
#     indeks = idx[0]
#     descr = input("Podaj treść ticketu: ")
#     task = "ID_" + str(indeks) + " " + descr
#     lista_taskow.append(task)
#     # slownik[status].append(task)
#
#
#
# result = ""
#
# while result != 'W':
#     print(tabulate(slownik, headers=["TO DO", "IN PROGRESS", "DONE"], tablefmt="rounded_grid"))
#     result = menu_glowne()
#
# print("Dziękuje za skorzystanie z aplikacji")
#





class Task:
    __count = 0

    def __init__(self, description, status):
        self.description = description
        self.status = status
        self.id = Task.incr() #python magic method to increment id for every task

    @classmethod
    def incr(cls): #python magic method to increment id for every task
        cls.__count += 1
        return cls.__count

    def describe(self):
        return f'{self.id}: {self.description}'

text = input("Zadanie ")
column = input("Kolumna")
a = Task(description=text, status=column)
slownik2 = {a.id: str(text + "," + column)}
print(slownik2)
print(type(a.describe()))



slownik2 = {
    1: Task("What is this", "TODO"),
    2: Task("How much is the fish", "IN PROGRESS"),
    3: Task("Where is it", "TODO")
}

#edit
idx1 = 1
idx2 = 2
idx3 = 3

task1 = slownik2[idx1]
task2 = slownik2[idx2]
task3 = slownik2[idx3]
print(task1.describe())
print(task2.describe())
print(task3.describe()) # każdy task ma inne id
new_desc = "We're done here"

task1.description = new_desc
print(task1.describe())

task1again = slownik2[idx1]
print(task1again.describe())

