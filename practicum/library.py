import csv
import pickle
import os

def load_table(filename):
    _, ext = os.path.splitext(filename)
    if ext == '.csv':
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            table = list(reader)
            attributes = {'delimiter': ','}
    elif ext == '.pkl':
        with open(filename, 'rb') as f:
            table = pickle.load(f)
            attributes = {'format': 'pickle'}
    else:
        raise ValueError('Unsupported file format.')

    return {'attributes': attributes, 'data': table}

def save_table(table, filename):
    _, ext = os.path.splitext(filename)
    if ext == '.csv':
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(table['data'])
    elif ext == '.pkl':
        with open(filename, 'wb') as f:
            pickle.dump(table['data'], f)
    elif ext == '.txt':
        with open(filename, 'w') as f:
            for row in table['data']:
                f.write(' '.join(map(str, row)))
                f.write('\n')
    else:
        raise ValueError('Unsupported file format.')
    
def get_rows_by_number(table, start, stop=None, copy_table=False):
    if stop is None:
        stop = start + 1
    if copy_table:
        data = table['data'][:]
    else:
        data = table['data']
    return {'attributes': table['attributes'], 'data': data[start:stop]}

def get_rows_by_index(table, *values, copy_table=False):
    indices = [i for i, row in enumerate(table['data']) if row[0] in values]
    if copy_table:
        data = table['data'][:]
    else:
        data = table['data']
    return {'attributes': table['attributes'], 'data': [data[i] for i in indices]}

def get_column_types(table, by_number=True):
    column_types = {}
    for i, column in enumerate(table['data'][0]):
        column_types[i if by_number else column] = type(column).__name__
    return column_types

def set_column_types(table, types_dict, by_number=True):
    column_types = get_column_types(table, by_number=by_number)
    for column, value_type in types_dict.items():
        if column not in column_types:
            raise ValueError('Invalid column.')
        if column_types[column] != value_type:
            for i, row in enumerate(table['data']):
                row[column if by_number else row.index(column)] = value_type(row[column if by_number else row.index(column)])

def get_values(table, column=0):
    values = [row[column] for row in table['data']]
    return values

def get_value(table, column=0):
    if len(table['data']) != 1:
        raise ValueError('The table should contain only one row.')
    return table['data'][0][column]

def set_values(table, values, column=0):
    if len(values) != len(table['data']):
        raise ValueError('The length of the values list should be equal to the number of rows in the table.')
    for i, row in enumerate(table['data']):
        row[column] = values[i]

def set_value(table, column=0):
    if len(table['data']) != 1:
        raise ValueError('The table should contain only one row.')
    value = input('Enter a value: ')
    table['data'][0][column] = value

def print_table(table):
    for row in table['data']:
        print(' '.join(map(str, row)))

def check_file_format(filename):
    _, ext = os.path.splitext(filename)
    if ext not in ['.csv', '.pkl', '.txt']:
        raise ValueError('Unsupported file format.')

def check_column(table, column, by_number=True):
    if by_number:
        if column not in range(len(table['data'][0])):
            raise ValueError('Invalid column number.')
    else:
        if column not in table['data'][0]:
            raise ValueError('Invalid column name.')

def check_table_length(table, expected_length):
    if len(table['data']) != expected_length:
        raise ValueError('Invalid table length.')