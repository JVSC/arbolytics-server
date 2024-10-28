import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import argparse

def generate_csv(start_date, num_days, value_range, id_value, output_file):
  dates = [start_date + timedelta(days=i) for i in range(num_days)]
  values = np.random.randint(value_range[0], value_range[1], size=num_days)

  data = {
      'date': dates,
      'value': values,
      'id': [id_value] * num_days
  }

  df = pd.DataFrame(data)
  df.to_csv(f'{output_file}.csv', index=False)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Generate a CSV file with date, value, and id.")
  parser.add_argument('start_date', type=str, help='Start date in YYYY-MM-DD format')
  parser.add_argument('num_days', type=int, help='Number of days to generate')
  parser.add_argument('value_range', type=int, nargs=2, help='Range for random values (min, max)')
  parser.add_argument('id_value', type=str, help='ID to assign to each row')
  parser.add_argument('output_file', type=str, help='Output CSV file name')

  args = parser.parse_args()

  # Convert start_date from string to datetime
  start_date = datetime.strptime(args.start_date, '%Y-%m-%d')

  # Call the function to generate the CSV
  generate_csv(start_date, args.num_days, args.value_range, args.id_value, args.output_file)
