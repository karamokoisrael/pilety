#Shipment model in finance
LOAD_TYPE_CHOICES = (
    ('TL', 'TL'),
    ('LTL', 'LTL'),
)

CURRENCY_CHOICES = (
    ('USD', 'USD'),
    ('RMB', 'RMB'),
)

ORDERS_STATUS_CHOICES = (
    ('PENDING', 'PENDING'),
    ('ACTIVE', 'ACTIVE'),
)

PRODUCTS_TYPE_CHOICES = (
    ('S', 'SERVICE'),
    ('P', 'PRODUCT'),
)

# Drivers model from users 
PAY_TYPE_CHOICES = (
    ('PERCENT', 'PERCENT'),
    ('PER MILE', 'PER MILE'),
    ('OTHER', 'OTHER'),
) 

DRIVER_STATUS_CHOICES = (
    ('ACTIVE', 'ACTIVE'),
    ('TERMINATED', 'TERMINATED'),
    ('TEMPORARY', 'TEMPORARY'),

)

UNIT_PACKAGING_CHOICES = (
    ('PCS', 'Pieces'),
    ('RLS', 'Rolls'),
    ('DZN', 'Dozens'),
    ('BGS', 'Bags'),
    ('SET', 'Set'),
)

CONTAINER_STATUS_CHOICES = (
    ('NF', 'Not Full'),
    ('FC', 'Full CBM'),
    ('OW', 'Over weight'),
    ('NC', 'Needs Confirming'),
)

EXPENSES_RECURRANCE_CHOICES = (
    ('N', 'Not Recurring'),
    ('D', 'Daily'),
    ('W', 'Weekly'),
    ('M', 'Monthly'),
    ('Q', 'Quaterly'),
    ('S', 'Semi Annual'),
    ('A', 'Annual'),
    
)

CARGO_STATUS_CHOICES = (
    ('RW', 'China Warehouse'),
    ('DC', 'Shipped '),
    ('AT', 'In Tanzania'),
    ('DV', ' Delivering'),
    ('RC', 'Recieved'),
)
CARGO_TYPE_CHOICES = (
    ('F', 'Full Cont. Cargo'),
    ('L', 'Loose Cont. Cargo'),
)

DELIVERY_STATUS = (
    ('WH','In Warehouse'),
    ('VH','Delivering'),
    ('RC','Received'),
)

QUOTE_STATUS = (
    ('S', 'Submitted'),
    ('R', 'Reviewing'),
    ('Q', 'Quoted'),
)

CATEGORY_CHOICES = (
    ('TOYS', 'TOYS'),#380 
    ('SUNGLASSES', 'SUNGLASSES'),#380 

    ('COSMETICS/PERFUME/TOOTHPASTE', 'COSMETICS/PERFUME/TOOTHPASTE'),#400
    ('STATIONARY', 'STATIONARY'),#400
    ('GYM EQUIPMENTS', 'GYM EQUIPMENTS'),#400 
    ('ORNAMENTS', 'ORNAMENTS'),#400 
    ('DECORATIONS', 'DECORATIONS'),#400
    ('PHONE ACCESSORIES', 'PHONE ACCESSORIES'),#400

    ('Hardware - 1', 'Hardware - 1'), #420
    ('CLOTHES', 'CLOTHES'),#420
    ('FURNITURE', 'FURNITURE'),#420 
    
    ('MOTORCYCLE SPAREPARTS', 'MOTORCYCLE SPARE PARTS'),#450
    ('SHOES', 'SHOES'),#450 
    ('CURTAINS', 'CURTAINS'),#450
    ('CARPETS/ FLOOR MAT', 'CARPETS/ FLOOR MAT'),#450
    ('TV', 'TV’S'),#450 
    ('ELECTRONICS', 'ELECTRONICS'), #450

    ('HARDWARE (wire mash, heavy hardware items)', 'HARDWARE (wire mash, heavy hardware items)'), #450
    ('MABATI', 'MABATI'),#500 
    ('MACHINES', 'MACHINES'),#500 
    ('CAR SPAREPARTS', 'CAR SPARE PARTS'),#500 
    ('HOSPITAL', 'HOSPITAL EQUIPMENTS I.E WHEEL CHAIRS'),#500 
    ('Other', 'Other'),#500 
    
)

CATEGORIES = (
    ('Kids Toys','Kids Toys'),#380
    ('Sunglasses','Sunglasses'),#380

    ('Scales','Scales'),#400
    ('Cosmetics','Cosmetics'),#400
    ('Stationeries','Stationeries'),#400
    ('Hardware','Hardware(Kawaida)'),#400
    ('Utensils','Utensils(Vyombo)'),#400
    ('Home Decorations','Home Decorations'),#400
    ('Tooth Paste & Brush','ToothPaste & Brush'),#400
    ('Gym Equipments','Gym Equipments'),#400
    ('Ornaments','Ornaments(urembo e.g hereni,pete etc)'),#400
    ('Phone accessories','Phone accessories'),#400
    ('Big toys','Big toys'),#400
    ('Kids Equipments','Kids Equipments(beds,swings)'),#400

    ('Boxers/Men Underwear','Boxers/Men Underwear'), #420
    ('Shoes','Shoes'),#420
    ('Socks','Socks'),#420
    ('Baby Clothes','Baby Clothes'),#420
    ('Furnitures','Furnitures'),#420

    ('Nails Paint/Polish','Nails Paint/Polish(Rangi za kucha)'),#450
    ('Heavy Hardware','Heavy Hardware(nzito)'),#420
    ('Perfume/Spray','Perfume/Spray'),#450
    ('Heavy Furnitures','Heavy Furnitures'),#450

    ('Spareparts','Spareparts'),#500
    ('Pallets','Pallets'),#500
    ('Hospital Equipments','Hospital Equipments'),#500
    ('Iron Sheets','Iron Sheets(Mabati)'),#500
    ('Heavy Bales','Heavy Bales(belo kubwa/zito)'),#500
    # ('',''),#
    # ('',''),#

    
)

cost_380 = ['Kids Toys',#380
'Sunglasses'#380
]

cost_400 = ['Scales',#400
'Cosmetics',#400
'Stationeries',#400
'Hardware',#400
'Utensils',#400
'Home Decorations',#400
'Tooth Paste & Brush',#400
'Gym Equipments',#400
'Ornaments)',#400
'Phone accessories',#400
'Big toys',#400
'Kids Equipments',#400
]
cost_420 = [
    'Boxers/Men Underwear', #420
    'Shoes',#420
    'Socks',#420
    'Baby Clothes',#420
    'Furnitures',#420
    'Heavy Hardware'
    ]

cost_450 = [
    'Nails Paint/Polish',#450
    'Perfume/Spray',#450
    'Heavy Furnitures',#450
    ]
cost_500 = [
    'Spareparts',#500
    'Pallets',#500
    'Hospital Equipments',#500
    'Iron Sheets',#500
    'Heavy Bales',#500
]    