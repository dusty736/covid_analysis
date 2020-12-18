"""Combines data into single dataset in data/raw. Exports into train and test data in data/processed.

Usage: data_preprocessing.py --out_dir=<out_dir> [--train_ratio=<train_ratio>]
 
Options:
--out_dir=<out_dir>    						    String: Output Directory
[--train_ratio=<train_ratio>]              Float: The training ratio (Default is 0.7)
"""

import pandas as pd 
import numpy as np
import covidcast
import datetime
from docopt import docopt
import os
import glob

opt = docopt(__doc__)

# Steps
# 1. Read in data on set at a time
# 2. Change the variable names
# 3. Combine into one dataset
# 4. Export into processed folder
# 5. Split into train and test data
# 6. Export train and test data into processed folder

def main(train_ratio, out_dir):
	data_files = glob.glob(out_dir + '/*.csv')
	generic_col_names = [geo_value, time_value, value, stderr, sample_size]

	# Define new column names
	col_names = 

	for i, file in enumerate(data_files):
		if i == 0:
			combined_df = pd.read_csv(file)
		else:
			tmp_df = pd.read_csv(file)
			renamed_df = col_name_changer(tmp_df, )

def test(out_dir):
	data_files = glob.glob(out_dir + '/*.csv')
	assert len(data_files) == 23, "Not every data file included!"

def col_name_changer(df, filename):
	col_name_dict = {}

if __name__ == "__main__":
	test(opt["--out_dir"])
	main(opt["--train_ratio"], opt["--out_dir"])