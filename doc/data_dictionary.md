Data Source | Signal | CSV Name | Old Variable Name | New Variable Name | Units | Description | Primary Key |
--- | --- | --- | --- |--- |--- |--- |--- |
chng | Covid Related Doctor Visits | smoothed_adj_outpatient_cli.csv | lag, value, stderr, sample_size | pct_visits_covid_lag, pct_visits_covid, pct_visits_covid_stderr, pct_visits_covid_samp_size |  | Percentage of daily doctor visits that are due to COVID-like symptoms | geo_value, time_value |
COVID Indicator Combination | COVID Indicator Combination | nmf_day_doc_fbc_fbs_ght.csv | lag, value, stderr, sample_size | comb_lag, comb_value, comb_stderr, comb_samp_size |  | Combination of several COVID-19 indicators available at this geographic level | geo_value, time_value |
Delphi Survey Results | COVID-Like Symptoms | smoothed_cli.csv |  |  |  | Percentage of people with COVID-like symptoms, based on surveys of Facebook users |  |
Delphi Survey Results | COVID-Like Symptoms in Community | smoothed_hh_cmnty_cli.csv |  |  |  | Percentage of people who know someone in their local community with COVID-like symptoms, based on surveys of Facebook users |  |
Delphi Survey Results | People Wearing Masks | smoothed_wearing_mask.csv |  |  |  | Percentage of people who report wearing a mask most or all of the time while in public, based on surveys of Facebook users |  |
Hospital Admissions | COVID Hospital Admissions | smoothed_adj_covid19_from_claims.csv |  |  |  | Percentage of daily hospital admissions with COVID-19 associated diagnoses |  |
Public Health Reports | COVID Cases (7-day average) | confirmed_7dav_incidence_num.csv |  |  |  | Newly reported COVID-19 cases (7-day average) |  |
Public Health Reports | COVID Cases (per 100,000 people) (7-day average) | confirmed_7dav_incidence_prop.csv |  |  |  | Newly reported COVID-19 cases per 100,000 people (7-day average) |  |
Public Health Reports | Cumulative COVID Cases | confirmed_cumulative_num.csv |  |  |  | Cumulative reported COVID-19 cases |  |
Public Health Reports | Cumulative COVID Cases (per 100,000 people) | confirmed_cumulative_prop.csv |  |  |  | Cumulative reported COVID-19 cases per 100,000 people |  |
Public Health Reports | COVID Cases | confirmed_incidence_num.csv |  |  |  | Newly reported COVID-19 cases (7-day average) |  |
Public Health Reports | COVID Cases (per 100,000 people) | confirmed_incidence_prop |  |  |  | Newly reported COVID-19 cases per 100,000 people (7-day average) |  |
Public Health Reports | COVID Deaths (7-day average) | deaths_7dav_incidence_num.csv |  |  |  | Newly reported COVID-19 deaths (7-day average) |  |
Public Health Reports | COVID Deaths (per 100,000 people) (7-day average) | deaths_7dav_incidence_prop.csv |  |  |  | Newly reported COVID-19 deaths per 100,000 people (7-day average) |  |
Public Health Reports | Cumulative COVID Deaths | deaths_cumulative_num.csv |  |  |  | Cumulative reported COVID-19 deaths |  |
Public Health Reports | Cumulative COVID Deaths (per 100,000 people) | deaths_cumulative_prop.csv |  |  |  | Cumulative reported COVID-19 deaths per 100,000 people |  |
Public Health Reports | COVID Deaths | deaths_incidence_num.csv |  |  |  | Newly reported COVID-19 deaths (7-day average) |  |
Public Health Reports | COVID Deaths (per 100,000 people) | deaths_incidence_prop |  |  |  | Newly reported COVID-19 deaths per 100,000 people (7-day average) |  |
Quidel Antigen Tests | COVID Antigen Test Positivity (Quidel) | covid_ag_smoothed_pct_positive.csv |  |  |  | Positivity rate of COVID-19 antigen tests, based on data provided by Quidel, Inc. |  |
SafeGraph Mobility Data | Bar Visits | bars_visit_prop.csv |  |  |  | Daily number of visits to bars per 100,000 people, based on SafeGraph’s Weekly Patterns dataset |  |
SafeGraph Mobility Data | At Away Location 6hr+ | full_time_work_prop_7dav.csv |  |  |  | 7-day trailing average of fraction of people spending 6 hours or more between 8am-6pm, in one location away from their home, based on SafeGraph mobility data |  |
SafeGraph Mobility Data | At Away Location 3-6hr | part_time_work_prop_7dav.csv |  |  |  | 7-day trailing average of fraction of people spending 3-6 hours between 8am-6pm, in one location away from their home, based on SafeGraph mobility data |  |
SafeGraph Mobility Data | Restaurant Visits | restaurants_visit_prop.csv |  |  |  | Daily number of visits to restaurants per 100,000 people, based on SafeGraph’s Weekly Patterns dataset |  |
