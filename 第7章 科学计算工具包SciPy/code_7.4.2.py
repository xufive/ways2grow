# -*- encoding: utf-8 -*-

"""
7.4.2 一维傅里叶变换的应用
"""

import pyaudio as pa
import numpy as np
from scipy import fft as spfft

def spectrum_analyser(data, rate):
    """频谱分析
    
    data    - 采集到的声音离散数据
    rate    - 采样频率
    """
    
    T = (data.shape[0]-1)/rate # 信号时长
    valid = int(np.ceil(data.shape[0]/2)) # 采样数量的一半
    fd = spfft.fft(data) # 快速傅里叶分析
    dforce = np.abs(fd[:valid])/data.shape[0] # 标准化的单边频谱数据
    f = np.argmax(dforce)/T # 最强分量的信号频率
        
    return f
    
def start(rate=8000, chunk=1024):
    """连续测试声音频率
    
    rate    - 采样频率
    chunk   - 声卡读写缓冲区大小
    """
    
    ac = pa.PyAudio()
    stream = ac.open(
        format = pa.paInt16,            # 设置量化精度：每个采样数据占用的位数（2字节）
        channels = 1,                   # 设置单声道模式           
        rate = rate,                    # 设置采样频率
        frames_per_buffer = chunk,      # 设置声卡读写缓冲区     
        input = True                    # 设置声卡输出模式
    )
    
    while True:
        data = b''
        while len(data) < 8000: # 至少采集8000字节
            data += stream.read(chunk) # 采集声音数据
        
        data = np.frombuffer(data[2000:6000], dtype=np.int16) # 去掉首尾可能的噪声
        f = spectrum_analyser(data, rate)
        print(f)

if __name__ == '__main__':
    # 启动频率计
    start()
