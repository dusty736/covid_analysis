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
from sklearn.model_selection import train_test_split

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

	for i, file in enumerate(data_files):
		print(i, file)
		if i == 0:
			combined_df = pd.read_csv(file)
			combined_df = col_name_changer(combined_df, file)
		else:
			tmp_df = pd.read_csv(file)
			renamed_df = col_name_changer(tmp_df, file)
			combined_df = pd.merge(combined_df, renamed_df, how="outer", on=['geo_value', 'time_value'])

	state_names = get_county_name()

	combined_df = pd.merge(combined_df, state_names, how="inner", on=['geo_value'])
	
	train_df, test_df = train_test_split(combined_df, train_size=float(train_ratio), random_state=42)

	train_df.to_csv("data/processed/train_data.csv")
	test_df.to_csv("data/processed/test_data.csv")
	combined_df.to_csv("data/processed/combined_data.csv")

def test(out_dir):
	data_files = glob.glob(out_dir + '/*.csv')
	assert len(data_files) == 23, "Not every data file included!"

def col_name_changer(df, filename):
	col_name_dict = {"data/raw/full_time_work_prop_7dav.csv" : ["full_time_work_prop_7dav", "full_time_work_prop_7dav_stderr", "full_time_work_prop_7dav_sample_size"],
						  "data/raw/smoothed_wearing_mask.csv" : ["wearing_mask_pct", "wearing_mask_pct_stderr", "wearing_mask_pct_sample_size"],
						  "data/raw/smoothed_adj_outpatient_cli.csv" : ["pct_visits_covid", "pct_visits_covid_stderr", "pct_visits_covid_samp_size"],
						  "data/raw/bars_visit_prop.csv" : ["bars_visit_prop", "bars_visit_prop_stderr", "bars_visit_prop_sample_size"],
						  "data/raw/deaths_cumulative_prop.csv" : ["deaths_cumulative_prop", "deaths_cumulative_prop_stderr", "deaths_cumulative_prop_sample_size"],
						  "data/raw/confirmed_7dav_incidence_prop.csv" : ["deaths_7dav_incidence_prop", "deaths_7dav_incidence_prop_stderr", "deaths_7dav_incidence_prop_sample_size"],
						  "data/raw/deaths_7dav_incidence_num.csv" : ["deaths_7dav_incidence_num", "deaths_7dav_incidence_num_stderr", "deaths_7dav_incidence_num_sample_size"],
						  "data/raw/part_time_work_prop_7dav.csv" : ["part_time_work_prop_7dav", "part_time_work_prop_7dav_stderr", "part_time_work_prop_7dav_sample_size"],
						  "data/raw/covid_ag_smoothed_pct_positive.csv" : ["covid_ag_smoothed_pct_positive", "covid_ag_smoothed_pct_positive_stderr", "covid_ag_smoothed_pct_positive_sample_size"],
						  "data/raw/deaths_cumulative_num.csv" : ["deaths_cumulative_num", "deaths_cumulative_num_stderr", "deaths_cumulative_num_sample_size"],
						  "data/raw/smoothed_hh_cmnty_cli.csv" : ["cmnty_cli_pct", "cmnty_cli_pct_stderr", "cmnty_cli_pct_sample_size"],
						  "data/raw/nmf_day_doc_fbc_fbs_ght.csv" : ["comb_ind_value", "comb_ind_stderr", "comb_ind_samp_size"],
						  "data/raw/smoothed_cli.csv" : ["cli_pct", "cli_pct_stderr", "cli_pct_sample_size"],
						  "data/raw/deaths_incidence_prop.csv" : ["deaths_incidence_prop", "deaths_incidence_prop_stderr", "deaths_incidence_prop_sample_size"],
						  "data/raw/confirmed_incidence_prop.csv" : ["confirmed_incidence_prop", "confirmed_incidence_prop_stderr", "confirmed_incidence_prop_sample_size"],
						  "data/raw/deaths_7dav_incidence_prop.csv" : ["confirmed_7dav_incidence_prop", "confirmed_7dav_incidence_prop_stderr", "confirmed_7dav_incidence_prop_sample_size"],
						  "data/raw/deaths_incidence_num.csv" : ["deaths_incidence_num", "deaths_incidence_num_stderr", "deaths_incidence_num_sample_size"],
						  "data/raw/confirmed_cumulative_prop.csv" : ["confirmed_cumulative_prop", "confirmed_cumulative_prop_stderr", "confirmed_cumulative_prop_sample_size"],
						  "data/raw/confirmed_cumulative_num.csv" : ["confirmed_cumulative_num", "confirmed_cumulative_num_stderr", "confirmed_cumulative_num_sample_size"],
						  "data/raw/restaurants_visit_prop.csv" : ["restaurants_visit_prop", "restaurants_visit_prop_stderr", "restaurants_visit_prop_sample_size"],
						  "data/raw/confirmed_7dav_incidence_num.csv" : ["confirmed_7dav_incidence_num", "confirmed_7dav_incidence_num_stderr", "confirmed_7dav_incidence_num_sample_size"],
						  "data/raw/confirmed_incidence_num.csv" : ["confirmed_incidence_num", "confirmed_incidence_num_stderr", "confirmed_incidence_num_sample_size"],
						  "data/raw/smoothed_adj_covid19_from_claims.csv" : ["hosp_adm_pct", "hosp_adm_pct_stderr", "hosp_adm_pct_sample_size"]}

	new_col_names = col_name_dict[filename]
	col_name_change = dict(zip(["value", "stderr", "sample_size"], new_col_names))
	df = df[["geo_value", "time_value", "value", "stderr", "sample_size"]]
	df['geo_value'] = df['geo_value'].apply(str)
	df['geo_value'] = df['geo_value'].str.zfill(5)

	return(df.rename(columns = col_name_change, errors = "raise"))

def get_county_name():
	geo_data = pd.read_csv("https://raw.githubusercontent.com/kjhealy/fips-codes/master/county_fips_master.csv", encoding ='latin1')
	geo_data['fips'] = geo_data['fips'].apply(str)
	geo_data['fips'] = geo_data['fips'].str.zfill(5)
	geo_data = geo_data.rename(columns = {"fips" : "geo_value"})

	#geo_data['County Code (FIPS)'] = geo_data['County Code (FIPS)'].apply(str)
	#geo_data['County Code (FIPS)'] = geo_data['County Code (FIPS)'].str.zfill(3)

	#geo_data["geo_value"] = geo_data['State Code (FIPS)'] + geo_data['County Code (FIPS)']

	#state_codes = pd.read_csv("https://www2.census.gov/geo/docs/reference/state.txt", sep="|")
	#state_codes['STATE'] = state_codes['STATE'].apply(str)
	#state_codes['STATE'] = state_codes['STATE'].str.zfill(2)
	#state_codes = state_codes.rename(columns = {"STATE" : "State Code (FIPS)", "STATE_NAME" : "state_name", "Area Name (including legal/statistical area description)" : "county_name"})

	#geo_data = pd.merge(geo_data, state_codes[['State Code (FIPS)', 'state_name']], how="left", on="State Code (FIPS)")
	#geo_data.rename(columns = {"Area Name (including legal/statistical area description)" : "county_name"})
	#test = geo_data[['geo_value', 'county_name', 'state_name']]

	return(geo_data[['geo_value', 'county_name', 'state_name']])

if __name__ == "__main__":
	test(opt["--out_dir"])
	main(opt["--train_ratio"], opt["--out_dir"])