"""Downloads data from a url to a file specified by filepath.

Usage: data_download.py [--start_date=<start_date>] [--end_date<end_date>] --out_dir=<out_dir>
 
Options:
[<start_date>]               String: Date for beginning of available data, default will be January 1st 2020 formatted as 2020-01-01
[<end_date>]                 String: Date for ending of available data, default will be December 1st 2020 formatted as 2020-12-01
<out_dir>                    String: Output directory relative to project home path
"""

import pandas as pd 
import numpy as np
import covidcast
from datetime import date
from docopt import docopt
import os

opt = docopt(__doc__)

#def main(start_date, end_date):

#def test():

#data = covidcast.signal("chng", "smoothed_adj_outpatient_cli",
#                        date(2020, 11, 15), date(2020, 12, 15),
#                        "county")

#if __name__ == "__main__":
#    test()
#    main(opt["<url>"], opt["<filepath>"])
print(opt["<out_dir>"])