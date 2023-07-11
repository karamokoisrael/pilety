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
    ('HW1', 'Hardware - 1'), #420
    ('HW2', 'HARDWARE (wire mash, heavy hardware items)'), #450
    ('MAB', 'MABATI'),#500 
    ('COS', 'COSMETICS/PERFUME/TOOTHPASTE'),#400
    ('CL', 'CLOTHES'),#420
    ('ST', 'STATIONARY'),#400
    ('GE', 'GYM EQUIPMENTS'),#400 
    ('MC', 'MACHINES'),#500 
    ('CA', 'CAR SPARE PARTS'),#500 
    ('MS', 'MOTORCYCLE SPARE PARTS'),#450
    ('TO', 'TOYS'),#380 
    ('SH', 'SHOES'),#450 
    ('CU', 'CURTAINS'),#450
    ('CF', 'CARPETS/ FLOOR MAT'),#450
    ('OR', 'ORNAMENTS'),#400 
    ('DC', 'DECORATIONS'),#400
    ('SU', 'SUNGLASSES'),#380 
    ('PA', 'PHONE ACCESSORIES'),#400
    ('TV', 'TV’S'),#450 
    ('EL', 'ELECTRONICS'), #450
    ('FU', 'FURNITURE'),#420 
    ('HO', 'HOSPITAL EQUIPMENTS I.E WHEEL CHAIRS'),#500 
    ('OT', 'Other'),#500 
    
)