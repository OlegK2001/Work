### импорт внешних библтотек ###
import os; import glob; import gc
from selenium import webdriver
import re; import time

### импорт внутренних функций ###
from katalog import product


###     Функции     ###
# Вывод информации о категориях
def printf(files):
    # print(files)
    count = 1
    for obj in files:
        print(f'#{count}: {obj}')
        count += 1

# Создание файлов для хранения товаров
def groupingFiles(productCatalog):
    count = 0
    if not os.path.isdir("./products"):
        os.mkdir("./products")
        count = 1
    os.chdir("./products")

    # Создадим папки и файлы для товаров
    def Directory(name, array):
        if not os.path.isdir(f"{name}"): os.mkdir(f"{name}")
        os.chdir(f"{name}")
        WorkWithArray(array)

    def File(name):
        try:    open(f"{name}.html", 'rt').close()
        except: open(f"{name}.html", 'wt').close()

    def WorkWithArray(array):
        for index in range(len(array)):
            if type(array[index]) == type('text') and type(array[index + 1]) != type(['mass']):
                File(array[index])
            try:
                if type(array[index + 1]) == type(['mass']): Directory(array[index], array[index + 1])
            except:
                os.chdir('..')
    if count == 1: #pass
        WorkWithArray(productCatalog)

# Создание ссылок на все *.html файлы
def creatingLinks():
    LinksFile = []
    #print('1')
    #print(os.getcwd())
    # path = '/OLDIproject/Work/Exampls/Parser/products'
    #os.chdir("products")
    path = os.getcwd()

    #print(os.getcwd())
    files = [os.path.abspath(f) for f in glob.glob(f"{path}/")]
    files += [os.path.abspath(f) for f in glob.glob(f"{path}/**")]
    files += [os.path.abspath(f) for f in glob.glob(f"{path}/**/**")]
    files += [os.path.abspath(f) for f in glob.glob(f"{path}/**/**/**")]
    files += [os.path.abspath(f) for f in glob.glob(f"{path}/**/**/**/**")]
    for obj in files:
        # print(obj)
        if '.html' in obj:
            if '.txt' in obj: continue
            LinksFile.append(obj)
    printf(LinksFile)
    return LinksFile

# Словарь для сопоставление адреса файлов и ссылок на каталоги
def LinksWithArray(dict, array):
    diction = {}
    for key in dict.keys():
        #print(key)
        for obj in array:
            #print(obj)#copy #CA_Motherboards.html
            if str(key) in str(obj):
                diction[obj] = dict[key]
    #print(diction)
    return diction

# Функция для получение смысловой части товаров
def request(Page):
    # Получение информации о товарах
    pattern1 = r' [0-9]{7,10}'
    pattern2 = r'>.*</'
    pattern3 = r'<strong>код:</strong>.[0-9]*</div>'
    pattern4 = r'<span class="catalog-list-title">.*</span>'
    answer1 = requestProducts(pattern3, Page)
    answer2 = requestProducts(pattern4, Page)

    text = f'#{len(answer1)} ***\n'
    for index in range(len(answer1)):
        answer1[index] = requestProducts(pattern1, answer1[index])[0]
        answer2[index] = requestProducts(pattern2, answer2[index])

        text += f'#{index + 1} => {answer1[index]} || {answer2[index]}\n'
    text += '###'
    print(text)
    return text, answer1, answer2

# Код страницы
def codePage(dictinary, driver, Key):

    driver.get(dictinary[Key])
    pageSource = driver.page_source

    # Посчитаем кол-во страниц для данного вида товара
    pattern = r'class="local".*>[0-9]*</a>'
    answer = re.findall(pattern, pageSource)
    text = ''
    t = False
    count = []
    for index in range(len(answer)):
        for i in answer[index]:
            if i == '<':  t = False
            if t == True: text += i
            if i == '>':  t = True
        count.append(int(text))
    try:    lan = max(count)
    except: lan = 1
    for index in range(2, lan+1):
        driver.get(dictinary[Key] + f'?PAGEN_1={index}')
        pageSource += driver.page_source
        # Получение информации о продуктах
    products = request(pageSource)
    if not os.path.isfile(Key + '.txt'):
        #print('Новая категория:', Key)
        with open(Key + '.txt', 'w') as f:  f.write(str(products[0]))

    return pageSource, products

# Парсинг товаров
def requestProducts(pattern, text):
    return re.findall(pattern, text)

# Считываем информацию из файлов
def reading(Key):
    with open(Key + '.txt', 'rt') as f:
        productsID = []
        productsName = []
        count = f.readline()
        text  = f.readline()
        #print(text)
        while text != '###':
            text = text.split(' =>  ')[1]
            #print(text)
            text = text.split(' || ')
            #print(text)
            productsID.append(text[0])
            productsName.append(text[1])
            text = f.readline()
    return count, productsID, productsName

# соотнесение товаров
def correlationOfGoods(count, productID, productName, Products, Key, Page):
    answer = requestProducts(r'[0-9]{1,3}', count)
    productsID = []
    productsName = []
    Products = Products[0].split('***\n')[1].split(' =>  ')
    for index in range(len(Products)-1):
        productsID.append(Products[index+1].split(' || ')[0])
        productsName.append(Products[index + 1].split(' || ')[1])
    Products = productsID

    for obj in productID:
        if obj not in Products:
            print(f'Отсутствует => {obj} || {productName[productID.index(obj)]}')

    with open(Key + '.txt', 'rt') as f:
        text1 = f.read()
        text1 = text1[0:1:len(text1)-3]
        product, a, b = request(Page)
        for obj in Products:
            if obj not in productID:
                text1 += f'#{len(a)} =>  {obj} || {productsName[productsID.index(obj)]}\n'
                a.append(obj)
    #text1 += '###'
    with open(Key + '.txt', 'wt') as f: f.write(text1[0:len(text1)-2])

    #print(Products)
    #print(Key)


### Управляющий код ###
productCatalog = product.productCatalog             # массив  каталога
linksOnWeb_Sayte = product.linksOnWeb_Sayte         # словарь каталога

# путь к драйверу
path = 'C:\\Users\\olegk\\PycharmProjects\\pythonProject\\oldi\\Parser\\driver\\chromedriver'
#driver = webdriver.Chrome(executable_path=path)






# Старый управляющий код (в поисках гемороя)
'''
def work():
#try:
    # Создаем папки для страниц сайта
    groupingFiles(productCatalog)

    # Создаем ссылки на категории товара
    Links = creatingLinks()

    #print(linksOnWeb_Sayte, Links)

    # Создадим сводный словарь ссылок
    dictinary = LinksWithArray(linksOnWeb_Sayte, Links)

    # Получение кода страницы
    driver = webdriver.Safari()
    driver.maximize_window()
    #driver = webdriver.Chrome(executable_path="/Users/olegkalasnikov/PycharmProjects/pythonProject/OLDIproject/Work/Exampls/Parser")
    for Key in dictinary.keys():
        pages, Products = codePage(dictinary, driver, Key)

        # Начинаем сравнивать товары те, что есть и те, что спарсили
        count, productID, productName = reading(Key) # Считываем информацию из документов
        #print(productID)
        #print(count)
        #print(productName)

        # Соотнесение товаров
        #print(pages)
        correlationOfGoods(count, productID, productName, Products, Key, pages)
    driver.close()
'''












