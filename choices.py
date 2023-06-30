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
    ('RW', 'Recieved in China Warehouse'),
    ('DC', 'Departed China '),
    ('AT', 'Arrived in Tanzania'),
    ('RC', 'Recieved by Customer'),
)
CARGO_TYPE_CHOICES = (
    ('F', 'Full Cargo'),
    ('L', 'Loose Cargo'),
)

DELIVERY_STATUS = (
    ('WH','In TZ Warehouse'),
    ('VH','Loaded in Vehicle'),
    ('RC','Received by Customer'),
)

QUOTE_STATUS = (
    ('S', 'Submitted'),
    ('R', 'Reviewing'),
    ('Q', 'Quoted'),
)