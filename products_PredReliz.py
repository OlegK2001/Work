# Подключим необходимые нам библиотеки
import os
import glob
from selenium import webdriver
import re
import time
import gc

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
        ''
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
            '',
        ],
    ],
]
linksOnWeb_Sayte = {
    'Appliances./Home appliances./Irons.html': 'https://www.oldi.ru/catalog/8143/',
    'Appliances./Home appliances./Clock with radio and alarm clocks.html': 'https://www.oldi.ru/catalog/8311/',
    'Appliances./Home appliances./Electric windscreen wipers.html': 'https://www.oldi.ru/catalog/12700/',
    'Appliances./Home appliances./Vacuum cleaners.html': 'https://www.oldi.ru/catalog/8064/',
    'Appliances./Home appliances./Steamers and steam cleaners.html': 'https://www.oldi.ru/catalog/8048/',
    'Appliances./Home appliances./Care of clothes and shoes.html': 'https://www.oldi.ru/catalog/8436/',
    'Appliances./Home appliances./Accessories for vacuum cleaners.html': 'https://www.oldi.ru/catalog/11489/',
    'Appliances./Home appliances./Sewing machines.html': 'https://www.oldi.ru/catalog/9789/',
    'Appliances./Home appliances./Wall clock.html': 'https://www.oldi.ru/catalog/10891/',
    'Appliances./Cooking./Mini ovens.html': 'https://www.oldi.ru/catalog/8276/',
    'Appliances./Cooking./Waffle iron, hazelnuts, sandwich makers.html': 'https://www.oldi.ru/catalog/8289/',
    'Appliances./Cooking./Ice cream makers.html': 'https://www.oldi.ru/catalog/8324/',
    'Appliances./Cooking./Toasters.html': 'https://www.oldi.ru/catalog/8111/',
    'Appliances./Cooking./Electroshashlychnitsy.html': 'https://www.oldi.ru/catalog/8314/',
    'Appliances./Cooking./Aerogrills, deep fryers.html': 'https://www.oldi.ru/catalog/8162/',
    'Appliances./Cooking./Kitchen tiles.html': 'https://www.oldi.ru/catalog/12068/',
    'Appliances./Cooking./Yogurt makers.html': 'https://www.oldi.ru/catalog/11648/',
    'Appliances./Cooking./Electric grills.html': 'https://www.oldi.ru/catalog/8280/',
    'Appliances./Cooking./Accessories for slow cookers.html': 'https://www.oldi.ru/catalog/13565/',
    'Appliances./Cooking./Microwave ovens.html': 'https://www.oldi.ru/catalog/8065/',
    'Appliances./Cooking./Bread makers.html': 'https://www.oldi.ru/catalog/8112/',
    'Appliances./Cooking./Slow cookers.html': 'https://www.oldi.ru/catalog/8109/',
    'Appliances./Cooking./Steamers.html': 'https://www.oldi.ru/catalog/8110/',
    'Appliances./Cooking./Pancakes.html': 'https://www.oldi.ru/catalog/8247/',
    'Appliances./Preparation of products./Blenders.html': 'https://www.oldi.ru/catalog/8104/',
    'Appliances./Preparation of products./Electric kettles.html': 'https://www.oldi.ru/catalog/8033/',
    'Appliances./Preparation of products./Food processors.html': 'https://www.oldi.ru/catalog/8106/',
    'Appliances./Preparation of products./Dryers for vegetables and fruits.html': 'https://www.oldi.ru/catalog/8307/',
    'Appliances./Preparation of products./Thermopots.html': 'https://www.oldi.ru/catalog/8141/',
    'Appliances./Preparation of products./Meat grinders.html': 'https://www.oldi.ru/catalog/8032/',
    'Appliances./Preparation of products./Milk frothers.html': 'https://www.oldi.ru/catalog/8315/',
    'Appliances./Preparation of products./Kitchen scales.html': 'https://www.oldi.ru/catalog/8039/',
    'Appliances./Preparation of products./Mixers.html': 'https://www.oldi.ru/catalog/8108/',
    'Appliances./Preparation of products./Slicers.html': 'https://www.oldi.ru/catalog/8107/',
    'Appliances./Preparation of products./Juicers.html': 'https://www.oldi.ru/catalog/8036/',
    'Appliances./Other kitchen products./Water Filters.html': 'https://www.oldi.ru/catalog/8142/',
    'Appliances./Other kitchen products./Knives.html': 'https://www.oldi.ru/catalog/8361/',
    'Appliances./Other kitchen products./Filter Cartridges.html': 'https://www.oldi.ru/catalog/13298/',
    'Appliances./Other kitchen products./Brackets for the kitchen.html': 'https://www.oldi.ru/catalog/8608/',
    'Appliances./Tableware and accessories./TaC_Thermos flasks.html': 'https://www.oldi.ru/catalog/8956/',
    'Appliances./Tableware and accessories./TaC_Frying pans.html': 'https://www.oldi.ru/catalog/8881/',
    'Appliances./Tableware and accessories./TaC_Buckets.html': 'https://www.oldi.ru/catalog/12643/',
    'Appliances./Tableware and accessories./TaC_Knives.html': 'https://www.oldi.ru/catalog/8879/',
    'Appliances./Tableware and accessories./TaC_Other.html': 'https://www.oldi.ru/catalog/13689/',
    'Appliances./Tableware and accessories./TaC_Saucepans.html': 'https://www.oldi.ru/catalog/12644/',
    'Appliances./Tableware and accessories./TaC_Lids for dishes.html': 'https://www.oldi.ru/catalog/10872/',
    'Appliances./Tableware and accessories./TaC_Tableware.html': 'https://www.oldi.ru/catalog/8882/',
    'Appliances./Tableware and accessories./TaC_Dishes for microwave ovens.html': 'https://www.oldi.ru/catalog/10873/',
    'Appliances./Tableware and accessories./TaC_Sets of dishes.html': 'https://www.oldi.ru/catalog/8880/',
    'Appliances./Tableware and accessories./TaC_Baking pans.html': 'https://www.oldi.ru/catalog/9121/',
    'Appliances./Tableware and accessories./TaC_Pots.html': 'https://www.oldi.ru/catalog/8861/',
    'Appliances./Tableware and accessories./TaC_Teapots.html': 'https://www.oldi.ru/catalog/8957/',
    'Appliances./Making coffee./Coffee makers and coffee machines.html': 'https://www.oldi.ru/catalog/8211/',
    'Appliances./Making coffee./Coffee grinders.html': 'https://www.oldi.ru/catalog/8212/',
    'Appliances./Making coffee./Accessories for coffee makers.html': 'https://www.oldi.ru/catalog/13297/',
    'Appliances./Beauty and health./Tonometers_thermometers.html': 'https://www.oldi.ru/catalog/15754/',
    'Appliances./Beauty and health./Razors.html': 'https://www.oldi.ru/catalog/8208/',
    'Appliances./Beauty and health./Foot baths.html': 'https://www.oldi.ru/catalog/10892/',
    'Appliances./Beauty and health./Massagers.html': 'https://www.oldi.ru/catalog/8244/',
    'Appliances./Beauty and health./Epilators.html': 'https://www.oldi.ru/catalog/8210/',
    'Appliances./Beauty and health./Hair dryers and styling appliances.html': 'https://www.oldi.ru/catalog/8163/',
    'Appliances./Beauty and health./Toothbrushes_Irrigators.html': 'https://www.oldi.ru/catalog/15754/',
    'Appliances./Beauty and health./Floor scales.html': 'https://www.oldi.ru/catalog/8031/',
    'Appliances./Beauty and health./Clippers.html': 'https://www.oldi.ru/catalog/8209/',
    'Appliances./Beauty and health./Toothbrush Heads.html': 'https://www.oldi.ru/catalog/12712/',
    'Appliances./Beauty and health./Manicure sets.html': 'https://www.oldi.ru/catalog/8246/',
    'Appliances./Built-in household appliances./Built-in ovens.html': 'https://www.oldi.ru/catalog/10862/',
    'Appliances./Built-in household appliances./Built-in hoods.html': 'https://www.oldi.ru/catalog/11971/',
    'Appliances./Built-in household appliances./Accessories and additional accessories.html': 'https://www.oldi.ru/catalog/10861/',
    'Appliances./Built-in household appliances./Food Waste Shredders.html': 'https://www.oldi.ru/catalog/12930/',
    'Appliances./Built-in household appliances./Built-in dishwashers.html': 'https://www.oldi.ru/catalog/10858/',
    'Appliances./Built-in household appliances./Built-in washing machines.html': 'https://www.oldi.ru/catalog/10859/',
    'Appliances./Built-in household appliances./Built-in cooktops.html': 'https://www.oldi.ru/catalog/10854/',
    'Appliances./Built-in household appliances./Built-in microwave ovens.html': 'https://www.oldi.ru/catalog/11969/',
    'Appliances./Large household appliances./Drying machines.html': 'https://www.oldi.ru/catalog/10869/',
    'Appliances./Large household appliances./Washing machines.html': 'https://www.oldi.ru/catalog/9697/',
    'Appliances./Large household appliances./Dishwashers.html': 'https://www.oldi.ru/catalog/10868/',
    'Appliances./Large household appliances./Kitchen stoves.html': 'https://www.oldi.ru/catalog/7975/',
    'Appliances./Large household appliances./Hoods.html': 'https://www.oldi.ru/catalog/9735/',
    'Appliances./adapters_Light./Energy-saving light bulbs.html': 'https://www.oldi.ru/catalog/7579/',
    'Appliances./adapters_Light./Searchlights.html': 'https://www.oldi.ru/catalog/8164/',
    'Appliances./adapters_Light./Table lamps.html': 'https://www.oldi.ru/catalog/13583/',
    'Appliances./adapters_UPS, surge protectors and stabilizers.html': 'https://www.oldi.ru/catalog/6628/',
    'Appliances./A_Batteries, accumulators, chargers.html': 'https://www.oldi.ru/catalog/7719/',
    'Appliances./A_Accessories and consumables for household appliances.html': 'https://www.oldi.ru/catalog/10867/',

    'Cables, cords, adapters, adapters./Interface cable./Adapters_Adapters.html': 'https://www.oldi.ru/catalog/8494/',
    'Cables, cords, adapters, adapters./Interface cable./Molex power cables.html': 'https://www.oldi.ru/catalog/9682/',
    'Cables, cords, adapters, adapters./Interface cable./SATA Cables.html': 'https://www.oldi.ru/catalog/8492/',
    'Cables, cords, adapters, adapters./Audio cables./RCA - RCA cables.html': 'https://www.oldi.ru/catalog/9665/',
    'Cables, cords, adapters, adapters./Audio cables./Toslink optical audio cables.html': 'https://www.oldi.ru/catalog/9669/',
    'Cables, cords, adapters, adapters./Audio cables./Jack - to - jack cables.html': 'https://www.oldi.ru/catalog/9666/',
    'Cables, cords, adapters, adapters./Audio cables./Jack - RCA cables.html': 'https://www.oldi.ru/catalog/9667/',
    'Cables, cords, adapters, adapters./Network and telephone cables./Telephone cables.html': 'https://www.oldi.ru/catalog/9672/',
    'Cables, cords, adapters, adapters./Network and telephone cables./Network cables (Coils).html': 'https://www.oldi.ru/catalog/7229/',
    'Cables, cords, adapters, adapters./Network and telephone cables./Network cables (Patch cords).html': 'https://www.oldi.ru/catalog/9673/',
    'Cables, cords, adapters, adapters./USB cables and adapters./USB - mini-USB cables.html': 'https://www.oldi.ru/catalog/9678/',
    'Cables, cords, adapters, adapters./USB cables and adapters./Adapters.html': 'https://www.oldi.ru/catalog/8489/',
    'Cables, cords, adapters, adapters./USB cables and adapters./USB - micro-USB cables.html': 'https://www.oldi.ru/catalog/9678/',
    'Cables, cords, adapters, adapters./USB cables and adapters./USB - USB Type-C Cable.html': 'https://www.oldi.ru/catalog/11627/',
    'Cables, cords, adapters, adapters./USB cables and adapters./USB Adapters Extension Cords.html': 'https://www.oldi.ru/catalog/9674/',
    'Cables, cords, adapters, adapters./USB cables and adapters./USB 2.0.html': 'https://www.oldi.ru/catalog/6925/',
    'Cables, cords, adapters, adapters./USB cables and adapters./USB Cable - Apple Lightning.html': 'https://www.oldi.ru/catalog/9679/',
    'Cables, cords, adapters, adapters./USB cables and adapters./Cable USB AM_BM.html': 'https://www.oldi.ru/catalog/9676/',
    'Cables, cords, adapters, adapters./USB cables and adapters./Cable USB 3.0.html': 'https://www.oldi.ru/catalog/8488/',
    'Cables, cords, adapters, adapters./Video cables./DVI.html': 'https://www.oldi.ru/catalog/8483/',
    'Cables, cords, adapters, adapters./Video cables./Mini DisplayPort.html': 'https://www.oldi.ru/catalog/15753/',
    'Cables, cords, adapters, adapters./Video cables./VGA.html': 'https://www.oldi.ru/catalog/8484/',
    'Cables, cords, adapters, adapters./Video cables./HDMI cables.html': 'https://www.oldi.ru/catalog/6927/',
    'Cables, cords, adapters, adapters./Video cables./SCART & S-video.html': 'https://www.oldi.ru/catalog/9670/',
    'Cables, cords, adapters, adapters./Video cables./DVI_VGA_HDMI Adapter.html': 'https://www.oldi.ru/catalog/8485/',
    'Cables, cords, adapters, adapters./Video cables./DisplayPort.html': 'https://www.oldi.ru/catalog/8490/',
    'Cables, cords, adapters, adapters./Power cables.html': 'https://www.oldi.ru/catalog/9554/',
    'Cables, cords, adapters, adapters./Audio_Video adapters and Adapters.html': 'https://www.oldi.ru/catalog/10971/',
    'Cables, cords, adapters, adapters./USB splitters.html': 'https://www.oldi.ru/catalog/7111/',
    'Cables, cords, adapters, adapters./DVI_VGA_HDMI Splitters.html': 'https://www.oldi.ru/catalog/9655/',
    'Cables, cords, adapters, adapters./KVM devices and cables.html': 'https://www.oldi.ru/catalog/8480/',
    'Cables, cords, adapters, adapters./Cables for controllers.html': 'https://www.oldi.ru/catalog/7117/',
    'Cables, cords, adapters, adapters./Acoustic cables.html': 'https://www.oldi.ru/catalog/13015/',
    'Cables, cords, adapters, adapters./Cable for KVM.html': 'https://www.oldi.ru/catalog/7615/',
    'Cables, cords, adapters, adapters./TV cables and splitters.html': 'https://www.oldi.ru/catalog/6926/',

    'Climate equipment./Air Purifiers.html': 'https://www.oldi.ru/catalog/8021/',
    'Climate equipment./Fans and extras equipment.html': 'https://www.oldi.ru/catalog/8013/',
    'Climate equipment./Heated towel rails.html': 'https://www.oldi.ru/catalog/13019/',
    'Climate equipment./Weather stations.html': 'https://www.oldi.ru/catalog/8120/',
    'Climate equipment./Heaters.html': 'https://www.oldi.ru/catalog/8020/',
    'Climate equipment./Humidifiers.html': 'https://www.oldi.ru/catalog/8022/',
    'Climate equipment./Electric Hand Dryers.html': 'https://www.oldi.ru/catalog/8203/',
    'Climate equipment./Underfloor heating.html': 'https://www.oldi.ru/catalog/13564/',
    'Climate equipment./Water heaters.html': 'https://www.oldi.ru/catalog/8120/',
    'Climate equipment./Dehumidifiers.html': 'https://www.oldi.ru/catalog/8593/',
    'Climate equipment./Air conditioners.html': 'https://www.oldi.ru/catalog/8021/',

    'Computer accessories./Server hardware./Server hard drives.html': 'https://www.oldi.ru/catalog/7082/',
    'Computer accessories./Server hardware./Server optical drives.html': 'https://www.oldi.ru/catalog/11322/',
    'Computer accessories./Server hardware./Server RAM.html': 'https://www.oldi.ru/catalog/7080/',
    'Computer accessories./Server hardware./Power supplies for servers.html': 'https://www.oldi.ru/catalog/7234/',
    'Computer accessories./Server hardware./Cooling systems for servers.html': 'https://www.oldi.ru/catalog/7863/',
    'Computer accessories./Server hardware./Server Accessories.html': 'https://www.oldi.ru/catalog/11323/',
    'Computer accessories./Server hardware./Server enclosures.html': 'https://www.oldi.ru/catalog/7081/',
    'Computer accessories./Server hardware./Server processors.html': 'https://www.oldi.ru/catalog/6876/',
    'Computer accessories./Server hardware./Server controllers.html': 'https://www.oldi.ru/catalog/7083/',
    'Computer accessories./Server hardware./Server motherboards.html': 'https://www.oldi.ru/catalog/7078/',
    'Computer accessories./Cooling system./Fans.html': 'https://www.oldi.ru/catalog/7231/',
    'Computer accessories./Cooling system./Cooler.html': 'https://www.oldi.ru/catalog/6548/',
    'Computer accessories./Cooling system./Cooling systems for video cards.html': 'https://www.oldi.ru/catalog/7131/',
    'Computer accessories./Cooling system./Thermal pastes.html': 'https://www.oldi.ru/catalog/6937/',
    'Computer accessories./Optical drives./CD_DVD drives.html': 'https://www.oldi.ru/catalog/6842/',
    'Computer accessories./Optical drives./Blu-Ray Drives.html': 'https://www.oldi.ru/catalog/7193/',
    'Computer accessories./Optical drives./Optical External Drives.html': 'https://www.oldi.ru/catalog/6843/',
    'Computer accessories./CA_Hard drives and accessories./Hard Drives 2.5.html': 'https://www.oldi.ru/catalog/15065/',
    'Computer accessories./CA_Hard drives and accessories./Hard Drives 3.5.html': 'https://www.oldi.ru/catalog/7107/',
    'Computer accessories./CA_Hard drives and accessories./Accessories for hard drives.html': 'https://www.oldi.ru/catalog/7112/',
    'Computer accessories./CA_Hard drives and accessories./Hard Drive Containers.html': 'https://www.oldi.ru/catalog/6652/',
    'Computer accessories./CA_Hard drives and accessories./SSD.html': 'https://www.oldi.ru/catalog/13266/',
    'Computer accessories./CA_RAM for laptops.html': 'https://www.oldi.ru/catalog/7621/',
    'Computer accessories./CA_Processors.html': 'https://www.oldi.ru/catalog/6869/',
    'Computer accessories./Computer enclosures.html': 'https://www.oldi.ru/catalog/6508/',
    'Computer accessories./Controllers.html': 'https://www.oldi.ru/catalog/8521/',
    'Computer accessories./Sound Cards.html': 'https://www.oldi.ru/catalog/6763/',
    'Computer accessories./CA_Motherboards.html': 'https://www.oldi.ru/catalog/6569/',
    'Computer accessories./Power supplies.html': 'https://www.oldi.ru/catalog/6499/',
    'Computer accessories./Video cards.html': 'https://www.oldi.ru/catalog/6571/',
    'Computer accessories./CA_RAM.html': 'https://www.oldi.ru/catalog/6587/',

    '/Computers and peripherals./Printers, MFPs, scanners./Accessories for peripherals.html': 'https://www.oldi.ru/catalog/7086/',
    '/Computers and peripherals./Printers, MFPs, scanners./Printers.html': 'https://www.oldi.ru/catalog/6863/',
    '/Computers and peripherals./Printers, MFPs, scanners./Sticker Printers.html': 'https://www.oldi.ru/catalog/8582/',
    '/Computers and peripherals./Printers, MFPs, scanners./Scanners.html': 'https://www.oldi.ru/catalog/7984/',
    '/Computers and peripherals./Printers, MFPs, scanners./Accessories for plotters.html': 'https://www.oldi.ru/catalog/10017/',
    '/Computers and peripherals./Printers, MFPs, scanners./MFPs.html': 'https://www.oldi.ru/catalog/6849/',
    '/Computers and peripherals./Printers, MFPs, scanners./Barcode Scanners.html': 'https://www.oldi.ru/catalog/13568/',
    '/Computers and peripherals./Printers, MFPs, scanners./Plotters.html': 'https://www.oldi.ru/catalog/7085/',
    '/Computers and peripherals./Software./Antiviruses.html': 'https://www.oldi.ru/catalog/6479/',
    '/Computers and peripherals./Software./Operating systems.html': 'https://www.oldi.ru/catalog/7141/',
    '/Computers and peripherals./Software./Office applications.html': 'https://www.oldi.ru/catalog/7142/',
    '/Computers and peripherals./Computer speakers./CS_Remote controls.html': 'https://www.oldi.ru/catalog/13571/',
    '/Computers and peripherals./Computer speakers./CS_Portable speakers.html': 'https://www.oldi.ru/catalog/11603/',
    '/Computers and peripherals./Computer speakers./CS_Mice.html': 'https://www.oldi.ru/catalog/6963/',
    '/Computers and peripherals./Computer speakers./CS_Mouse pads.html': 'https://www.oldi.ru/catalog/7093/',
    '/Computers and peripherals./Computer speakers./CS_Keyboards.html': 'https://www.oldi.ru/catalog/13572/',
    '/Computers and peripherals./Computer speakers./CS_Joysticks and gamepads.html': 'https://www.oldi.ru/catalog/6948/',
    '/Computers and peripherals./Computer speakers./CS_Input devices.html': 'https://www.oldi.ru/catalog/6947/',
    '/Computers and peripherals./Computer speakers./CS_Kits.html': 'https://www.oldi.ru/catalog/6952/',
    '/Computers and peripherals./Computer speakers./CS_Graphic tablets.html': 'https://www.oldi.ru/catalog/7096/',
    '/Computers and peripherals./Computer speakers./CS_Steering wheels.html': 'https://www.oldi.ru/catalog/6971/',
    '/Computers and peripherals./Computer speakers./CS_Webcams.html': 'https://www.oldi.ru/catalog/6514/',
    '/Computers and peripherals./Monitors and accessories./Brackets for monitors.html': 'https://www.oldi.ru/catalog/7642/',
    '/Computers and peripherals./Monitors and accessories./Monitors.html': 'https://www.oldi.ru/catalog/6488/',
    '/Computers and peripherals./Monitors and accessories./Power supplies for monitors.html': 'https://www.oldi.ru/catalog/12769/',
    '/Computers and peripherals./OLDI computers./Mini PC OLDI.html': 'https://www.oldi.ru/catalog/15669/',
    '/Computers and peripherals./OLDI computers./Gaming.html': 'https://www.oldi.ru/catalog/15658/',
    '/Computers and peripherals./OLDI computers./For home.html': 'https://www.oldi.ru/catalog/15659/',
    '/Computers and peripherals./OLDI computers./OLDI monoblocks.html': 'https://www.oldi.ru/catalog/15670/',
    '/Computers and peripherals./OLDI computers./For the office.html': 'https://www.oldi.ru/catalog/15660/',
    '/Computers and peripherals./OLDI computers./PC with Microsoft Office.html': 'https://www.oldi.ru/catalog/15713/',
    '/Computers and peripherals./UPS, surge protectors and stabilizers./Network filters.html': 'https://www.oldi.ru/catalog/6635/',
    '/Computers and peripherals./UPS, surge protectors and stabilizers./Batteries for UPS.html': 'https://www.oldi.ru/catalog/6633/',
    '/Computers and peripherals./UPS, surge protectors and stabilizers./Accessories for UPS.html': 'https://www.oldi.ru/catalog/7140/',
    '/Computers and peripherals./UPS, surge protectors and stabilizers./Uninterruptible power supplies.html': 'https://www.oldi.ru/catalog/6629/',
    '/Computers and peripherals./UPS, surge protectors and stabilizers./Stabilizers.html': 'https://www.oldi.ru/catalog/9306/',
    '/Computers and peripherals./UPS, surge protectors and stabilizers./Extension cords.html': 'https://www.oldi.ru/catalog/9305/',

    '/Discounted goods./Non-working non-guaranteed goods.html': 'https://www.oldi.ru/catalog/13343/',
    '/Discounted goods./Office equipment./OE_Various.html': 'https://www.oldi.ru/catalog/12784/',
    '/Discounted goods./Office equipment./OE_Office equipment.html': 'https://www.oldi.ru/catalog/12864/',
    '/Discounted goods./Office equipment./OE_Consumables.html': 'https://www.oldi.ru/catalog/12806/',
    '/Discounted goods./Office equipment./OE_Telephony.html': 'https://www.oldi.ru/catalog/12808/',
    '/Discounted goods./Laptops, tablets, smartphones./Laptop_Bags and cases.html': 'https://www.oldi.ru/catalog/12788/',
    '/Discounted goods./Laptops, tablets, smartphones./Laptop_Laptops.html': 'https://www.oldi.ru/catalog/12786/',
    '/Discounted goods./Laptops, tablets, smartphones./Laptop_Tablet PCs.html': 'https://www.oldi.ru/catalog/12785/',
    '/Discounted goods./Laptops, tablets, smartphones./Laptop_Monowheels and gyroscuters.html': 'https://www.oldi.ru/catalog/13337/',
    '/Discounted goods./External hard drives, memory cards, flash drives./drivers_Memory cards.html': 'https://www.oldi.ru/catalog/12894/',
    '/Discounted goods./Appliances./App_Built-in household appliances.html': 'https://www.oldi.ru/catalog/12804/',
    '/Discounted goods./Appliances./App_Small household appliances.html': 'https://www.oldi.ru/catalog/12802/',
    '/Discounted goods./Computers and peripherals./CaP_Columns.html': 'https://www.oldi.ru/catalog/13342/',
    '/Discounted goods./Computers and peripherals./CaP_Network equipment.html': 'https://www.oldi.ru/catalog/12859/',
    '/Discounted goods./Computers and peripherals./CaP_Cables, adapters, cords, adapters.html': 'https://www.oldi.ru/catalog/12856/',
    '/Discounted goods./Computers and peripherals./CaP_Uninterruptible power supplies.html': 'https://www.oldi.ru/catalog/12855/',
    '/Discounted goods./Computers and peripherals./CaP_IP cameras.html': 'https://www.oldi.ru/catalog/15159/',
    '/Discounted goods./Computers and peripherals./CaP_Headphones and headsets.html': 'https://www.oldi.ru/catalog/13338/',
    '/Discounted goods./Computers and peripherals./CaP_Monitors.html': 'https://www.oldi.ru/catalog/12793/',
    '/Discounted goods./PC accessories./PCa_Motherboards.html': 'https://www.oldi.ru/catalog/12796/',
    '/Discounted goods./PC accessories./PCa_Cooling system.html': 'https://www.oldi.ru/catalog/12854/',
    '/Discounted goods./PC accessories./PCa_RAM.html': 'https://www.oldi.ru/catalog/12799/',
    '/Discounted goods./Televisions, audio-video,automotive equipment./Car video recorders.html': 'https://www.oldi.ru/catalog/13334/',

    '/External hard drives, memory cards, flash drives./USB flash drives.html': 'https://www.oldi.ru/catalog/6839/',
    '/External hard drives, memory cards, flash drives./External Hard drives.html': 'https://www.oldi.ru/catalog/7806/',
    '/External hard drives, memory cards, flash drives./Card readers.html': 'https://www.oldi.ru/catalog/6828/',
    '/External hard drives, memory cards, flash drives./Memory cards./Compact Flash Card.html': 'https://www.oldi.ru/catalog/6829/',
    '/External hard drives, memory cards, flash drives./Memory cards./microSD memory Cards.html': 'https://www.oldi.ru/catalog/7823/',
    '/External hard drives, memory cards, flash drives./Memory cards./SD Memory Cards.html': 'https://www.oldi.ru/catalog/6838/',
    '/External hard drives, memory cards, flash drives./Disks./DVD-R discs.html': 'https://www.oldi.ru/catalog/7147/',
    '/External hard drives, memory cards, flash drives./Disks./CD-R discs.html': 'https://www.oldi.ru/catalog/11856/',
    '/External hard drives, memory cards, flash drives./Disks./Disk Accessories.html': 'https://www.oldi.ru/catalog/6904/',
    '/External hard drives, memory cards, flash drives./Disks./CD-RW discs.html': 'https://www.oldi.ru/catalog/7225/',
    '/External hard drives, memory cards, flash drives./Disks./DVD-RW discs.html': 'https://www.oldi.ru/catalog/7226/',

    '/Garden and leisure products./High pressure washers.html': 'https://www.oldi.ru/catalog/12873/',
    '/Garden and leisure products./Thermos bags.html': 'https://www.oldi.ru/catalog/8291/',
    '/Garden and leisure products./Travel and sports bags.html': 'https://www.oldi.ru/catalog/10994/',
    '/Garden and leisure products./Mosquito and insect repellents.html': 'https://www.oldi.ru/catalog/9268/',
    '/Garden and leisure products./Tractors and snowplows.html': 'https://www.oldi.ru/catalog/12757/',
    '/Garden and leisure products./Pumps./Pumping stations.html': 'https://www.oldi.ru/catalog/15481/',
    '/Garden and leisure products./Pumps./Submersible pumps for wells.html': 'https://www.oldi.ru/catalog/15483/',
    '/Garden and leisure products./Pumps./Circulation pumps.html': 'https://www.oldi.ru/catalog/15480/',
    '/Garden and leisure products./Pumps./Drainage pumps.html': 'https://www.oldi.ru/catalog/15482/',
    '/Garden and leisure products./Pumps./Sewage pumps.html': 'https://www.oldi.ru/catalog/15484/',
    '/Garden and leisure products./Pumps./Borehole pumps.html': 'https://www.oldi.ru/catalog/15485/',
    '/Garden and leisure products./Garden equipment./Tillers.html': 'https://www.oldi.ru/catalog/13068/',
    '/Garden and leisure products./Garden equipment./Cultivators.html': 'https://www.oldi.ru/catalog/13067/',
    '/Garden and leisure products./Garden equipment./Cars.html': 'https://www.oldi.ru/catalog/13069/',
    '/Garden and leisure products./Garden equipment./Scissors and brush cutters.html': 'https://www.oldi.ru/catalog/10780/',
    '/Garden and leisure products./Garden equipment./Watering equipment.html': 'https://www.oldi.ru/catalog/11319/',
    '/Garden and leisure products./Garden equipment./Grass Trimmers.html': 'https://www.oldi.ru/catalog/10753/',
    '/Garden and leisure products./Garden equipment./Lawn mowersBlowers.html': 'https://www.oldi.ru/catalog/10782/',
    '/Garden and leisure products./Garden equipment./Accessories for garden equipment.html': 'https://www.oldi.ru/catalog/10784/',

    '/Laptops and accessories./Laptops.html': 'https://www.oldi.ru/catalog/6535/',
    '/Laptops and accessories./RAM for laptops.html': 'https://www.oldi.ru/catalog/7621/',
    '/Laptops and accessories./Laptop Accessories./Laptop Bags.html': 'https://www.oldi.ru/catalog/6585/',
    '/Laptops and accessories./Laptop Accessories./Laptop Chargers.html': 'https://www.oldi.ru/catalog/11444/',
    '/Laptops and accessories./Laptop Accessories./Laptop controllers.html': 'https://www.oldi.ru/catalog/14146/',
    '/Laptops and accessories./Laptop Accessories./Laptop stands.html': 'https://www.oldi.ru/catalog/7666/',
    '/Laptops and accessories./Laptop Accessories./Security system for laptops.html': 'https://www.oldi.ru/catalog/14145/',
    '/Laptops and accessories./Laptop Accessories./Laptop batteries.html': 'https://www.oldi.ru/catalog/7667/',
    '/Laptops and accessories./Laptop Accessories./Laptop docking stations.html': 'https://www.oldi.ru/catalog/13529/',

    '/NetworkEquipment./Print servers.html': 'https://www.oldi.ru/catalog/7137/',
    '/NetworkEquipment./Network Wireless Adapters.html': 'https://www.oldi.ru/catalog/6614/',
    '/NetworkEquipment./Extension modules.html': 'https://www.oldi.ru/catalog/13419/',
    '/NetworkEquipment./Network cards.html': 'https://www.oldi.ru/catalog/6610/',
    '/NetworkEquipment./Routers and firewalls.html': 'https://www.oldi.ru/catalog/8525/',
    '/NetworkEquipment./Optical Patch Cords.html': 'https://www.oldi.ru/catalog/9693/',
    '/NetworkEquipment./Media converters, transceivers.html': 'https://www.oldi.ru/catalog/9790/',
    '/NetworkEquipment./Related network equipment.html': 'https://www.oldi.ru/catalog/7972/',
    '/NetworkEquipment./Switches.html': 'https://www.oldi.ru/catalog/6612/',
    '/NetworkEquipment./Bluetooth Adapters.html': 'https://www.oldi.ru/catalog/7118/',
    '/NetworkEquipment./PoE Adapters.html': 'https://www.oldi.ru/catalog/13533/',
    '/NetworkEquipment./Powerline equipment.html': 'https://www.oldi.ru/catalog/13525/',
    '/NetworkEquipment./Signal amplifiers_Repeaters.html': 'https://www.oldi.ru/catalog/13113/',
    '/NetworkEquipment./Signal transmission equipment.html': 'https://www.oldi.ru/catalog/11332/',
    '/NetworkEquipment./Wi-Fi routers and access points.html': 'https://www.oldi.ru/catalog/7859/',
    '/NetworkEquipment./Antennas.html': 'https://www.oldi.ru/catalog/7534/',
    '/NetworkEquipment./Mobile 3G_4G modems.html': 'https://www.oldi.ru/catalog/13112/',
    '/NetworkEquipment./NAS Network Storage.html': 'https://www.oldi.ru/catalog/7809/',
    '/NetworkEquipment./Components for the installation of networks./Cabinets, racks.html': 'https://www.oldi.ru/catalog/10990/',
    '/NetworkEquipment./Components for the installation of networks./Connectors.html': 'https://www.oldi.ru/catalog/6706/',
    '/NetworkEquipment./Components for the installation of networks./Installation equipment.html': 'https://www.oldi.ru/catalog/6711/',
    '/NetworkEquipment./Components for the installation of networks./Sockets for network equipment.html': 'https://www.oldi.ru/catalog/13406/',
    '/NetworkEquipment./Components for the installation of networks./Tools for installation and testing.html': 'https://www.oldi.ru/catalog/6692/',

    '/Office equipment and consumables./Printers, MFPs, scanners.html': 'https://www.oldi.ru/catalog/6848/',
    '/Office equipment and consumables./OEC_Banknote Detectors.html': 'https://www.oldi.ru/catalog/13575/',
    '/Office equipment and consumables./Cutters.html': 'https://www.oldi.ru/catalog/6486/',
    '/Office equipment and consumables./Pamphleteers.html': 'https://www.oldi.ru/catalog/9756/',
    '/Office equipment and consumables./Shredders.html': 'https://www.oldi.ru/catalog/6858/',
    '/Office equipment and consumables./Laminators.html': 'https://www.oldi.ru/catalog/8584/',
    '/Office equipment and consumables./Calculators.html': 'https://www.oldi.ru/catalog/7884/',
    '/Office equipment and consumables./ACS./Base stations.html': 'https://www.oldi.ru/catalog/10085/',
    '/Office equipment and consumables./ACS./System boards for PBX.html': 'https://www.oldi.ru/catalog/10091/',
    '/Office equipment and consumables./ACS./Digital PBX.html': 'https://www.oldi.ru/catalog/10093/',
    '/Office equipment and consumables./ACS./System phones for PBX.html': 'https://www.oldi.ru/catalog/10092/',
    '/Office equipment and consumables./ACS./Headsets for VoIP.html': 'https://www.oldi.ru/catalog/15662/',
    '/Office equipment and consumables./Office furniture./OF_Cabinets and cabinets.html': 'https://www.oldi.ru/catalog/11472/',
    '/Office equipment and consumables./Office furniture./OF_Chairs.html': 'https://www.oldi.ru/catalog/13567/',
    '/Office equipment and consumables./Office furniture./OF_Tables and racks.html': 'https://www.oldi.ru/catalog/11345/',
    '/Office equipment and consumables./Office furniture./OF_Furniture accessories.html': 'https://www.oldi.ru/catalog/10992/',
    '/Office equipment and consumables./Office furniture./OF_Chairs for gamers.html': 'https://www.oldi.ru/catalog/11343/',
    '/Office equipment and consumables./Office furniture./OF_Office chairs.html': 'https://www.oldi.ru/catalog/7655/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Cleaning products.html': 'https://www.oldi.ru/catalog/6919/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Spare parts for printing equipment.html': 'https://www.oldi.ru/catalog/10989/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Refills_Ink.html': 'https://www.oldi.ru/catalog/13532/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Consumables for bookbinders.html': 'https://www.oldi.ru/catalog/8585/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Thermal films.html': 'https://www.oldi.ru/catalog/11330/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Paper.html': 'https://www.oldi.ru/catalog/6880/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Cartridges for copying equipment.html': 'https://www.oldi.ru/catalog/7146/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Photo paper.html': 'https://www.oldi.ru/catalog/13574/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Cartridges for 3D printers.html': 'https://www.oldi.ru/catalog/11437/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Consumables for laminators.html': 'https://www.oldi.ru/catalog/7221/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Films for printing.html': 'https://www.oldi.ru/catalog/11328/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Laser cartridges.html': 'https://www.oldi.ru/catalog/14925/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Toners.html': 'https://www.oldi.ru/catalog/10988/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Ink cartridges.html': 'https://www.oldi.ru/catalog/14926/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Developers.html': 'https://www.oldi.ru/catalog/11329/',
    '/Office equipment and consumables./Consumables, cleaning materials./materials_Photo drums.html': 'https://www.oldi.ru/catalog/13573/',
    '/Office equipment and consumables./Telephony./Additional handsets.html': 'https://www.oldi.ru/catalog/11430/',
    '/Office equipment and consumables./Telephony./IP Phones.html': 'https://www.oldi.ru/catalog/7157/',
    '/Office equipment and consumables./Telephony./Wired phones.html': 'https://www.oldi.ru/catalog/6602/',
    '/Office equipment and consumables./Telephony./Wireless phones.html': 'https://www.oldi.ru/catalog/7238/',
    '/Office equipment and consumables./OEC_Batteries, accumulators, chargers.html': 'https://www.oldi.ru/catalog/7719/',

    '/Photo- video cameras and accessories./Tripods.html': 'https://www.oldi.ru/catalog/7034/',
    '/Photo- video cameras and accessories./Batteries, accumulators, chargers.html': 'https://www.oldi.ru/catalog/7719/',
    '/Photo- video cameras and accessories./Action cameras.html': 'https://www.oldi.ru/catalog/9564/',
    '/Photo- video cameras and accessories./Accessories for Action cameras.html': 'https://www.oldi.ru/catalog/9726/',
    '/Photo- video cameras and accessories./Bags for Photo and Video Cameras.html': 'https://www.oldi.ru/catalog/7021/',

    '/Products for cars./Car refrigerators.html': 'https://www.oldi.ru/catalog/10844/',
    '/Products for cars./PdC_Accessories for mini-washes.html': 'https://www.oldi.ru/catalog/13390/',
    '/Products for cars./PdC_Car Vacuum cleaners.html': 'https://www.oldi.ru/catalog/10844/',
    '/Products for cars./PdC_Automotive compressors.html': 'https://www.oldi.ru/catalog/8144/',
    '/Products for cars./PdC_GPS navigators.html': 'https://www.oldi.ru/catalog/13018/',
    '/Products for cars./PdC_Inverters.html': 'https://www.oldi.ru/catalog/15755/',
    '/Products for cars./PdC_High pressure washers.html': 'https://www.oldi.ru/catalog/12873/',
    '/Products for cars./PdC_Video recorders.html': 'https://www.oldi.ru/catalog/7838/',
    '/Products for cars./Auto chemistry and Auto cosmetics.html': 'https://www.oldi.ru/catalog/10821/',
    '/Products for cars./PdC_Holders in the car.html': 'https://www.oldi.ru/catalog/8237/',
    '/Products for cars./PdC_Radar detectors.html': 'https://www.oldi.ru/catalog/8038/',
    '/Products for cars./PdC_Charging and charging devices.html': 'https://www.oldi.ru/catalog/7668/',
    '/Products for cars./PdC_Sound in the car./Sound_Car Sound Amplifiers.html': 'https://www.oldi.ru/catalog/10809/',
    '/Products for cars./PdC_Sound in the car./Sound_Acoustic cables.html': 'https://www.oldi.ru/catalog/13015/',
    '/Products for cars./PdC_Sound in the car./Sound_Component autoacoustics.html': 'https://www.oldi.ru/catalog/10819/',
    '/Products for cars./PdC_Sound in the car./Sound_Coaxial car acoustics.html': 'https://www.oldi.ru/catalog/10818/',
    '/Products for cars./PdC_Sound in the car./Sound_Car radios.html': 'https://www.oldi.ru/catalog/13013/',
    '/Products for cars./PdC_Sound in the car./Sound_Subwoofers.html': 'https://www.oldi.ru/catalog/15752/',

    '/Sale./Tableware.html': 'https://www.oldi.ru/catalog/15349/',
    '/Sale./Computers and laptops./CaL_Laptops.html': 'https://www.oldi.ru/catalog/15592/',
    '/Sale./Computers and laptops./CaL_Monoblocks.html': 'https://www.oldi.ru/catalog/15595/',
    '/Sale./Computers and laptops./CaL_Laptop Chargers.html': 'https://www.oldi.ru/catalog/15619/',
    '/Sale./Computers and laptops./CaL_Laptop bags and backpacks.html': 'https://www.oldi.ru/catalog/15593/',
    '/Sale./Computers and laptops./CaL_Laptop docking station.html': 'https://www.oldi.ru/catalog/15618/',
    '/Sale./Smartphones, tablets and gadgets./gadget_Accessories for tablets and smartphones.html': 'https://www.oldi.ru/catalog/15584/',
    '/Sale./Smartphones, tablets and gadgets./gadget_Graphic tablets.html': 'https://www.oldi.ru/catalog/15627/',
    '/Sale./Network equipment./NE_Wi-Fi routers and access points.html': 'https://www.oldi.ru/catalog/15615/',
    '/Sale./Network equipment./NE_Switches.html': 'https://www.oldi.ru/catalog/15630/',
    '/Sale./Network equipment./NE_VoIP Power Supplies.html': 'https://www.oldi.ru/catalog/15614/',
    '/Sale./Network equipment./NE_PoE Adapters.html': 'https://www.oldi.ru/catalog/15631/',
    '/Sale./Computer peripherals./CP_Keyboards.html': 'https://www.oldi.ru/catalog/15601/',
    '/Sale./Computer peripherals./CP_Webcams.html': 'https://www.oldi.ru/catalog/15597/',
    '/Sale./Computer peripherals./CP_Kits (keyboard + mouse).html': 'https://www.oldi.ru/catalog/15596/',
    '/Sale./Computer peripherals./CP_Projectors.html': 'https://www.oldi.ru/catalog/15638/',
    '/Sale./Computer peripherals./CP_Monitors.html': 'https://www.oldi.ru/catalog/15599/',
    '/Sale./Computer peripherals./CP_UPS.html': 'https://www.oldi.ru/catalog/15624/',
    '/Sale./Computer peripherals./CP_Batteries for Photo_Video equipment.html': 'https://www.oldi.ru/catalog/15623/',
    '/Sale./Computer peripherals./CP_Mouse pads.html': 'https://www.oldi.ru/catalog/15598/',
    '/Sale./Computer peripherals./CP_Headphones and headsets.html': 'https://www.oldi.ru/catalog/15639/',
    '/Sale./Computer peripherals./CP_Surge protectors and stabilizers.html': 'https://www.oldi.ru/catalog/15637/',
    '/Sale./Computer peripherals./CP_Columns.html': 'https://www.oldi.ru/catalog/15600/',
    '/Sale./Computer peripherals./CP_Mice.html': 'https://www.oldi.ru/catalog/15602/',
    '/Sale./Cables, cords, adapters, adapters./adapters_Patch cords.html': 'https://www.oldi.ru/catalog/15635/',
    '/Sale./Cables, cords, adapters, adapters./adapters_USB cables and adapters.html': 'https://www.oldi.ru/catalog/15620/',
    '/Sale./Cables, cords, adapters, adapters./adapters_Cables and loops.html': 'https://www.oldi.ru/catalog/15621/',
    '/Sale./Cables, cords, adapters, adapters./adapters_USB splitters.html': 'https://www.oldi.ru/catalog/15622/',
    '/Sale./Cables, cords, adapters, adapters./adapters_Cable in coils.html': 'https://www.oldi.ru/catalog/15636/',
    '/Sale./Cables, cords, adapters, adapters./adapters_Cable of HDMI_VGA_DP_DVI.html': 'https://www.oldi.ru/catalog/15634/',
    '/Sale./Appliances./appliances_Juicers.html': 'https://www.oldi.ru/catalog/15350/',
    '/Sale./Appliances./appliances_Meat grinders.html': 'https://www.oldi.ru/catalog/15632/',
    '/Sale./Televisions, video and audio equipment./Batteries, accumulators and chargers.html': 'https://www.oldi.ru/catalog/15626',
    '/Sale./Televisions, video and audio equipment./Brackets.html': 'https://www.oldi.ru/catalog/15640/',
    '/Sale./Televisions, video and audio equipment./Adapters and containers for TV.html': 'https://www.oldi.ru/catalog/15625/',
    '/Sale./PC Accessories./Sale_Enclosures.html': 'https://www.oldi.ru/catalog/15576/',
    '/Sale./PC Accessories./Sale_Power supplies.html': 'https://www.oldi.ru/catalog/15574/',
    '/Sale./PC Accessories./Sale_Motherboards.html': 'https://www.oldi.ru/catalog/15578/',
    '/Sale./PC Accessories./Sale_RAM.html': 'https://www.oldi.ru/catalog/15579/',
    '/Sale./PC Accessories./Sale_Coolers for processors.html': 'https://www.oldi.ru/catalog/15604/',
    '/Sale./PC Accessories./Sale_Controllers.html': 'https://www.oldi.ru/catalog/15628/',
    '/Sale./PC Accessories./Sale_Fans and coolers.html': 'https://www.oldi.ru/catalog/15603/',
    '/Sale./PC Accessories./Sale_SSD drives.html': 'https://www.oldi.ru/catalog/15577/',
    '/Sale./Tools and household goods./TaHG_Batteries for power tools.html': 'https://www.oldi.ru/catalog/15613/',
    '/Sale./Kitchen appliances.html': 'https://www.oldi.ru/catalog/15347/',

    '/Smart home PERENIO./Safety.html': 'https://www.oldi.ru/catalog/13647/',
    '/Smart home PERENIO./Management.html': 'https://www.oldi.ru/catalog/13645/',

    '/Smartphones, tablets and gadgets./Mobile phones.html': 'https://www.oldi.ru/catalog/13566/',
    '/Smartphones, tablets and gadgets./Smartphones.html': 'https://www.oldi.ru/catalog/6555/',
    '/Smartphones, tablets and gadgets./GPS navigators.html': 'https://www.oldi.ru/catalog/13018/',
    '/Smartphones, tablets and gadgets./Tablets.html': 'https://www.oldi.ru/catalog/7963/',
    '/Smartphones, tablets and gadgets./Video recorders.html': 'https://www.oldi.ru/catalog/7838/',
    '/Smartphones, tablets and gadgets./3D pens.html': 'https://www.oldi.ru/catalog/11230/',
    '/Smartphones, tablets and gadgets./Smart watches and fitness bracelets.html': 'https://www.oldi.ru/catalog/9264/',
    '/Smartphones, tablets and gadgets./E-books.html': 'https://www.oldi.ru/catalog/7651/',
    '/Smartphones, tablets and gadgets./Gyroscuters.html': 'https://www.oldi.ru/catalog/10793/',
    '/Smartphones, tablets and gadgets./Accessories for Apple products./Accessories for Apple iWatch.html': 'https://www.oldi.ru/catalog/15746/',
    '/Smartphones, tablets and gadgets./Accessories for Apple products./Chargers and power supplies.html': 'https://www.oldi.ru/catalog/7987/',
    '/Smartphones, tablets and gadgets./Accessories for Apple products./Apple Cables and Adapters.html': 'https://www.oldi.ru/catalog/7986/',
    '/Smartphones, tablets and gadgets./Accessories for Apple products./Adapters and adapters.html': 'https://www.oldi.ru/catalog/7985/',
    '/Smartphones, tablets and gadgets./Accessories for Apple products./Protective glasses and films for Apple.html': 'https://www.oldi.ru/catalog/8784/',
    '/Smartphones, tablets and gadgets./Accessories for Apple products./Bags and cases for Apple.html': 'https://www.oldi.ru/catalog/7994/',
    '/Smartphones, tablets and gadgets./Accessories for tablets and smartphones./Cases and bags for tablets.html': 'https://www.oldi.ru/catalog/13553/',
    '/Smartphones, tablets and gadgets./Accessories for tablets and smartphones./Input devices, docking stations,gloves for touch screens.html': 'https://www.oldi.ru/catalog/7885/',
    '/Smartphones, tablets and gadgets./Accessories for tablets and smartphones./Charging.html': 'https://www.oldi.ru/catalog/8235/',
    '/Smartphones, tablets and gadgets./Accessories for tablets and smartphones./Car charging for phones.html': 'https://www.oldi.ru/catalog/13524/',
    '/Smartphones, tablets and gadgets./Accessories for tablets and smartphones./Protective glasses and films.html': 'https://www.oldi.ru/catalog/8025/',
    '/Smartphones, tablets and gadgets./Accessories for tablets and smartphones./Selfie sticks.html': 'https://www.oldi.ru/catalog/9747/',
    '/Smartphones, tablets and gadgets./Accessories for tablets and smartphones./Cables, adapters and adapters.html': 'https://www.oldi.ru/catalog/8478/',
    '/Smartphones, tablets and gadgets./Accessories for tablets and smartphones./Portable speakers.html': 'https://www.oldi.ru/catalog/11603/',
    '/Smartphones, tablets and gadgets./Accessories for tablets and smartphones./Holders in the car.html': 'https://www.oldi.ru/catalog/8237/',
    '/Smartphones, tablets and gadgets./Accessories for tablets and smartphones./External batteries.html': 'https://www.oldi.ru/catalog/8579/',
    '/Smartphones, tablets and gadgets./Accessories for tablets and smartphones./Covers.html': 'https://www.oldi.ru/catalog/8236/',

    '/Televisions, video and audio equipment./Televisions.html': 'https://www.oldi.ru/catalog/6988/',
    '/Televisions, video and audio equipment./equpment_UPS, surge protectors and stabilizers.html': 'https://www.oldi.ru/catalog/6628/',
    '/Televisions, video and audio equipment./equpment_TV Accessories./TVa_Antennas.html': 'https://www.oldi.ru/catalog/7999/',
    '/Televisions, video and audio equipment./equpment_TV Accessories./TVa_Racks_Cabinets.html': 'https://www.oldi.ru/catalog/13114/',
    '/Televisions, video and audio equipment./equpment_TV Accessories./TVa_TV brackets.html': 'https://www.oldi.ru/catalog/8606/',
    '/Televisions, video and audio equipment./equpment_TV Accessories./TVa_Remote Controls.html': 'https://www.oldi.ru/catalog/7012/',
    '/Televisions, video and audio equipment./equpment_TV Accessories./TVa_Video cables.html': 'https://www.oldi.ru/catalog/8482/',
    '/Televisions, video and audio equipment./Game consoles and accessories./Game consoles.html': 'https://www.oldi.ru/catalog/7592/',
    '/Televisions, video and audio equipment./Audio equipment and accessories./accessories_MP3 players.html': 'https://www.oldi.ru/catalog/6519/',
    '/Televisions, video and audio equipment./Audio equipment and accessories./accessories_Audio cables.html': 'https://www.oldi.ru/catalog/8487/',
    '/Televisions, video and audio equipment./Audio equipment and accessories./accessories_Home theaters.html': 'https://www.oldi.ru/catalog/7652/',
    '/Televisions, video and audio equipment./Audio equipment and accessories./accessories_Headphones and headsets.html': 'https://www.oldi.ru/catalog/7228/',
    '/Televisions, video and audio equipment./Audio equipment and accessories./accessories_Car radios.html': 'https://www.oldi.ru/catalog/13013/',
    '/Televisions, video and audio equipment./Audio equipment and accessories./accessories_Radios and Walkie-talkies.html': 'https://www.oldi.ru/catalog/8310/',
    '/Televisions, video and audio equipment./Audio equipment and accessories./accessories_Receivers and amplifiers.html': 'https://www.oldi.ru/catalog/10849/',
    '/Televisions, video and audio equipment./Audio equipment and accessories./accessories_Music centers.html': 'https://www.oldi.ru/catalog/7663/',
    '/Televisions, video and audio equipment./Audio equipment and accessories./accessories_Microphones.html': 'https://www.oldi.ru/catalog/6782/',
    '/Televisions, video and audio equipment./Audio equipment and accessories./accessories_Acoustic cables.html': 'https://www.oldi.ru/catalog/13015/',
    '/Televisions, video and audio equipment./Audio equipment and accessories./accessories_Portable speakers.html': 'https://www.oldi.ru/catalog/11603/',
    '/Televisions, video and audio equipment./Audio equipment and accessories./accessories_Radio recorders.html': 'https://www.oldi.ru/catalog/7662/',
    '/Televisions, video and audio equipment./Video equipment./Video Players (DVD, Blu-Ray).html': 'https://www.oldi.ru/catalog/6538/',
    '/Televisions, video and audio equipment./Video equipment./Digital TV set-top boxes.html': 'https://www.oldi.ru/catalog/8500/',
    '/Televisions, video and audio equipment./Video equipment./Satellite TV Sets.html': 'https://www.oldi.ru/catalog/12764/',
    '/Televisions, video and audio equipment./Video equipment./Projectors and accessories.html': 'https://www.oldi.ru/catalog/7639/',
    '/Televisions, video and audio equipment./Video equipment./Media Players (Smart TV).html': 'https://www.oldi.ru/catalog/7795/',

    '/Tools and household goods./tools_Lanterns.html': 'https://www.oldi.ru/catalog/11185/',
    '/Tools and household goods./Tool Kits.html': 'https://www.oldi.ru/catalog/11186/',
    '/Tools and household goods./tools_Blowtorches.html': 'https://www.oldi.ru/catalog/11241/',
    '/Tools and household goods./tools_Ladders and ladders.html': 'https://www.oldi.ru/catalog/12759/',
    '/Tools and household goods./tools_Lamps.html': 'https://www.oldi.ru/catalog/13570/',
    '/Tools and household goods./tools_UPS, surge protectors and stabilizers.html': 'https://www.oldi.ru/catalog/6628/',
    '/Tools and household goods./Machines./Machines_Grinding machines.html': 'https://www.oldi.ru/catalog/13519/',
    '/Tools and household goods./Machines./Machines_Railmus machines.html': 'https://www.oldi.ru/catalog/13522/',
    '/Tools and household goods./Machines./Machines_Sawing machines.html': 'https://www.oldi.ru/catalog/13517/',
    '/Tools and household goods./Machines./Machines_Stone-cutting machines.html': 'https://www.oldi.ru/catalog/13518/',
    '/Tools and household goods./Machines./Machines_Drilling machines.html': 'https://www.oldi.ru/catalog/13523/',
    '/Tools and household goods./Smart Home./Smart Light.html': 'https://www.oldi.ru/catalog/10985/',
    '/Tools and household goods./Smart Home./Sensors and sockets.html': 'https://www.oldi.ru/catalog/10986/',
    '/Tools and household goods./Smart Home./Accessories (smart home).html': 'https://www.oldi.ru/catalog/11309/',
    '/Tools and household goods./Measuring instrument./Levels.html': 'https://www.oldi.ru/catalog/12312/',
    '/Tools and household goods./Measuring instrument./Measuring instruments.html': 'https://www.oldi.ru/catalog/12315/',
    '/Tools and household goods./Measuring instrument./Multimeter.html': 'https://www.oldi.ru/catalog/12302/',
    '/Tools and household goods./Measuring instrument./Goniometers and inclinometers.html': 'https://www.oldi.ru/catalog/12311/',
    '/Tools and household goods./Measuring instrument./Rangefinders.html': 'https://www.oldi.ru/catalog/12295/',
    '/Tools and household goods./Measuring instrument./Roulette.html': 'https://www.oldi.ru/catalog/12304/',
    '/Tools and household goods./Consumables for the tool./Boers.html': 'https://www.oldi.ru/catalog/9835/',
    '/Tools and household goods./Consumables for the tool./Saws and cloths.html': 'https://www.oldi.ru/catalog/9841/',
    '/Tools and household goods./Consumables for the tool./Glue Gun Rods.html': 'https://www.oldi.ru/catalog/13109/',
    '/Tools and household goods./Consumables for the tool./Accessories for power tools.html': 'https://www.oldi.ru/catalog/9834/',
    '/Tools and household goods./Consumables for the tool./Electrodes.html': 'https://www.oldi.ru/catalog/13106/',
    '/Tools and household goods./Consumables for the tool./Hardware and fasteners.html': 'https://www.oldi.ru/catalog/13554/',
    '/Tools and household goods./Consumables for the tool./Circles, discs, cutters.html': 'https://www.oldi.ru/catalog/9837/',
    '/Tools and household goods./Consumables for the tool./Batteries for power tools.html': 'https://www.oldi.ru/catalog/15732/',
    '/Tools and household goods./Consumables for the tool./Sanding bands and sheets.html': 'https://www.oldi.ru/catalog/9844/',
    '/Tools and household goods./Consumables for the tool./Milling cutters.html': 'https://www.oldi.ru/catalog/13105/',
    '/Tools and household goods./Consumables for the tool./Drills.html': 'https://www.oldi.ru/catalog/9842/',
    '/Tools and household goods./Consumables for the tool./Sets of bits and drills.html': 'https://www.oldi.ru/catalog/9838/',
    '/Tools and household goods./Consumables for the tool./Staples for construction stapler.html': 'https://www.oldi.ru/catalog/13103/',
    '/Tools and household goods./Construction equipment./Concrete Mixers.html': 'https://www.oldi.ru/catalog/15069/',
    '/Tools and household goods./Construction equipment./Jacks.html': 'https://www.oldi.ru/catalog/15494/',
    '/Tools and household goods./Construction equipment./Jackhammers.html': 'https://www.oldi.ru/catalog/15486/',
    '/Tools and household goods./Power electrical engineering./Generators.html': 'https://www.oldi.ru/catalog/9845/',
    '/Tools and household goods./Power electrical engineering./Welding machines.html': 'https://www.oldi.ru/catalog/9846/',
    '/Tools and household goods./tools_Electrics./Flaps, automation, counters.html': 'https://www.oldi.ru/catalog/10126/',
    '/Tools and household goods./tools_Electrics./Cable, cords, cable channels, corrugated pipes.html': 'https://www.oldi.ru/catalog/10098/',
    '/Tools and household goods./tools_Electrics./Sockets, switches, dimmers.html': 'https://www.oldi.ru/catalog/10105/',
    '/Tools and household goods./Pneumatic equipment./Accessories for pneumatic equipment.html': 'https://www.oldi.ru/catalog/13412/',
    '/Tools and household goods./Pneumatic equipment./Pistols.html': 'https://www.oldi.ru/catalog/13414/',
    '/Tools and household goods./Pneumatic equipment./Grinders.html': 'https://www.oldi.ru/catalog/13409/',
    '/Tools and household goods./Pneumatic equipment./Staplers.html': 'https://www.oldi.ru/catalog/13413/',
    '/Tools and household goods./Pneumatic equipment./Wrenches.html': 'https://www.oldi.ru/catalog/13410/',
    '/Tools and household goods./Pneumatic equipment./Spray gun.html': 'https://www.oldi.ru/catalog/13408/',
    '/Tools and household goods./Electro tool./Electric drills, punchers, electric jackhammers.html': 'https://www.oldi.ru/catalog/9870/',
    '/Tools and household goods./Electro tool./Screwdrivers, wrenches.html': 'https://www.oldi.ru/catalog/9862/',
    '/Tools and household goods./Electro tool./Compressors.html': 'https://www.oldi.ru/catalog/13415/',
    '/Tools and household goods./Electro tool./Grinding machines.html': 'https://www.oldi.ru/catalog/9855/',
    '/Tools and household goods./Electro tool./Electric planes.html': 'https://www.oldi.ru/catalog/9849/',
    '/Tools and household goods./Electro tool./Milling machines.html': 'https://www.oldi.ru/catalog/13569/',
    '/Tools and household goods./Electro tool./Technical hair dryers.html': 'https://www.oldi.ru/catalog/9851/',
    '/Tools and household goods./Electro tool./Staplers construction.html': 'https://www.oldi.ru/catalog/9850/',
    '/Tools and household goods./Electro tool./Industrial vacuum cleaners.html': 'https://www.oldi.ru/catalog/11184/',
    '/Tools and household goods./Electro tool./Thermal pistols.html': 'https://www.oldi.ru/catalog/13483/',
    '/Tools and household goods./Electro tool./Electric saws and electric jigsaws.html': 'https://www.oldi.ru/catalog/9870/',
    '/Tools and household goods./Hand tools./Piercing-cutting and sawing tools.html': 'https://www.oldi.ru/catalog/11243/',
    '/Tools and household goods./Hand tools./Percussion and lever tools.html': 'https://www.oldi.ru/catalog/11253/',
    '/Tools and household goods./Hand tools./Keys.html': 'https://www.oldi.ru/catalog/11246/',
    '/Tools and household goods./Hand tools./Consumables.html': 'https://www.oldi.ru/catalog/13625/',
    '/Tools and household goods./Hand tools./Screwdrivers.html': 'https://www.oldi.ru/catalog/15751/',
    '/Tools and household goods./Hand tools./Garden and Household inventory.html': 'https://www.oldi.ru/catalog/11244/',
    '/Tools and household goods./Hand tools./Plastering and painting tools.html': 'https://www.oldi.ru/catalog/11243/',
    '/Tools and household goods./Hand tools./Lip Tool.html': 'https://www.oldi.ru/catalog/11252/',
    '/Tools and household goods./Personal protective equipment./Safety glasses.html': 'https://www.oldi.ru/catalog/13480/',
    '/Tools and household goods./Personal protective equipment./Helmets.html': 'https://www.oldi.ru/catalog/13479/',
    '/Tools and household goods./Personal protective equipment./Gloves.html': 'https://www.oldi.ru/catalog/13482/',
    '/Tools and household goods./Personal protective equipment./Respirators, Self-rescuers.html': 'https://www.oldi.ru/catalog/13481/',

    '/Video surveillance systems./Camera brackets.html': 'https://www.oldi.ru/catalog/8921/',
    '/Video surveillance systems./Wireless video door phones.html': 'https://www.oldi.ru/catalog/8907/',
    '/Video surveillance systems./Power supplies for video surveillance.html': 'https://www.oldi.ru/catalog/8911/',
    '/Video surveillance systems./Video surveillance kits.html': 'https://www.oldi.ru/catalog/8919/',
    '/Video surveillance systems./Lenses for video cameras.html': 'https://www.oldi.ru/catalog/11335/',
    '/Video surveillance systems./Accessories for intercoms.html': 'https://www.oldi.ru/catalog/8934/',
    '/Video surveillance systems./DVRs and video recorders.html': 'https://www.oldi.ru/catalog/8915/',
    '/Video surveillance systems./Video door phones.html': 'https://www.oldi.ru/catalog/8912/',
    '/Video surveillance systems./IP cameras.html': 'https://www.oldi.ru/catalog/8909/',
    '/Video surveillance systems./Intercoms and video eyes.html': 'https://www.oldi.ru/catalog/8914/',
    '/Video surveillance systems./Microphones for video systems.html': 'https://www.oldi.ru/catalog/9438/',
    '/Video surveillance systems./Video cameras for indoor installation.html': 'https://www.oldi.ru/catalog/8925/',
    '/Video surveillance systems./Accessories for video surveillance systems.html': 'https://www.oldi.ru/catalog/11336/',
    '/Video surveillance systems./Wireless and wired sensors.html': 'https://www.oldi.ru/catalog/8907/',
    '/Video surveillance systems./Infrared spotlights.html': 'https://www.oldi.ru/catalog/8923/',

}


#####################
# Выполняемые функции
#####################

# Вывод информации о категориях
def printf(files):
    # print(files)
    count = 1
    for obj in files:
        print(f'{obj}')
        print(f'#{count}: {obj}')
        count += 1
    del files, count, obj

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
        del name, array

    def File(name):
        try:
            open(f"{name}.html", 'rt').close()
        except:
            open(f"{name}.html", 'wt').close()
        del name

    def WorkWithArray(array):
        for index in range(len(array)):
            if type(array[index]) == type('text') and type(array[index + 1]) != type(['mass']):
                File(array[index])
            try:
                if type(array[index + 1]) == type(['mass']): Directory(array[index], array[index + 1])
            except:
                os.chdir('..')
        del array

    if count == 1: WorkWithArray(productCatalog)

    del productCatalog, count

# Создание ссылок на все *.html файлы
def creatingLinks():
    LinksFile = []
    #os.chdir("products")
    path = os.getcwd()
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

    del files, path, obj
    return LinksFile

# Словарь для сопоставление адреса файлов и ссылок на каталоги
def LinksWithArray(dict, array):
    diction = {}
    for key in dict.keys():
        # print(key)
        for obj in array:
            # print(obj)#copy #CA_Motherboards.html
            if str(key) in str(obj):
                diction[obj] = dict[key]

    del dict, array, key, obj

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
    #if len(answer1) != len(answer2): print('!!!!!')

    text = f'#{len(answer1)} ***\n'
    for index in range(len(answer1)):
        answer1[index] = requestProducts(pattern1, answer1[index])[0]  # ID-товара
        if index < len(answer2):
            answer2[index] = requestProducts(pattern2, answer2[index])  # Name-товара
        else:
            answer2.append('no')
            #print(f'#{index + 1} => {answer1[index]} || {answer2[index]} (отсутствует наименование)\n')

        text += f'#{index + 1} => {answer1[index]} || {answer2[index]}\n'
    text += '###'

    del Page, pattern1, pattern2, pattern3, pattern4

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
    for index in range(2, lan + 1):
        driver.get(dictinary[Key] + f'?PAGEN_1={index}')
        pageSource += driver.page_source
        # Получение информации о продуктах
    products = request(pageSource)
    with open(Key, 'rt') as f: Pages = f.read()
    if not os.path.isfile(Key + '.txt'):
        print('Новая категория:', Key, '\n')
        with open(Key + '.txt', 'wt') as f:
            f.write(str(products[0]))
            f.flush()
            f.close()
        with open(Key, 'wt') as f:
            f.write(str(pageSource))
            f.flush()
            f.close()

    del dictinary, driver, Key, pattern, answer, text, Pages, f, lan, t,

    return pageSource, products

# Парсинг товаров
def requestProducts(pattern, text):
    answer = re.findall(pattern, text)
    del pattern, text
    return answer


# Считываем информацию из файлов                                                                     (Переделать!!!!!!!)
# Взять за основу програмный код, получающий информацию с сайта

######Старое######
'''
def reading(Key):
    with open(Key + '.txt', 'rt') as f:
        productsID = []
        productsName = []
        count = f.readline()
        text = f.readline()
        while text != '###':
            text = text.split(' =>  ')[1].split(' || ')
            productsID.append(text[0])
            productsName.append(text[1])
            text = f.readline()
    del text, Key, f
    return count, productsID, productsName
'''
######Новое#######
def reading(Key):
    with open(Key, 'rt') as f:
        PageSours = f.read()
        text, ProductsID, ProductsName = request(PageSours)
    del f, Key
    return text, ProductsID, ProductsName


# соотнесение товаров
########Старая#########
'''
def correlationOfGoods(count, productID, productName, Products, Key, Page):
    # answer = requestProducts(r'[0-9]{1,3}', count)
    productsID = []
    productsName = []
    Products = Products[0].split('***\n')[1].split(' =>  ')
    for index in range(len(Products) - 1):
        productsID.append(Products[index + 1].split(' || ')[0])
        productsName.append(Products[index + 1].split(' || ')[1])
    Products = productsID

    for obj in productID:
        if ' ' in obj:
            print(
                'productID!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!\n')
        if obj not in Products:
            text = f'Отсутствует => {obj} || {productName[productID.index(obj)]}'
            print(text); logi(str(f'{obj} || {productName[productID.index(obj)]}'), 'Отсутствует')

    for obj in Products:
        if ' ' in obj:
            print(
                'Products!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!\n!!!!!!!!!!!!!!!!!!!!!!!!!\n')
        if obj not in productID:
            product, a, b = request(Page)
            text = f'Новый товар => {obj}'
            print(text); logi([obj, b[Products.index(obj)]], 'Новый товар')
            with open(Key + '.txt', 'wt') as f: f.write(product)

    del count, productID, productName, Products, Key, Page
'''
########Новая#########

def correlationOfGoods(count, productID, productName, Products, Key, Page):
    # answer = requestProducts(r'[0-9]{1,3}', count)
    texts, ProductsIDforDef, ProductsNameForDef = request(Page)

    for obj in productID:
        if obj not in ProductsIDforDef:
            text = f'Отсутствует => {obj} || {productName[productID.index(obj)]} (в файле не было товара)'
            #print(text);
            logi(str(f'{obj} || {productName[productID.index(obj)]}'), 'Отсутствует')

    for obj in ProductsIDforDef:
        if obj not in productID:
            #product, a, b = request(Page)
            text = f'Новый товар => {obj}'
            #print(text)
            p = ProductsNameForDef[ProductsIDforDef.index(obj)][0]
            logi([obj, p[1:len(p)-42]], 'Новый товар')
            with open(Key + '.txt', 'wt') as f:
                f.write(texts)
                f.flush()
                f.close()
            with open(Key, 'wt') as f:
                f.write(Page)
                f.flush()
                f.close()

    del count, productID, productName, Products, Key, Page, texts, ProductsIDforDef, ProductsNameForDef
    #print('close')


def logi(obj, text):
    global Logi, LogiFile
    Time = time.strftime('%d %B %Y %A %X', time.localtime())
    if text == 'Начало работы':
        LogiFile.write(Logi)
        log = f'\n\n{Time} => Программа запущена\n\n'
    elif text == 'Отсутствует':
        log = f'\n    {Time} => Товар с ID был удален с сайта: {obj}'
    elif text == 'Новый товар':
        log = f'\n    {Time} => Новый товар появился на сайте: {obj[0]} || {obj[1]}'
    elif text == 'Проверяется':
        log = f'\n{Time} => Проверяется страница: {obj}'
    elif text == 'Error':
        log = f'\n{Time} => Непредвиденная ошибка!!!\n'
    else:
        log = f'\n{Time} => Программа проводит повторную проверку\n'

    Logi += log; LogiFile.write(log); LogiFile.flush();
    print(log)

    del obj, text, log, Time
    #return Logi

def work():
    # try:
    # Создаем папки для страниц сайта
    groupingFiles(productCatalog)

    # Создаем ссылки на категории товара
    Links = creatingLinks()

    # print(linksOnWeb_Sayte, Links)

    # Создадим сводный словарь ссылок
    dictinary = LinksWithArray(linksOnWeb_Sayte, Links)
    del Links
    for Key in dictinary.keys():
        # Получение кода страницы
        try:
            driver = webdriver.Safari()
        except: pass

        #driver.maximize_window()
        # driver = webdriver.Chrome(executable_path="/Users/olegkalasnikov/PycharmProjects/pythonProject/OLDIproject/Work/Exampls/Parser")
        logi(Key, "Проверяется")
        pages, Products = codePage(dictinary, driver, Key)

        # Начинаем сравнивать товары те, что есть и те, что спарсили
        count, productID, productName = reading(Key)  # Считываем информацию из документов

        # Соотнесение товаров
        correlationOfGoods(count, productID, productName, Products, Key, pages)
        gc.collect()

        driver.close()
        del pages, Products, count, productID, productName, driver
        del Key#######<-

# Обработчик ошибок
'''
    except Exception as exc:
        logi(exc, 'Error')
        global Logi
        with open('logi.txt', 'wt') as LogiFile: LogiFile.write(Logi)
        print(exc)
    finally:
        pass #driver.close()
'''


'''Уравляющий код'''
# Ведение логов
try:
    with open('logi.txt', 'rt') as LogiFile:
        Logi = LogiFile.read()
except: Logi = ''
LogiFile = open('logi.txt', 'wt')
logi(0, 'Начало работы')


# Автоповтор проверки

while True:
    work()
    Sleep = 2.5 * 60 * 60;
    logi(0, f'Повторная проверка с интервалом: {Sleep / 60 / 60} часов')
    os.chdir("..")
    time.sleep(Sleep)

