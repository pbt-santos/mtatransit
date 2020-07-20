# isolate Times Square data from MTA and write to csv

import requests
import re
import datetime
import csv

DELTA = datetime.timedelta(hours=4)
BEG_TIME = datetime.datetime(month=1, day=1, year=2019, hour=0, minute=0, second=0)
END_TIME = datetime.datetime(month=1, day=1, year=2020, hour=0, minute=0, second=0)

if __name__ == "__main__":

    # read data from turnstile_data
    f = open("turnstile_data.txt")
    td = f.read()
    f.close()

    # prepare for organized web-scraping
    td = td.split("<a")
    td.reverse()
    urls = []
    for d in td:
        path_to_csv = re.match(".*href=\"(.*)\"", d).group(1)
        urls.append("http://web.mta.info/developers/" + path_to_csv)

    # execute web-scrape and storing of relevant data
    data = [["C/A", "UNIT", "SCP", "STATION", "LINENAME", "DIVISION", "DATE", "TIME", "DESC", "ENTRIES", "EXITS"]]
    t_id_to_last_e_e = {}  # turnstile id (C/A, UNIT, SCP) to last [datetime_of_DATE_and_TIME, ENTRIES, EXITS]
    url_counter = 1
    for url in urls:
        payload = requests.get(url).text
        payload = payload.replace(" ", "")  # get rid of whitespace padding at end of lines
        payload = payload.splitlines()
        for line in payload[1:]:
            # check for relevance to Times Square
            if re.match(".*(TIMESSQ\-42ST|42ST\-PORTAUTH).*", line):
                line = line.split(",")
                # get datetime representation of DATE and TIME
                date = re.match("(\d*?)\/(\d*?)\/(\d*)", line[6])
                time = re.match("(\d*?):(\d*?):(\d*)", line[7])
                dt = datetime.datetime(month=int(date.group(1)), day=int(date.group(2)), year=int(date.group(3)),
                                       hour=int(time.group(1)), minute=int(time.group(2)), second=int(time.group(3)))
                t_id = tuple(line[:3])
                # check that record is within 2019 and if record for current turnstile already exists
                if BEG_TIME < dt < END_TIME and t_id in t_id_to_last_e_e.keys():
                    prev = t_id_to_last_e_e[t_id]
                    actual_e_e = [abs(int(line[9]) - prev[1]), abs(int(line[10]) - prev[2])] # abs cuz fuck mta
                    # check that record is at most 4 hours ahead of previous record, and that e_e is reasonable
                    if prev[0] >= dt - DELTA and sum(actual_e_e) < 10000:
                        data.append(line[:9] + actual_e_e)
                # update t_id_to_last_e_e entry
                t_id_to_last_e_e[t_id] = [dt] + list(map(int, line[9:11]))
        print("Done", url_counter, "of", len(urls))
        url_counter += 1

    f = open("times_square_data.csv", "w", newline="")
    writer = csv.writer(f)
    writer.writerows(data)
    f.close()
