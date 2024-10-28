from flask import Flask, request
from flask_cors import CORS
import pandas as pd
import json
import requests as http
from dtw import calculate_similarity

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def get_scatter_points():
  data_frame = pd.read_csv('./data/geodata/_rioverde.csv')
  latitude_array = data_frame['latitude'].to_list()
  longitude_array = data_frame['longitude'].to_list()
  address_array = data_frame['address'].to_list();
  value_array = data_frame['value'].to_list()

  return json.dumps(dict(lat=latitude_array, long=longitude_array, value=value_array, address=address_array))

@app.route('/<point_id>')
def get_scatter_point_data(point_id):
  data_frame = pd.read_csv(f'data/geodata_scatterpoints/{point_id}.csv')
  values = data_frame['value'].to_list()
  label = data_frame['date'].to_list()

  return json.dumps(dict(data=dict(label=label, value=values)))

@app.route('/<point_id>/similarity')
def get_similarity(point_id):
  result = calculate_similarity(point_id)
  return result

@app.route('/cnes_units')
def get_cnes_units():
  codigo_tipo_unidade = request.args.get("codigo_tipo_unidade")
  codigo_municipio = request.args.get("codigo_municipio")
  limit = request.args.get("limit")
  offset = request.args.get("offset")
  params = {
    "codigo_tipo_unidade": codigo_tipo_unidade,
    "codigo_municipio": codigo_municipio,
    "offset": offset,
    "limit": limit
  }
  print(params)
  response = http.get('https://apidadosabertos.saude.gov.br/cnes/estabelecimentos', params=params)
  return response.json()
