# get useful statistics from times_square_data.csv

import csv

if __name__ == "__main__":

    # read csv into data
    f = open("times_square_data.csv", "r")
    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append(row)
    f.close()

    # store and crop column names from data
    col_names = data[0]
    data = data[1:]

    # sort data by highest volume of movement
    hv_data = sorted(data, key=lambda entry: sum(map(int, entry[9:11])), reverse=True)
    print(hv_data[:5])

    # merge individual turnstile records and group by control area (C/A)
    merged_data = []
    g_id_to_e_e = {} # group id = (C/A, UNIT, DATE, TIME) to cumulative [ENTRIES, EXITS, num_turnstiles_per_group]
    for row in data:
        row_g_id = tuple(row[:2] + row[6:8])
        if row_g_id in g_id_to_e_e:
            g_id_to_e_e[row_g_id] = [g_id_to_e_e[row_g_id][0] + int(row[9]), g_id_to_e_e[row_g_id][1] + int(row[10]),
                                     g_id_to_e_e[row_g_id][2] + 1]
        else:
            g_id_to_e_e[row_g_id] = [int(row[9]), int(row[10]), 1]
    merged_data = [list(key) + g_id_to_e_e[key] for key in g_id_to_e_e.keys()]
    print(merged_data[:5])

    # sort merged data by highest volume of movement
    hv_merged_data = sorted(merged_data, key=lambda entry: sum(map(int, entry[5:7])), reverse=True)
    print(hv_merged_data[:5])

    # write sorted merged data to csv
    f = open("grouped+sorted_times_square_data.csv", "w", newline="")
    writer = csv.writer(f)
    writer.writerow(["C/A", "UNIT", "DATE", "TIME", "ENTRIES", "EXITS", "num_turnstiles_per_group"])
    writer.writerows(hv_merged_data)
    f.close()
