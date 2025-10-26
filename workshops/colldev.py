import csv
import tablib
import requests
import time
import sys

CUNY = 'cun01'

# schools = [{'value':'BARUCH', 'label':'Baruch College'}, {'value':'BOROUGH', 'label':'BMCC'}, {'value':'BRONX', 'label':'Bronx CC'},
#         {'value':'BROOKLYN', 'label':'Brooklyn College'}, {'value':'CENTRO', 'label':'Centro at Hunter'},
#         {'value':'CITY', 'label':'City College and DSI'}, {'value':'STATENISLAND', 'label':'College of Staten Island'},
#         {'value':'GRADCENTER', 'label':'Graduate Center'}, {'value':'JOURNALISM', 'label':'Graduate School of Journalism'},
#         {'value':'HOSTOS', 'label':'Hostos CC'}, {'value':'HUNTER', 'label':'Hunter College'}, {'value':'JOHNJAY', 'label':'John Jay College'},
#         {'value':'KINGSBOROUGH', 'label':'Kingsborough CC'}, {'value':'LAGUARDIA', 'label':'LaGuardia CC'}, {'value':'LAW', 'label':'Law School'},
#         {'value':'LEHMAN', 'label':'Lehman College'}, {'value':'MEDGAR', 'label':'Medgar Evers College'}, {'value':'NYCITY', 'label':'NYCCT'},
#         {'value':'QUEENS', 'label':'Queens College'}, {'value':'QUEENSBOROUGH', 'label':'Queensborough CC'}, {'value':'YORK', 'label':'York College'}]


def lookup_ISBN(ISBN, school, count=0):
    # payload = {'query': ISBN, 'queryType': 'ISBN', 'school': school}
    the_url = 'http://lookup.cunylibraries.org/' + school + '/isbn/' + ISBN + '?format=json'
    try:
        r = requests.get(the_url)
        JSON_record = r.json()
        count = 0
        return JSON_record
    except Exception, e:
        print e
        if count >= 30:
            raise e
        count += 1
        time.sleep(6)
        lookup_ISBN(ISBN, school, count)


def lookup_worldcat(ISBN, count=0):
    a_url = 'http://xisbn.worldcat.org/webservices/xid/isbn/' + ISBN
    payload = {'method': 'getEditions', 'format': 'json', 'fl': 'ed'}
    try:
        t = requests.get(a_url, params=payload)
        record = t.json()
        worldcat_count = 0
        return record
    except Exception, e:
        if worldcat_count >= 10:
            raise e
        count += 1
        lookup_worldcat(ISBN, count)


def csv_import(which):
    try:
        csvReader = csv.reader(open(which, 'rU'), delimiter=',')
    except Exception, e:
        raise e
    headline = []
    for row in csvReader:
        header = str(row).rsplit(',')
        for word in header:
            newstr = word.replace("[", "")
            newstr = newstr.replace("]", "")
            newstr = newstr.replace("\\", "")
            newstr = newstr.replace("'", "")
            newstr = newstr.strip()
            headline.append(newstr)
        break
    data = tablib.Dataset()
    data.headers = headline
    for row in csvReader:
        if len(row) != len(data.headers):
            difference = len(data.headers) - len(row)
            a = 0
            while a < difference:
                row.append('None')
                a += 1
        data.append(row)

    ISBN_column = 'None'
    title_column = 'None'
    category_column = 'None'
    specialty_column = 'None'
    price_column = 'None'

    for index, column in enumerate(data.headers):
        if column == 'ISBN' or column == 'ISBN10':
            ISBN_column = index
        if column == 'title' or column == 'Title':
            title_column = index
        if column == 'Category' or column == 'category':
            category_column = index
        if column == 'Specialty' or column == 'specialty':
            specialty_column = index
        if column == 'ListPrice' or column == 'Price' or column == 'price':
            price_column = index
        print index, column

    searched_items_list = []

    for row in data:
        if isinstance(ISBN_column, int):
            the_ISBN = row[ISBN_column]
        else:
            the_ISBN = None
        if isinstance(title_column, int):
            the_title = row[title_column]
        else:
            the_title = None
        if isinstance(category_column, int):
            the_category = row[category_column]
        else:
            the_category = None
        if isinstance(specialty_column, int):
            the_specialty = row[specialty_column]
        else:
            the_specialty = None
        if isinstance(price_column, int):
            the_price = row[price_column]
        else:
            the_price = None

        JSON_record = lookup_ISBN(the_ISBN, CUNY)
        try:
            if JSON_record:
                item = {'title': JSON_record[0]['title'], 'given_title': the_title, 'ISBN': the_ISBN, 'schools': [], 'other_editions': '',
                        'specialty': the_specialty, 'category': the_category, 'price': the_price}
                for piece in JSON_record:
                    campus = piece['campus']
                    item['schools'].append(campus)
            else:
                item = {'title': 'Not Owned in CUNY', 'given_title': the_title, 'ISBN': the_ISBN, 'schools': '', 'other_editions': '',
                        'specialty': the_specialty, 'category': the_category, 'price': the_price}
        except TypeError:
            item = {'title': 'lookup failed', 'given_title': the_title, 'ISBN': the_ISBN, 'schools': '', 'other_editions': '',
                    'specialty': the_specialty, 'category': the_category, 'price': the_price}
        searched_items_list.append(item)
        print item

        # looking for alternate isbns
        if item['title'] == 'Not Owned in CUNY':
            other_ISBNs = lookup_worldcat(item['ISBN'])
            if 'list' in other_ISBNs:
                item['other_editions'] = []
                for book in other_ISBNs['list']:
                    other_ISBN = book['isbn'][0]
                    if 'ed' in book:
                        other_ed = book['ed']
                    else:
                        other_ed = book['isbn']
                    try:
                        other_edition_lookup = lookup_ISBN(other_ISBN, CUNY)
                        for piece in other_edition_lookup:
                            campus = piece['campus']
                            item['other_editions'].append(campus + ': ' + other_ed)
                    except TypeError:
                        item['other_editions'].append('lookup failed')
        item['schools'] = ', '.join(item['schools'])
        item['other_editions'] = '||'.join(item['other_editions'])

    final_data = tablib.Dataset()
    final_data.headers = ('Given Title', 'Catalog Title', 'ISBN', 'Category', 'Specialty', 'Schools With This Edition', 'Schools With Other Editions', 'Price')
    for book in searched_items_list:
        final_data.append((book['given_title'], book['title'], book['ISBN'], book['category'], book['specialty'], book['schools'], book['other_editions'], book['price']))
    with open('output.csv', 'wb') as f:
            f.write(final_data.csv)
            f.seek(0)

csv_import(sys.argv[1])
