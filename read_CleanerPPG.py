import numpy as np
import pandas as pd
import os
# --------------------- #
deb_log = False
if deb_log:
    import matplotlib.pyplot as plt
# --------------------- #

    
def readCSV(_path,header=0):
    f = pd.read_csv(
        _path,header=header
    )
    return f

def plotXY(X,Y,peaks,label=''):
    plt.figure()
    plt.plot(X,Y,label=label)
    peakX = np.where(peaks==1 ,X,np.nan)
    peakY = np.where(peaks==1 ,Y,np.nan)
    peakX = peakX[~np.isnan(peakX)]
    peakY = peakY[~np.isnan(peakY)]
    # peakX = np.unique(peakX)
    plt.scatter(peakX,peakY,
                marker='o', # marker類型
                s=48*1, # marker的大小
                color='green',
                label='peaks' # 名字
                )
    plt.show()
    
def p2p(sigs):
    length_sigs = len(sigs)
    i = 1
    avg_time = np.nan
    times = []
    if length_sigs > i:
        while i < length_sigs:
            times.append(sigs[i]-sigs[i-1])
            i += 1
        avg_time = np.array(times,dtype=np.float64)
        avg_time = np.mean(avg_time)         
            
    return avg_time

def ms2bpm(sigs,timescale): 
    output = 60 * timescale/np.array(sigs,dtype=np.float64) # 1min = 60sec
    return output

def genHR(
        times, # millisecond
        peaks,
        sw_size=8 #second
        ):
    timescale = 1000.0 # second to millisecond
    times = np.where(peaks==1 ,times,np.nan)
    peaktimes = times[~np.isnan(times)]
    if deb_log:
        print('[genHR] times =',peaktimes)
    gt = []
    secs = range(1,61,1)
    for sec in secs:
        t = sec*timescale
        _peakstime =  peaktimes[peaktimes<=t]
        _peakstime = _peakstime[_peakstime>=t-(sw_size*timescale)]
        if deb_log:
            print(_peakstime)
        hr = p2p(_peakstime)
        gt.append(hr)
    
    gt = ms2bpm(gt,timescale)
    if deb_log:
        print('[genHR] len(gt),gt =',len(gt),gt)
    
    para = {
        'timescale':timescale,
        'secs':secs,
        'sw_size':sw_size
    }
    return secs,gt,para


def showData(_path):
    cleaner_path = f'{_path}/Cleaned'
    raw_path = f'{_path}/Raw'
    datasetname = _path.split('/')[-1]
    if datasetname == 'ECG-Fitness':
        output_path = f'Z:/CleanerPPG/{datasetname}/Henry_GT/'
        log_path = f'{output_path}/log'
        gt_path = f'{output_path}/groundtruth'
        # cmras = [1,2]
        acts  = range(1,7,1)
        subs  = range(0,17,1)
        cmras = [1]
        # acts  = [2]
        # subs  = [0]
        # os.makedirs(output_path, exist_ok=True)
        os.makedirs(log_path, exist_ok=True)
        os.makedirs(gt_path, exist_ok=True)
        for cmra in cmras:
            for act in acts:
                for sub in subs:
                    if sub==2 and act == 4:
                        if deb_log:
                            print(f'Skip sub{sub}_act{act}')
                        continue
                    name = f'{sub:02d}_{act:02d}_c920-{cmra} ECG.csv'
                    _name = f'{sub:02d}_{act:02d}_c920-{cmra}'
                    filepath = f'{cleaner_path}/{name}'
                    file = readCSV(filepath)
                    times = file.loc[:,'Time']
                    signals = file.loc[:,'Signal']
                    peaks = file.loc[:,'Peaks']
                    if deb_log:
                        plotXY(times,signals,peaks)
                    time,gt,para = genHR(times,peaks)
                    gtpath = f'{gt_path}/{_name}_PR.csv'
                    gt_df = pd.DataFrame(
                        {
                            'time':time,
                            'HR':gt
                        }
                    )
                    
                    gt_df.to_csv(gtpath)
                    log_df = pd.DataFrame(
                        para
                    )
                    logpath = f'{log_path}/{_name}_log.csv'
                    log_df.to_csv(logpath)
        print('===> Finish')           
                    
                    
        

def _main():
    CleanerPPG_path = 'Z:/CleanerPPG'
    Datasets_list = ['ECG-Fitness']
    for dataset in Datasets_list:
        showData(
            f'{CleanerPPG_path}/{dataset}'
        )

if __name__ == '__main__':
    _main()