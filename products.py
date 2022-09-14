# Подключим необходимые нам библиотеки
import os
import glob
from selenium import webdriver
import re
import time

'''Файлы категории товаров / группировка файлов и папок'''
productCatalog = [
    'NetworkEquipment.',
    [
        'Wi-Fi routers and access points',
        'Mobile 3G_4G modems',
        'Network Wireless Adapters',
        'Signal amplifiers_Repeaters',
        'Switches',
        'PoE Adapters',
        'NAS Network Storage',
        'Powerline equipment',
        'Extension modules',
        'Routers and firewalls',
        'Print servers',
        'Media converters, transceivers',
        'Antennas',
        'Related network equipment',
        'Network cards',
        'Signal transmission equipment',
        'Optical Patch Cords',
        'Bluetooth Adapters',
        'Components for the installation of networks.',
        [
            'Sockets for network equipment',
            'Cabinets, racks',
            'Tools for installation and testing',
            'Connectors',
            'Installation equipment',
            '',
        ],
    ],

    'Smartphones, tablets and gadgets.',
    [
        'Smartphones',
        'Mobile phones',
        'Video recorders',
        'Tablets',
        'E-books',
        'Smart watches and fitness bracelets',
        'GPS navigators',
        'Gyroscuters',
        'Accessories for tablets and smartphones.',
        [
            'Covers',
            'Cases and bags for tablets',
            'Portable speakers',
            'Charging',
            'Car charging for phones',
            'Protective glasses and films',
            'Cables, adapters and adapters',
            'Holders in the car',
            'Selfie sticks',
            'External batteries',
            'Input devices, docking stations,gloves for touch screens',
            '',
        ],
        'Accessories for Apple products.',
        [
            'Adapters and adapters',
            'Chargers and power supplies',
            'Accessories for Apple iWatch',
            'Bags and cases for Apple',
            'Protective glasses and films for Apple',
            'Apple Cables and Adapters',
            '',
        ],
        '3D pens',
        '',
    ],

    'Computers and peripherals.',
    [
        'OLDI computers.',
        [
            'For home',
            'For the office',
            'Gaming',
            'OLDI monoblocks',
            'Mini PC OLDI',
            'PC with Microsoft Office',
            '',
        ],

        'Computers',
        'Monoblocks',
        'Printers, MFPs, scanners.',
        [
            'MFPs',
            'Printers',
            'Sticker Printers',
            'Scanners',
            'Plotters',
            'Barcode Scanners',
            'Accessories for plotters',
            'Accessories for peripherals',
            '',
        ],

        'Monitors and accessories.',
        [
            'Monitors',
            'Brackets for monitors',
            'Power supplies for monitors',
            '',
        ],

        'Platforms',
        'Servers',
        'Software.',
        [
            'Operating systems',
            'Office applications',
            'Antiviruses',
            '',
        ],

        'UPS, surge protectors and stabilizers.',
        [
            'Uninterruptible power supplies',
            'Network filters',
            'Extension cords',
            'Stabilizers',
            'Batteries for UPS',
            'Accessories for UPS',
            '',
        ],

        'Computer speakers.',
        [
            'CS_Portable speakers',
            'CS_Webcams',
            'CS_Input devices',
            'CS_Keyboards',
            'CS_Remote controls',
            'CS_Kits',
            'CS_Mouse pads',
            'CS_Mice',
            'CS_Joysticks and gamepads',
            'CS_Graphic tablets',
            'CS_Steering wheels',
            '',
        ],

        'Chairs for gamers',
        'KVM',
        'Cleaning products',
        '',
    ],

    'Computer accessories.',
    [
        'CA_Processors',
        'CA_Motherboards',
        'CA_RAM',
        'CA_RAM for laptops',
        'CA_Hard drives and accessories.',
        [
            'SSD',
            'Hard Drives 2.5',
            'Hard Drives 3.5',
            'Hard Drive Containers',
            'Accessories for hard drives',
            '',
        ],

        'Optical drives.',
        [
            'CD_DVD drives',
            'Optical External Drives',
            'Blu-Ray Drives',
            '',
        ],

        'Video cards',
        'Sound Cards',
        'Computer enclosures',
        'Power supplies',
        'Cooling system.',
        [
            'Fans',
            'Cooler',
            'Cooling systems for video cards',
            'Thermal pastes',
            '',
        ],

        'Server hardware.',
        [
            'Server motherboards',
            'Server processors',
            'Cooling systems for servers',
            'Server RAM',
            'Server enclosures',
            'Server hard drives',
            'Server controllers',
            'Power supplies for servers',
            'Server Accessories',
            'Server optical drives',
            '',
        ],

        'Controllers',
        '',
    ],

    'Laptops and accessories.',
    [
        'Laptops',
        'Laptop Accessories.',
        [
            'Laptop controllers',
            'Security system for laptops',
            'Laptop Bags',
            'Laptop stands',
            'Laptop Chargers',
            'Laptop docking stations',
            'Laptop batteries',
            '',
        ],

        'RAM for laptops',
        '',
    ],

    'Office equipment and consumables.',
    [
        'Printers, MFPs, scanners',
        'Consumables, cleaning materials.',
        [
            'materials_Cartridges for copying equipment',
            'materials_Laser cartridges',
            'materials_Ink cartridges',
            'materials_Photo drums',
            'materials_Photo paper',
            'materials_Cartridges for 3D printers',
            'materials_Consumables for bookbinders',
            'materials_Consumables for laminators',
            'materials_Toners',
            'materials_Paper',
            'materials_Films for printing',
            'materials_Thermal films',
            'materials_Spare parts for printing equipment',
            'materials_Refills_Ink',
            'materials_Developers',
            'materials_Cleaning products',
            '',
        ],

        'Telephony.',
        [
            'Additional handsets',
            'Wireless phones',
            'Wired phones',
            'IP Phones',
            '',
        ],

        'ACS.',
        [
            'Base stations',
            'Headsets for VoIP',
            'System boards for PBX',
            'System phones for PBX',
            'Digital PBX',
            '',
        ],

        'Pamphleteers',
        'Laminators',
        'Cutters',
        'Shredders',
        'Calculators',
        'Office furniture.',
        [
            'OF_Furniture accessories',
            'OF_Chairs',
            'OF_Cabinets and cabinets',
            'OF_Chairs for gamers',
            'OF_Tables and racks',
            'OF_Office chairs',
            '',
        ],

        'OEC_Banknote Detectors',
        'OEC_Batteries, accumulators, chargers',
    ],

    'Televisions, video and audio equipment.',
    [
        'Televisions',
        'Video equipment.',
        [
            'Satellite TV Sets',
            'Digital TV set-top boxes',
            'Media Players (Smart TV)',
            'Video Players (DVD, Blu-Ray)',
            'Projectors and accessories',
            '',
        ],

        'Audio equipment and accessories.',
        [
            'accessories_Portable speakers',
            'accessories_Headphones and headsets',
            'accessories_Car radios',
            'accessories_Music centers',
            'accessories_Microphones',
            'accessories_Acoustic cables',
            'accessories_Audio cables',
            'accessories_Home theaters',
            'accessories_Radio recorders',
            'accessories_MP3 players',
            'accessories_Radios and Walkie-talkies',
            'accessories_Receivers and amplifiers',
            '',
        ],

        'Game consoles and accessories.',
        [
            'Game consoles',
            '',
        ],

        'equpment_UPS, surge protectors and stabilizers',
        'equpment_TV Accessories.',
        [
            'TVa_Racks_Cabinets',
            'TVa_Video cables',
            'TVa_TV brackets',
            'TVa_Antennas',
            'TVa_Remote Controls',
            '',
        ],
    ],

    'External hard drives, memory cards, flash drives.',
    [
        'External Hard drives',
        'Memory cards.',
        [
            'microSD memory Cards',
            'SD Memory Cards',
            'Compact Flash Card',
            '',
        ],

        'USB flash drives',
        'Card readers',
        'Disks.',
        [
            'CD-R discs',
            'CD-RW discs',
            'DVD-R discs',
            'DVD-RW discs',
            'Disk Accessories',
            '',
        ],
    ],

    'Cables, cords, adapters, adapters.',
    [
        'USB splitters',
        'Network and telephone cables.',
        [
            'Network cables (Coils)',
            'Telephone cables',
            'Network cables (Patch cords)',
            '',
        ],

        'Acoustic cables',
        'USB cables and adapters.',
        [
            'USB Cable - Apple Lightning',
            'USB - USB Type-C Cable',
            'USB - micro-USB cables',
            'USB - mini-USB cables',
            'USB 2.0',
            'Cable USB 3.0',
            'Cable USB AM_BM',
            'Adapters',
            'USB Adapters Extension Cords',
            '',
        ],

        'Audio cables.',
        [
            'RCA - RCA cables',
            'Jack - to - jack cables',
            'Jack - RCA cables',
            'Toslink optical audio cables',
            '',
        ],

        'Video cables.',
        [
            'Mini DisplayPort',
            'HDMI cables',
            'VGA',
            'DVI',
            'SCART & S-video',
            'DVI_VGA_HDMI Adapter',
            'DisplayPort',
            '',
        ],

        'DVI_VGA_HDMI Splitters',
        'Interface cable.',
        [
            'SATA Cables',
            'Molex power cables',
            'Adapters_Adapters',
            '',
        ],

        'TV cables and splitters',
        'KVM devices and cables',
        'Power cables',
        'Audio_Video adapters and Adapters',
        'Cable for KVM',
        'Cables for controllers',
        '',
    ],

    'Appliances.',
    [
        'Preparation of products.',
        [
            'Blenders',
            'Milk frothers',
            'Kitchen scales',
            'Food processors',
            'Slicers',
            'Mixers',
            'Meat grinders',
            'Juicers',
            'Dryers for vegetables and fruits',
            'Thermopots',
            'Electric kettles',
            '',
        ],

        'Cooking.',
        [
            'Aerogrills, deep fryers',
            'Pancakes',
            'Waffle iron, hazelnuts, sandwich makers',
            'Ice cream makers',
            'Yogurt makers',
            'Kitchen tiles',
            'Microwave ovens',
            'Mini ovens',
            'Slow cookers',
            'Accessories for slow cookers',
            'Steamers',
            'Toasters',
            'Bread makers',
            'Electric grills',
            'Electroshashlychnitsy',
            '',
        ],

        'Making coffee.',
        [
            'Accessories for coffee makers',
            'Coffee makers and coffee machines',
            'Coffee grinders',
            '',
        ],

        'Other kitchen products.',
        [
            'Filter Cartridges',
            'Brackets for the kitchen',
            'Knives',
            'Water Filters',
            '',
        ],

        'Tableware and accessories.',
        [
            'TaC_Pots',
            'TaC_Saucepans',
            'TaC_Buckets',
            'TaC_Frying pans',
            'TaC_Baking pans',
            'TaC_Sets of dishes',
            'TaC_Tableware',
            'TaC_Knives',
            'TaC_Thermos flasks',
            'TaC_Teapots',
            'TaC_Lids for dishes',
            'TaC_Dishes for microwave ovens',
            'TaC_Other',
            '',
        ],

        'Home appliances.',
        [
            'Vacuum cleaners',
            'Electric windscreen wipers',
            'Irons',
            'Sewing machines',
            'Steamers and steam cleaners',
            'Accessories for vacuum cleaners',
            'Care of clothes and shoes',
            'Wall clock',
            'Clock with radio and alarm clocks',
            '',
        ],

        'Beauty and health.',
        [
            'Toothbrush Heads',
            'Hair dryers and styling appliances',
            'Razors',
            'Clippers',
            'Epilators',
            'Toothbrushes_Irrigators',
            'Floor scales',
            'Manicure sets',
            'Massagers',
            'Foot baths',
            'Tonometers_thermometers',
            '',
        ],

        'Large household appliances.',
        [
            'Washing machines',
            'Dishwashers',
            'Drying machines',
            'Kitchen stoves',
            'Hoods',
            '',
        ],

        'Built-in household appliances.',
        [
            'Built-in ovens',
            'Built-in cooktops',
            'Built-in dishwashers',
            'Built-in washing machines',
            'Built-in microwave ovens',
            'Built-in hoods',
            'Accessories and additional accessories',
            'Food Waste Shredders',
            '',
        ],

        'adapters_UPS, surge protectors and stabilizers',
        'adapters_Light.',
        [
            'Table lamps',
            'Energy-saving light bulbs',
            'Searchlights',
            '',
        ],

        'A_Batteries, accumulators, chargers',
        'A_Accessories and consumables for household appliances',
        '',
    ],

    'Climate equipment.',
    [
        'Weather stations',
        'Heated towel rails',
        'Underfloor heating',
        'Water heaters',
        'Heaters',
        'Air Purifiers',
        'Humidifiers',
        'Air conditioners',
        'Dehumidifiers',
        'Fans and extras equipment',
        'Electric Hand Dryers',
        '',
    ],

    'Tools and household goods.',
    [
        'Electro tool.',
        [
            'Compressors',
            'Thermal pistols',
            'Milling machines',
            'Screwdrivers, wrenches',
            'Electric drills, punchers, electric jackhammers',
            'Grinding machines',
            'Electric saws and electric jigsaws',
            'Electric planes',
            'Technical hair dryers',
            'Industrial vacuum cleaners',
            'Staplers construction',
            '',
        ],

        'Consumables for the tool.',
        [
            'Batteries for power tools',
            'Accessories for power tools',
            'Boers',
            'Circles, discs, cutters',
            'Hardware and fasteners',
            'Sets of bits and drills',
            'Saws and cloths',
            'Drills',
            'Staples for construction stapler',
            'Glue Gun Rods',
            'Milling cutters',
            'Sanding bands and sheets',
            'Electrodes',
            '',
        ],

        'Machines.',
        [
            'Machines_Stone-cutting machines',
            'Machines_Sawing machines',
            'Machines_Railmus machines',
            'Machines_Drilling machines',
            'Machines_Grinding machines',
            '',
        ],

        'Tool Kits',
        'Power electrical engineering.',
        [
            'Generators',
            'Welding machines',
            '',
        ],

        'Hand tools.',
        [
            'Lip Tool',
            'Keys',
            'Piercing-cutting and sawing tools',
            'Screwdrivers',
            'Consumables',
            'Garden and Household inventory',
            'Percussion and lever tools',
            'Plastering and painting tools',
            '',
        ],

        'Pneumatic equipment.',
        [
            'Accessories for pneumatic equipment',
            'Wrenches',
            'Spray gun',
            'Pistols',
            'Staplers',
            'Grinders',
            '',
        ],

        'Measuring instrument.',
        [
            'Rangefinders',
            'Measuring instruments',
            'Multimeter',
            'Roulette',
            'Goniometers and inclinometers',
            'Levels',
            '',
        ],

        'tools_Lanterns',
        'tools_Lamps',
        'tools_Blowtorches',
        'tools_Ladders and ladders',
        'tools_UPS, surge protectors and stabilizers',
        'tools_Electrics.',
        [
            'Cable, cords, cable channels, corrugated pipes',
            'Sockets, switches, dimmers',
            'Flaps, automation, counters',
            '',
        ],

        'Smart Home.',
        [
            'Accessories (smart home)',
            'Sensors and sockets',
            'Smart Light',
            '',
        ],

        'Personal protective equipment.',
        [
            'Safety glasses',
            'Helmets',
            'Gloves',
            'Respirators, Self-rescuers',
            '',
        ],

        'Construction equipment.',
        [
            'Concrete Mixers',
            'Jacks',
            'Jackhammers',
            '',
        ],
    ],

    'Products for cars.',
    [
        'PdC_Video recorders',
        'PdC_Inverters',
        'PdC_Automotive compressors',
        'PdC_GPS navigators',
        'PdC_Radar detectors',
        'PdC_Charging and charging devices',
        'PdC_High pressure washers',
        'PdC_Accessories for mini-washes',
        'PdC_Car Vacuum cleaners',
        'PdC_Holders in the car',
        'PdC_Sound in the car.',
        [
            'Sound_Acoustic cables',
            'Sound_Coaxial car acoustics',
            'Sound_Component autoacoustics',
            'Sound_Subwoofers',
            'Sound_Car radios',
            'Sound_Car Sound Amplifiers',
            '',
        ],

        'Auto chemistry and Auto cosmetics',
        'Car refrigerators',
        '',
    ],

    'Garden and leisure products.',
    [
        'Pumps.',
        [
            'Pumping stations',
            'Drainage pumps',
            'Sewage pumps',
            'Submersible pumps for wells',
            'Borehole pumps',
            'Circulation pumps',
            '',
        ],
        'Garden equipment.',
        [
            'Cultivators',
            'Tillers',
            'Cars',
            'Grass Trimmers',
            'Lawn mowers'
            'Blowers',
            'Scissors and brush cutters',
            'Accessories for garden equipment',
            'Watering equipment',
            '',
        ],
        'Mosquito and insect repellents',
        'High pressure washers',
        'Tractors and snowplows',
        'Travel and sports bags',
        'Thermos bags',
        ''
    ],

    'Video surveillance systems.',
    [
        'Video door phones',
        'Wireless video door phones',
        'Intercoms and video eyes',
        'Power supplies for video surveillance',
        'Accessories for intercoms',
        'Video surveillance kits',
        'Accessories for video surveillance systems',
        'IP cameras',
        'Video cameras for indoor installation',
        'Infrared spotlights',
        'Microphones for video systems',
        'Lenses for video cameras',
        'Camera brackets',
        'DVRs and video recorders',
        'Wireless and wired sensors',
        '',
    ],

    'Smart home PERENIO.',
    [
        'Safety',
        'Management',
        '',
    ],

    'Photo- video cameras and accessories.',
    [
        'Action cameras',
        'Accessories for Action cameras',
        'Bags for Photo and Video Cameras',
        'Tripods',
        'Batteries, accumulators, chargers',
        '',
    ],

    'Discounted goods.',
    [
        'Non-working non-guaranteed goods',
        'Laptops, tablets, smartphones.',
        [
            'Laptop_Monowheels and gyroscuters',
            'Laptop_Tablet PCs',
            'Laptop_Laptops',
            'Laptop_Bags and cases',
            '',
        ],

        'Computers and peripherals.',
        [
            'CaP_IP cameras',
            'CaP_Uninterruptible power supplies',
            'CaP_Cables, adapters, cords, adapters',
            'CaP_Columns',
            'CaP_Headphones and headsets',
            'CaP_Network equipment',
            'CaP_Monitors',
            '',
        ],

        'PC accessories.',
        [
            'PCa_Cooling system',
            'PCa_Motherboards',
            'PCa_RAM',
            '',
        ],

        'Televisions, audio-video,automotive equipment.',
        [
            'Car video recorders',
            '',
        ],

        'Appliances.',
        [
            'App_Small household appliances',
            'App_Built-in household appliances',
            '',
        ],

        'Office equipment.',
        [
            'OE_Office equipment',
            'OE_Consumables',
            'OE_Telephony',
            'OE_Various',
            '',
        ],

        'External hard drives, memory cards, flash drives.',
        [
            'drivers_Memory cards',
            ''
        ],
    ],

    'Sale.',
    [
        'Appliances.',
        [
            'appliances_Meat grinders',
            'appliances_Juicers',
            '',
        ],

        'Tools and household goods.',
        [
            'TaHG_Batteries for power tools',
            '',
        ],

        'Cables, cords, adapters, adapters.',
        [
            'adapters_USB cables and adapters',
            'adapters_USB splitters',
            'adapters_Cables and loops',
            'adapters_Cable in coils',
            'adapters_Cable of HDMI_VGA_DP_DVI',
            'adapters_Patch cords',
            '',
        ],

        'PC Accessories.',
        [
            'Sale_Power supplies',
            'Sale_Fans and coolers',
            'Sale_Controllers',
            'Sale_Enclosures',
            'Sale_Coolers for processors',
            'Sale_Motherboards',
            'Sale_SSD drives',
            'Sale_RAM',
            '',
        ],

        'Computer peripherals.',
        [
            'CP_Batteries for Photo_Video equipment',
            'CP_Webcams',
            'CP_UPS',
            'CP_Keyboards',
            'CP_Mouse pads',
            'CP_Columns',
            'CP_Kits (keyboard + mouse)',
            'CP_Monitors',
            'CP_Mice',
            'CP_Headphones and headsets',
            'CP_Projectors',
            'CP_Surge protectors and stabilizers',
            '',
        ],

        'Computers and laptops.',
        [
            'CaL_Laptop docking station',
            'CaL_Laptop Chargers',
            'CaL_Monoblocks',
            'CaL_Laptops',
            'CaL_Laptop bags and backpacks',
            '',
        ],

        'Kitchen appliances',
        'Tableware',
        'Network equipment.',
        [
            'NE_Wi-Fi routers and access points',
            'NE_PoE Adapters',
            'NE_VoIP Power Supplies',
            'NE_Switches',
            '',
        ],

        'Smartphones, tablets and gadgets.',
        [
            'gadget_Accessories for tablets and smartphones',
            'gadget_Graphic tablets',
            '',
        ],

        'Televisions, video and audio equipment.',
        [
            'Batteries, accumulators and chargers',
            'Brackets',
            'Adapters and containers for TV',
        ],
    ],
]
linksOnWeb_Sayte = {
    #'/Selfie sticks': 'https://www.oldi.ru/catalog/6569/',
    #'/Protective glasses and films.': 'https://www.oldi.ru/catalog/9747/'
}

#####################
# Выполняемые функции
#####################

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




'''Уравляющий код'''
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



work()

