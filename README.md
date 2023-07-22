# Create a Note with python
#### Video Demo:  <https://www.youtube.com/watch?v=ar-V6j9tw1g>
#### Description:
Hello everyone, I am Behzad Danesh. Today I want to explain about my final project.
Here we have written a program that we can use to write and note down our daily plans and save them in the desired csv file.
In the first part, we enter "csv" and "re" modules.
#### import csv
#### import re

Then we define our own function and get information such as the type of work we want to do and the date and duration of the work.
#### x = input("What should I do: ")
#### y = input("Date(DD/MM/YYYY): ")
#### z = input("How many hours? ")
In giyu(x) function, we specify that if the input in the "What "should I do" field contains only numbers and no letters are used, "invalid" will be written and the code will go back.
#### def giyu(x):
####    if x.isnumeric():
####       print("invalid")
####       return True
In date(y) function, we determine that if the date format is not like ([0-3][0-9])\/([0-1][0-9])\/([2][0][0-9][0-9]), our program will not move forward
#### if re.search(r"^([0-3][0-9])\/([0-1][0-9])\/([2][0][0-9][0-9])$", y):
####        pass
#### else:
####      print("invalid date")
####      return True

And in the hours(z) function, we specified that if a letter is entered, our code does not go forward and returns
####     if z.isnumeric():
####        pass
####     else:
####        print("Invalid")
####        return True

Then in this section we write the "csv" file in which we want to save the information and specify our fields and specify which entry should be stored in which field.
####             with open("notes.csv", "a") as file:
####                writer = csv.DictWriter(file, fieldnames=["What", "Date", "Clock"])
####                writer.writerow({"What": x, "Date": y, "Clock": z})
We specified that "ctrl+D" exits the program and we can enter as many entries as we want.
####     except EOFError:
####        exit()
In our first test code, we import the functions we want to test
#### from main import giyu
#### from main import date
#### from main import hours
And then we wrote in our function that if our input contains only numbers, it will show true and otherwise it will be written as None
#### assert giyu("1234") == True
#### assert giyu("B2") == None
In the test_date function, we specified that if the day, month, or year is not based on the format that we specified in the meta, our code will not proceed.
For example, we cannot write 41 in the day part or we cannot write 54 for the month
Also, we cannot write 1005 or 3210 in the year part.
#### assert date("210/09/2024") == True
#### assert date("12/31/2022") == True
#### assert date("12/05/1432") == True
#### assert date("12/05/2023") == None
In the test_hours function, we specified that if a letter is written in that part, our code will show an error and not move forward, because we cannot write letters in the hours part and we only have to enter the number of hours.
#### assert hours("giyu") == True
#### assert hours("3n") == True
#### assert hours("2") == None

Thank you for your hard work and excellent training and special thanks to the Cs50x Iran team.
