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


