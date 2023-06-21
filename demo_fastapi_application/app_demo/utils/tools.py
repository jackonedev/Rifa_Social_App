# Create a test for a string that should be a date but can have verbose month names
#
# Path: app_demo\tests\test_clientes.py
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'es_ES')


def de_definition(obj:str) -> str:
    lista = obj.split(' ')
    while 'de' in lista:
        lista.remove('de')
    return ' '.join(lista)

    

def define_date_w_year(obj:str) -> str:
    """Check de input format and return it in a standard format"""
    obj = de_definition(obj)

    try:
        datetime.strptime(obj, '%d/%m/%Y')
        return obj
    except ValueError:
        try:
            datetime.strptime(obj, '%d %B %Y')
            return datetime.strptime(obj, '%d %B %Y').strftime('%d/%m/%Y')
        except ValueError:
            return None
        
def define_date(obj:str) -> str:
    """Check de input format and return it in a standard format"""
    obj = de_definition(obj)

    try:
        datetime.strptime(obj, '%d/%m')
        return obj
    except ValueError:
        try:
            datetime.strptime(obj, '%d %B')
            return datetime.strptime(obj, '%d %B').strftime('%d/%m')
        except ValueError:
            return None
