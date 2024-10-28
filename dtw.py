import json
from dtaidistance import dtw
import pandas as pd
import os

def get_dtw_distance(timeseries_id_1, timeseries_id_2):
  ts_1 = pd.read_csv(f'./data/geodata_scatterpoints/{timeseries_id_1}')
  ts_2 = pd.read_csv(f'./data/geodata_scatterpoints/{timeseries_id_2}')

  # Load the JSON data
  ts_list_1 = ts_1['value']
  ts_list_2 = ts_2['value']

  # Calculate the distance using Dynamic Time Warping (DTW)
  distance = dtw.distance(ts_list_1, ts_list_2)
  data = {
    "id": timeseries_id_2,
    "values": ts_2['value'].to_list(),
    "labels": ts_2['date'].to_list(),
    "distance": distance
  }
  return data

def calculate_similarity(except_file):
  files = os.listdir('./data/geodata_scatterpoints')
  different_files = filter(lambda file: file != f'{except_file}.csv', files)
  response = list()
  for file in different_files:
    similarity = get_dtw_distance(f'{except_file}.csv', file)
    response.append(similarity)
  return response
