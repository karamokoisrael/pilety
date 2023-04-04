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
    ('SERVICE', 'SERVICE'),
    ('PRODUCT', 'PRODUCT'),
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


