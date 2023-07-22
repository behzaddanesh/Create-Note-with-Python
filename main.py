import csv
import re

def main():

    try:
        while True:
            x = input("What should I do: ")
            if giyu(x):
                continue
            y = input("Date(DD/MM/YYYY): ")
            if date(y):
                continue
            z = input("How many hours? ")
            if hours(z):
                continue
            with open("notes.csv", "a") as file:
                writer = csv.DictWriter(file, fieldnames=["What", "Date", "Clock"])
                writer.writerow({"What": x, "Date": y, "Clock": z})


    except EOFError:
        exit()

def giyu(x):
    if x.isnumeric():
        print("invalid")
        return True


def date(y):
    if re.search(r"^([0-3][0-9])\/([0-1][0-9])\/([2][0][0-9][0-9])$", y):
        pass
    else:
        print("invalid date")
        return True
def hours(z):
    if z.isnumeric():
        pass
    else:
        print("Invalid")
        return True



if __name__ == '__main__':
    main()






