from selenium import webdriver

# d = webdriver.Chrome()
# d.get('https://www.imymac.com/sitemap/')
# d.find_element_by_link_text()

i = [1, 2, 3, 4]
j = [1, 4, 6, 7]
print('1 2 3 4'.split(' '))
print(len(i) + len(j) != len(set(i + j)))
print(len(i) + len(j))
print(len(set(i + j)))
