import h5py
import csv

class HDF5:
    def __init__(self, filepath):
        self.nodes = []
        self.filepath = filepath

    def read_file(self):
        f = h5py.File(self.filepath, 'r')
        return f

    def explore(self, name, node):
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

        self.nodes.append(row) if row else None

    def get_dataset_value(self, dataset_path, hdf5_file):
        return hdf5_file[dataset_path][()]

    def write_csv(self, csvpath):
        keys = ['instance', 'shape', 'size', 'name', 'dtype']
        with open(csvpath, 'w') as output:
            dict_writer = csv.DictWriter(output, keys)
            dict_writer.writeheader()
            dict_writer.writerows(self.nodes)
