# ECG-FitnessPulseRate

CleanerPPG[1]對多項 rPPG 研究相關的資料集找尋專業人士共同標註峰值點，  
本代碼透過該團隊標註的 ECG 峰值點定義 ECG-Fitness[2]每秒心率基準點，  
需注意的有本代碼以 8 秒的滑動窗口計算 PPI 換算成心率數值並保留小數，每個.csv 檔案包含每秒的心率 GroundTruth。

# Description
Dear user, if you use this code to generate heart rate results, you do not need to mark them as coming from me,
but please remember to cite the paper that proposed the ECG-Fitness dataset and the paper that proposed the CleanerPPG dataset.
By the way, if you find that the definition of heart rate estimation in this code is unreasonable, you can open an issue discussion. (from google translate)

## If this is helpful, give a star.

# Reference

[1] https://www.mdpi.com/2076-3417/10/23/8630  
[2] https://cmp.felk.cvut.cz/~spetlrad/ecg-fitness/
