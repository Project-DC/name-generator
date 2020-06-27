from selenium import webdriver
import sys

browser = webdriver.Chrome('/Users/frankhart/Downloads/chromedriver')

char = sys.argv[1]

names = []

i = 1
while True:
    url = 'https://parenting.firstcry.com/baby-names/boy/starting-with/' + str(char) + '/page/' + str(i)
    
    browser.get(url)
    
    names_in_page = browser.find_elements_by_class_name('baby-name')
    names_in_page = [name.text for name in names_in_page]
    
    if(len(names_in_page) == 0):
        break
    
    names.append(names_in_page)
    
    print('Page #' + str(i))
    
    i += 1
    
names = sum(names, [])

browser.close()

print(len(names))

with open(str(char) + '-boy.txt', 'w') as file:
    for name in names:
        file.write(name + '\n')