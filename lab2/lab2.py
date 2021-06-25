def ReadFile(file):
    divisions = {}
    lines = file.readlines()
    for line in lines:
        params = line.split("; ")
        if divisions.get(params[3]) is None:
            d = {params[3]: [params[5]]}
            divisions.update(d)
        else:
            divisions.get(params[3]).append(params[5])
    return divisions


def Report(divisions):
    myReport = []
    for division in divisions:
        payments = [int(item) for item in divisions.get(division)]
        myReport.append(division + " Численность: " +
                        str(len(payments)) + '\t' +
                        "Макс зп: " + str(max(payments)) +
                        '\t' + "Мин зп: " + str(min(payments)) +
                        '\t' + "Ср зп:" + str(sum(payments) // len(payments)))

    return myReport


def SelectMenuItem():
    choice = ""
    choices = {'1', '2', '3', '4'}
    while choice not in choices:
        print("Введите номер команды:\n"
              "1 - Вывести все отделы\n"
              "2 - Вывести сводный отчёт по отделам\n"
              "3 - Сохранить сводный отчёт в виде csv\n"
              "4 - Выход\n")
        choice = input()
        return choice


def WorkFun(divisions):
    while 1:
        choice = SelectMenuItem()
        if choice == "1":
            for department in divisions.keys():
                print(department)
        elif choice == "2":
            for department in Report(divisions):
                print(department)
        elif choice == "3":
            f = open("report.csv", 'w')
            for department in Report(divisions):
                f.write(department + "\n")
            f.close()
            print("Отчет сохранен")
        elif choice == "4":
            break

        print("\n\r")


if __name__ == '__main__':
    workFile = open("work.csv", 'r')
    divisions = ReadFile(workFile)
    workFile.close()
    WorkFun(divisions)
