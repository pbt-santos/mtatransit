# get useful statistics from times_square_data.csv

import csv
import os


def grouped_time_based_sort(grouped_data, mode):
    # sort grouped data according to mode
    if mode == 0:  # mode = 0: total volume of movement
        sorted_grouped_data = sorted(grouped_data, key=lambda entry: sum(map(int, entry[4:6])), reverse=True)
        print("3 highest traffic turnstile groups:", sorted_grouped_data[:3])
        f = open("grpd+srtd_ttl_vol_data.csv", "w", newline="")
    elif mode == 1:  # mode = 1: total entries
        sorted_grouped_data = sorted(grouped_data, key=lambda entry: int(entry[4]), reverse=True)
        print("3 most entered turnstile groups:", sorted_grouped_data[:3])
        f = open("grpd+srtd_entry_data.csv", "w", newline="")
    elif mode == 2:  # mode = 2: total exits
        sorted_grouped_data = sorted(grouped_data, key=lambda entry: int(entry[5]), reverse=True)
        print("3 most exited turnstile groups:", sorted_grouped_data[:3])
        f = open("grpd+srtd_exit_data.csv", "w", newline="")
    else:
        return None

    # write data to csv
    writer = csv.writer(f)
    writer.writerow(["C/A", "UNIT", "DATE", "TIME", "ENTRIES", "EXITS", "num_turnstiles_per_group"])
    writer.writerows(sorted_grouped_data)
    f.close()

    print("Done grouped_time_based_sort() mode", mode)


def grouped_group_based_sort(grouped_data, mode):
    ts_groups_to_data = {}  # (C/A, UNIT) : [num_turnstiles, [DATE, TIME, ENTRIES, EXITS]]
    for row in grouped_data:
        g_id = tuple(row[:2])
        if g_id in ts_groups_to_data.keys():
            ts_groups_to_data[g_id][1].append(row[2:6])
        else:
            ts_groups_to_data[g_id] = [(row[6]), [row[2:6]]]

    for key in ts_groups_to_data.keys():
        if mode == 0:  # mode = 0: total volume of movement
            ts_groups_to_data[key][1] = sorted(ts_groups_to_data[key][1], key=lambda entry: sum(entry[2:4]), reverse=True)
            f = open("./sorted_turnstile_group_data/" + str(key[0]) + "," + str(key[1]) + "_ttl_vol_data.csv", "w", newline="")
        elif mode == 1:  # mode = 1: total entries
            ts_groups_to_data[key][1] = sorted(ts_groups_to_data[key][1], key=lambda entry: entry[2], reverse=True)
            f = open("./sorted_turnstile_group_data/" + str(key[0]) + "," + str(key[1]) + "_entry_data.csv", "w", newline="")
        elif mode == 2:  # mode = 2: total exits
            ts_groups_to_data[key][1] = sorted(ts_groups_to_data[key][1], key=lambda entry: entry[3], reverse=True)
            f = open("./sorted_turnstile_group_data/" + str(key[0]) + "," + str(key[1]) + "_exit_data.csv", "w", newline="")
        else:
            return None

        # write data to csv
        writer = csv.writer(f)
        writer.writerow(["C/A=" + str(key[0]), "UNIT=" + str(key[1]), "num_turnstiles=" + str(ts_groups_to_data[key][0])])
        writer.writerow(["DATE", "TIME", "ENTRIES", "EXITS"])
        writer.writerows(ts_groups_to_data[key][1])
        f.close()

    print("Done grouped_group_based_sort() mode", mode)


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
    print("3 highest traffic turnstiles:", hv_data[:3])

    # group individual turnstiles by control area (C/A) and UNIT
    grouped_data = []  # [C/A, UNIT, DATE, TIME, ENTRIES, EXITS, num_turnstiles_per_group]
    g_id_to_e_e = {}  # group id = (C/A, UNIT, DATE, TIME) to cumulative [ENTRIES, EXITS, num_turnstiles_per_group]
    for row in data:
        row_g_id = tuple(row[:2] + row[6:8])
        if row_g_id in g_id_to_e_e:
            g_id_to_e_e[row_g_id] = [g_id_to_e_e[row_g_id][0] + int(row[9]), g_id_to_e_e[row_g_id][1] + int(row[10]),
                                     g_id_to_e_e[row_g_id][2] + 1]
        else:
            g_id_to_e_e[row_g_id] = [int(row[9]), int(row[10]), 1]
    grouped_data = [list(key) + g_id_to_e_e[key] for key in g_id_to_e_e.keys()]
    print(grouped_data[:5])

    # sort grouped data by highest volume of movement, entries and exits over the entire year, and write results to csv files
    grouped_time_based_sort(grouped_data, 0)
    grouped_time_based_sort(grouped_data, 1)
    grouped_time_based_sort(grouped_data, 2)

    # make new directory containing csv files for each group
    try:
        os.mkdir("./sorted_turnstile_group_data")
    except OSError:
        print("Failed to create ./sorted_turnstile_group_data (probably already created)")

    # split grouped data by group, sort by highest volume of movement, entries and exits over the entire year, and write results to csv files
    grouped_group_based_sort(grouped_data, 0)
    grouped_group_based_sort(grouped_data, 1)
    grouped_group_based_sort(grouped_data, 2)
