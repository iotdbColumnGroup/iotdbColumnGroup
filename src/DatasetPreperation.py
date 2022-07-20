# coding=utf-8
import imp
from math import floor
import pandas as pd
import os
import numpy as np
import datetime
import time


def dataset_sampling(data_size_rate, time_series_rate, read_path):
    file_list = os.listdir(read_path)
    write_path = read_path + "\\sample"
    for file_name in file_list:
        if file_name[-4:] != ".csv":
            continue
        df = pd.read_csv(read_path + "\\" + file_name)
        data = np.array(df)
        time_sample = np.random.binomial(1, time_series_rate, data.shape[0])
        attribute_sample = np.insert(np.random.binomial(1, data_size_rate, data.shape[1] - 1), 0, 1)
        sampled_data = (data[:, np.where(attribute_sample == 1)[0]])[np.where(time_sample == 1)[0], :]
        sampled_df = pd.DataFrame(sampled_data)
        sampled_df.columns = list(np.array(df.columns[np.where(attribute_sample == 1)[0]]))
        sampled_df.to_csv(write_path + "\\" + file_name[:-4] + "_sampled.csv")


def string_to_timestamp_1(str_time):
    dt = time.strptime(str_time, "%Y-%m-%d %H:%M:%S.%f")
    ts = int(time.mktime(dt)) * 1000 + int(str_time[-3:])
    return ts


def string_to_timestamp_2(str_time):
    dt = time.strptime(str_time, "%Y-%m-%dT%H:%M:%S.%f+08:00")
    ts = int(time.mktime(dt)) * 1000 + int(str_time[-9:-6])
    return ts


def string_to_timestamp_0(str_time):
    if str_time[4] == "-" and str_time[6] == "-":
        str_time = str_time[:5] + "0" + str_time[5:]
    if str_time[12] == ":":
        str_time = str_time[:11] + "0" + str_time[11:]
    if len(str_time) != 19:
        str_time = str_time + ":00"
    dt = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    ts = int(time.mktime(dt)) * 1000
    return ts


def generate_unaligned_timeseries(file_path, noise_rate):
    df = pd.read_csv(file_path)
    data = np.array(df)
    return


def acquire_data(file_path):
    return np.array(pd.read_csv(file_path))


def timestamp_noise(timestamp):
    noise = int(max(min(np.random.normal(0, 2500), 3200), -3200))
    return timestamp + noise
