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
    ('HW', 'Hardware - 1'), #380
    ('HW', 'Hardware (wire mash, heavy hardware items)'), #380
    ('EL', 'Electronics'), #370
    ('TY', 'Toys'),#360
    ('CO', 'Cosmetics'),#380
    ('CL', 'Clothes'),#400
    ('ST', 'Stationery'),#360
    ('PA', 'Phone Accessories'),#360
    ('CC', 'Carpets and Curtains'),#400
    ('DC', 'Decor'),#370
    ('MS', 'Motorcycle spare parts'),#360
    ('OT', ''),#400 
    ('OT', 'Other'),#400 
    ('OT', 'Other'),#400 
    ('OT', 'Other'),#400 
    ('OT', 'Other'),#400 
    ('OT', 'Other'),#400 
    ('OT', 'Other'),#400 
    ('OT', 'Other'),#400 
    ('OT', 'Other'),#400 
    ('OT', 'Other'),#400 
    ('OT', 'Other'),#400 
)