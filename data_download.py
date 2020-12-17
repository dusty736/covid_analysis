"""Downloads data from a url to a file specified by filepath.

Usage: data_download.py --out_dir=<out_dir> [--start_date=<start_date>] [--end_date=<end_date>]
 
Options:
--out_dir=<out_dir>    
[--start_date=<start_date>]              String: Date for beginning of available data, default will be February 1st 2020 formatted as YYYY-MM-DD
[--end_date=<end_date>]                 String: Date for ending of available data, default will be February 1st 2020 formatted as YYYY-MM-DD                String: Output directory relative to project home path
"""

import pandas as pd 
import numpy as np
import covidcast
import datetime
from docopt import docopt
import os

opt = docopt(__doc__)

def main(start_date, end_date, out_dir):

    # Set default values
    if start_date == None:
        start_date = "2020-02-01"
    if end_date == None:
        end_date = "2020-12-01"

    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

    data_sources = {"chng" : ["smoothed_adj_outpatient_cli"],
                    "indicator-combination" : ["nmf_day_doc_fbc_fbs_ght"],
                    "fb-survey": ["smoothed_cli",
                                  "smoothed_hh_cmnty_cli",
                                  "smoothed_wearing_mask"],
                    "hospital-admissions" : ["smoothed_adj_covid19_from_claims"],
                    "indicator-combination" : ["confirmed_7dav_incidence_num",
                                               "confirmed_7dav_incidence_prop",
                                               "confirmed_cumulative_num",
                                               "confirmed_cumulative_prop",
                                               "confirmed_incidence_num",
                                               "confirmed_incidence_prop",
                                               "deaths_7dav_incidence_num",
                                               "deaths_7dav_incidence_prop"],
                    "quidel" : ["covid_ag_smoothed_pct_positive"],
                    "safegraph" : ["bars_visit_prop",
                                   "full_time_work_prop_7dav",
                                   "part_time_work_prop_7dav",
                                   "restaurants_visit_prop"]}

    for source in data_sources.keys():
        for signal in data_sources[source]:
            data = covidcast.signal(source, signal,
                                    start_date, end_date,
                                    "county")

            file_name = out_dir + "/" + signal + ".csv"

            data.to_csv(file_name)

def test():
    """Tests file structure and input formats for file parameters
    Parameters
    ----------
    Returns
    -------
    None
    """

    # Test path
    assert os.path.isdir(opt["--out_dir"]), "Incorrect file path!"

    # Test for date format
    format = "%Y-%m-%d"
    if opt["--start_date"] != None:
        assert datetime.datetime.strptime(opt["--start_date"], format), "Incorrect start date format, please use: YYYY-MM-DD"
    else:
        pass
    
    if opt["--end_date"] != None:
        assert datetime.datetime.strptime(opt["--end_date"], format), "Incorrect end date format, please use: YYYY-MM-DD"
    else:
        pass 

if __name__ == "__main__":
    test()
    main(opt["--start_date"], opt["--end_date"], opt["--out_dir"])