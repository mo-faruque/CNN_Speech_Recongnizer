# -*- coding: utf-8 -*-
"""final rastaplp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pEH2nWug72HsUcT6006ZOJLaBUNNsMmk
"""

import keras
from keras.layers import Activation, Dense, Dropout, Conv2D, \
                         Flatten, MaxPooling2D, BatchNormalization
from keras.models import Sequential
import librosa
import librosa.display
import numpy as np
import pandas as pd
import random
import sklearn
import warnings
warnings.filterwarnings('ignore')

import os
from pydub import AudioSegment

from shennong.audio import Audio
from shennong.features.processor.rastaplp import RastaPlpProcessor


from shennong.audio import Audio
from shennong.features.processor.plp import PlpProcessor
from pathlib import Path

y, sr = librosa.load('/home/raffael/bangla asr/3s/messenger/test/fold1/Chitra apu_00.wav')  
ps = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=36)

import matplotlib.pyplot as plt
plt.figure(figsize=(3, 3))
librosa.display.specshow(rplps, x_axis='time')
plt.colorbar()
plt.title('RASTA-PLP')
plt.tight_layout()
plt.savefig(' plot rasta1.png')
plt.show()

fs, sig = scipy.io.wavfile.read("/home/raffael/bangla asr/3s/messenger/test/fold1/Chitra apu_00.wav")
rplps = rplp(sig, fs, num_ceps)
vis.visualize_features(rplps, 'RPLP Index', 'Frame Index')

vis.visualize_features(rasta_plp, 'MFCC Index', 'Frame Index')
plt.savefig(' plot mfcc2.png')

audio = Audio.load('/home/raffael/bangla asr/3s/messenger/test/fold1/Chitra apu_00.wav')
processor = RastaPlpProcessor()
processor.sample_rate = audio.sample_rate
processor.order =12
rasta_plp= processor.process(audio.channel(0))

# Read Data of train samples
data = pd.read_csv('/home/raffael/bangla asr/3s/metadata/messenger xxx train.csv')
train_data= data[['slice_file_name', 'fold' ,'classID']]
train_data['path'] = 'fold' + train_data['fold'].astype('str') + '/' + train_data['slice_file_name'].astype('str')

# Read Data of train samples
data = pd.read_csv('/home/raffael/bangla asr/3s/metadata/messenger xxx test.csv')
test_data = data[['slice_file_name', 'fold' ,'classID']]
test_data['path'] = 'fold' + test_data['fold'].astype('str') + '/' + test_data['slice_file_name'].astype('str')


# Read Data of train samples
data = pd.read_csv('/home/raffael/bangla asr/3s/metadata/messenger xxx validation.csv')
validation_data = data[['slice_file_name', 'fold' ,'classID']]
validation_data['path'] = 'fold' + validation_data['fold'].astype('str') + '/' + validation_data['slice_file_name'].astype('str')

A1 = [] # Dataset
for row in train_data.itertuples():
    audio = Audio.load('/home/raffael/bangla asr/3s/messenger/train/' + (row.path))
    processor = RastaPlpProcessor()
    processor.sample_rate = audio.sample_rate
    processor.order =12
    rasta_plp= processor.process(audio.channel(0))
    if rasta_plp.shape != (298, 13): continue
    A1.append( (rasta_plp.data, row.classID) )

aD3=[]
for row in train_data.itertuples():
    y, sr = librosa.load('/home/raffael/bangla asr/3s/noise/ac/augment/4/' + (row.path))  
    ps = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=36)
    if ps.shape != (36, 130): continue
    aD3.append( (ps, row.classID) )
    
import pickle

###Load into file
with open("aD3.pkl","wb") as f:
    pickle.dump(aD3,f)