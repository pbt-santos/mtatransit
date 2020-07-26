Usage:

$ python get_data.py
$ python get_statistics.py

Action:

Running get_data.py will produce the file times_square_data.csv, which contains all turnstile data for Times Square Station in 2019

Running get_statistics.py will:
(1) print the 3 highest traffic individual turnstiles for <=4h time periods in 2019
(2) create the file grpd+srtd_ttl_vol_data.csv, which contains the grouped, by turnstile area (C/A and UNIT), and sorted, by total volume (sum of entries and exits), for =<4h time periods in 2019
(3) create the file grpd+srtd_entry_data.csv, which contains the grouped (same as above) and sorted, by total entries, for <=4h time periods in 2019
(4) create the file grpd+srtd_exit_data.csv, which contains the grouped (same as above) and sorted, by total exits, for <=4h time periods in 2019
(5) create the directory sorted_turnstile_group_data
(6) create 3 files in sorted_turnstile_group_data for each turnstile group, containing only data relevant to that turnstile group. Note that each file is named with C/A,UNIT at the beginning of the file name 
	(a) files of the form C/A,UNIT_ttl_vol_data.csv contain the subset of the data relevant to that C/A and UNIT sorted as in (2)
	(b) files of the form C/A,UNIT_entry_data.csv contain the subset of the data relevant to that C/A and UNIT sorted as in (3)
	(c) files of the form C/A,UNIT_exit_data.csv contain the subset of the data relevant to that C/A and UNIT sorted as in (4)
