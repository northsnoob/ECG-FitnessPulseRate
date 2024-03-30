# ECG-FitnessPulseRate
CleanerPPG[1]對多項rPPG研究相關的資料集找尋專業人士共同標註峰值點， \n
本代碼透過該團隊標註的ECG峰值點定義ECG-Fitness[2]每秒心率基準點，\n
需注意的有本代碼以8秒的滑動窗口計算PPI換算成心率數值並保留小數，每個.csv檔案包含每秒的心率GroundTruth。\n
\n
# Reference
[1] https://www.mdpi.com/2076-3417/10/23/8630
[2] https://cmp.felk.cvut.cz/~spetlrad/ecg-fitness/
