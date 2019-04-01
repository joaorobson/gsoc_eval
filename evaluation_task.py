from datetime import datetime
import pytz
import h5py
import csv

def nanoseconds_to_seconds(n_seconds):
    seconds = n_seconds/10**9
    return seconds

def convert_unix_time(unix_time):
    date = datetime.utcfromtimestamp(unix_time)
    return date

def get_utc_time(date):
    datetime_in_utc = date.astimezone(pytz.utc)
    return datetime_in_utc

def get_cern_time(date):
    datetime_in_cern = date.astimezone(pytz.timezone('Europe/Zurich'))
    return datetime_in_cern

def read_file(path):
    f = h5py.File(path, 'r')
    return f

def write_csv(data, path, keys):
    with open(path, 'w') as output:
        dict_writer = csv.DictWriter(output, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


nodes = []
def explore(name, node):
    row = {}
    if isinstance(node, h5py.Dataset):
        row['instance']= 'Dataset' 
        row['shape']= node.shape
        row['size'] = node.size
        row['name'] = node.name
        try:
            row['dtype']  = node.dtype
        except:
            row['dtype']  = 'error'
    elif isinstance(node, h5py.Group):
        row['instance']= 'Group' 
        row['shape']= '' 
        row['size'] = ''
        row['name'] = node.name
        row['dtype']  = ''
    nodes.append(row)

f = read_file('1541962108935000000_167_838.h5')
unix_time = f.filename[:19]
unix_time = int(unix_time)
unix_seconds = nanoseconds_to_seconds(unix_time)
date = convert_unix_time(unix_seconds)
print(get_utc_time(date))
print(get_cern_time(date))

f.visititems(explore)
keys = ['instance', 'shape', 'size', 'name', 'dtype']
write_csv(nodes, 'oi.csv', keys)
