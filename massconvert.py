import os
from importing import preprocessed_mat
from avalanchetoolbox import preprocessing as preproc

path = '/data/alstottj/NIMH/Original/rest'
output_path = '/data/alstottj/NIMH/Data/'
group_name = 'NIMH'
species = 'human'
location = 'NIMH'
sensor = 'axial'

dirList=os.listdir(path)

#bands = ('delta', 'theta', 'alpha', 'beta', 'raw', 'gamma', 'high-gamma', 'broad')
bands = ('raw',)
window='hamming'
#taps=25
taps = 512
#downsample=100.0
downsample=False
sampling_rate = 600.0


for dirname in dirList:
    if not dirname.endswith('-f.ds'):
        continue
    print dirname
    data = preprocessed_mat(dirname+'/', sensor)

    components = dirname.split('_')
    name = components[0]
    number = components[0]
    output_file = output_path+name

    date = components[2]
    task = components[1]

    preproc.write_to_HDF5(data,output_file, task, sampling_rate=sampling_rate, bands=bands,\
            window=window, taps=taps,\
            downsample=downsample,
            group_name=group_name, species=species, location=location,\
                    number_in_group=number, name=name, date=date)
