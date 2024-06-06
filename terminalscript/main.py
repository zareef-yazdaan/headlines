import requests
from bs4 import BeautifulSoup
import tkinter
import customtkinter
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()
app.geometry('720x480')
app.title('Daily Star')

def news():
    page = requests.get('https://www.thedailystar.net/')

    soup = BeautifulSoup(page.content, 'html.parser')
    headlines = (soup.find_all(class_='title h1'))
    number = len(headlines) - 1
    num = 0

    print('\n')
    print('\n')
    print('\n')

    print("////////////////////  LARGE EVENTS /////////////////////")
    print('\n')
    print('\n')
    print('\n')

    for i in headlines:
        number -= 1
        num += 1
        print(num, '#', headlines[number].get_text().strip(), '\n')

    print('\n')
    print('\n')
    print('\n')

    print("////////////////////  HEADLINES  /////////////////////")
    print('\n')
    print('\n')
    print('\n')

    lines = (soup.find_all(class_='intro'))
    line_number = len(headlines) - 1
    linenum = 0
    for x in lines:
        line_number -= 1
        linenum += 1
        print(linenum, '#', lines[line_number].get_text(), '\n')


news()