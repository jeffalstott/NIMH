def preprocessed_mat(directory, sensor):
    from scipy.io import loadmat
    directory = '/data/alstottj/NIMH/Original/rest/'+directory
    if sensor=='planar':
        matfile = loadmat(directory+'MEG_planar_preproc_norm2.mat')
    elif sensor=='planar_combined':
        matfile = loadmat(directory+'MEG_planar_preproc_norm.mat')
    else: #axial
        matfile = loadmat(directory+'MEG_'+sensor+'_preproc_norm.mat')
    data = matfile['y_dev']*matfile['y_std']+matfile['y_m']
    return data
