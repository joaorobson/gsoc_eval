import scipy.signal
import matplotlib.pyplot as plt
from hdf5 import HDF5
from time_conversion import TimeConversion
import sys

def get_local_times(hdf5_file):
    unix_time = int(hdf5_file.filename[:19])
    converted_date = TimeConversion(unix_time)
    print("Converted times")
    print("UTC Time: ", converted_date.utc_time)
    print("CERN Time: ", converted_date.cern_time)

def get_image(hdf5):
    image_data = hdf5.get_dataset_value('/AwakeEventData/XMPP-STREAK/StreakImage/streakImageData', f)
    image_height = hdf5.get_dataset_value('/AwakeEventData/XMPP-STREAK/StreakImage/streakImageHeight', f)
    image_width = hdf5.get_dataset_value('/AwakeEventData/XMPP-STREAK/StreakImage/streakImageWidth', f)
    image_matrix = image_data.reshape(image_height[0], image_width[0])
    image = scipy.signal.medfilt(image_matrix)
    plt.imshow(image)
    plt.savefig('image.png')
    plt.show()

if __name__ == "__main__":
    hdf5 = HDF5(sys.argv[1])
    f = hdf5.read_file()

    get_local_times(f)

    f.visititems(hdf5.explore)
    get_image(hdf5)
    hdf5.write_csv('hdf5.csv')
