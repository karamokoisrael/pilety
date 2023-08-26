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