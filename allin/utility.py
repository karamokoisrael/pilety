import openpyxl



def generate_fullco_excel_file(products, container):
    # Check if "container" is present in kwargs
    # container = kwargs.get("container", None)

    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["YIWU PILETY IMPORT AND EXPORT COMPANY LIMITED"])
    sheet.append(["ADD: Room 301 Building 20, District 4, Futian, Yiwu City, Jinhua City, Zhejiang Province"])
    sheet.append(["Email: pilety@pilety.com"])



    # Add four blank rows at the beginning
    
    sheet.append([])
    sheet.append([])

    # Write the headers for the Product model fields
    headers = ["recieved date", "name",
               "chinese", "ctn", "mark",
               "packaging", "units", "unit price", 
               "ttprice", "cbm/ctn", "ttcbm", "weght", 
               "TTweight", 
               "item_number"]
    
    headers = [item.upper() for item in headers]
    
    sheet.append(headers)

    # Write product data
    for product in products:
        sheet.append(product)

    sheet.append([])
    sheet.append([])
    
    sheet.append(['Container Number', container.number, 
                  'Total CBM', container.cbms, 
                  'Total ctns', container.ctns,
                  'Total weight', container.weight])

    return wb





def generate_looseco_excel_file(products, container):
    # Check if "container" is present in kwargs
    # container = kwargs.get("container", None)

    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["YIWU PILETY IMPORT AND EXPORT COMPANY LIMITED"])
    sheet.append(["ADD: Room 301 Building 20, District 4, Futian, Yiwu City, Jinhua City, Zhejiang Province"])
    sheet.append(["Email: pilety@pilety.com"])



    # Add four blank rows at the beginning
    
    sheet.append([])
    sheet.append([])

    # Write the headers for the Product model fields
    headers = ["recieved date", "name",
               "chinese", "ctn", "mark",
               "packaging", "units", "unit price", 
               "ttprice", "cbm/ctn", "ttcbm", "weght", 
               "TTweight", 
               "item_number", "contact"]
    
    headers = [item.upper() for item in headers]
    
    sheet.append(headers)

    # Write product data
    for product in products:
        sheet.append(product)

    sheet.append([])
    sheet.append([])
    
    sheet.append(['Container Number', container.number, 
                  'Total CBM', container.cbms, 
                  'Total ctns', container.ctns,
                  'Total weight', container.weight])

    return wb





def populatedata():
    #create a loose container
    #loop create loose ccargos which create other product
    loosecontainer = LooseContainer(name='Loose Cargo of june 26th', number='TEMU8836590')
    loosecontainer.save()
    for item in data:
        loose_cargo = LooseCargo(
                mark=item[0]['ITEM MARK'],
                container=loosecontainer
            )
        loose_cargo.save()
        for product_item in item:
            product=Product(
                    name=product_item.get('ITEM NAME'),
                    chinese=product_item.get('CHINESE DESCRIPTION'),
                    qty=product_item.get('CTN'),
                    packaging=product_item.get('PACKAGING'),
                    units=product_item.get('UNIT'),
                    price=product_item.get('UNIT PRICE'),
                    ttprice=product_item.get('TOTAL PRICE'),
                    cbm=product_item.get('CBM PER CTN'),
                    wght=product_item.get('WEIGHT(KG)'),
                    weight=product_item.get('TT.WEIGHT(KG)'),
                    l_cargo=loose_cargo
                )
            product.save()
        loose_cargo.save()
    loosecontainer.save()