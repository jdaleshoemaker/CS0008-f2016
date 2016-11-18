# file name for list of input CSV files
csv_list_file_name = 'f2016_cs8_a3.data.txt'
# output listing file name
output_file_name = 'f2016_cs8_jds140_a3.data.output.csv'

# all data dictionary {runner1: [distance1, distance2, ...], runner2: ..., ...}
all_data = dict()
# counter for total lines read from CSV (including headers)
total_lines = 0


def get_csv_set():
    # Get set of CSV files
    global csv_list_file_name
    # read all CSV filename into one set
    with open(csv_list_file_name) as f_in:
        csv_set = {x.strip() for x in f_in.readlines()}
    return csv_set


def read_csv_file(file_name):
    # Read all lines in CSV file
    global all_data, total_lines
    # open current CSV file
    with open(file_name) as f_in:
        # read and ignore first line of headers
        f_in.readline()
        # increment counter of total read lines
        total_lines += 1
        # iterate through each line in current csv file
        for row in f_in:
            # get list of strings [name, distance]
            x = row.split(',')
            # get cleaned name
            name = x[0].strip()
            # get cleaned float number of distance
            distance = float(x[1].strip())
            # check if the name was in all data dict
            if name in all_data:
                # append the distance to the current runner's distance list
                all_data[name].append(distance)
            else:
                # set the distance as the first element to the current runner's distance list
                all_data[name] = [distance]
            # increment counter of total read lines
            total_lines += 1


def console_output(csv_set):
    # Print out all necessary information
    global total_lines, all_data
    # number of files read = length of csv_list list
    print('Number of Input files read\t : ' + str(len(csv_set)))

    print('Total number of lines read\t : ' + str(total_lines))

    # sum all sums of values in distances' list for each runner
    total_distance = sum(sum(value) for value in all_data.values())
    print('total distance run\t\t\t : %.5f' % total_distance)

    # get temp dict {maximum_distance: runner}
    temp_dict = {max(value): key for key, value in all_data.items()}
    # get maximum distance from it
    max_distance = max(temp_dict)
    # get runner's name from it
    runner = temp_dict[max_distance]
    print('max distance run\t\t\t : %.5f' % max_distance + '\n  by participant\t\t\t : ' + runner)

    # total number of participants == length of all_data dictionary
    print('Total number of participants : ' + str(len(all_data)))

    # count all runners with length of distance list > 1
    multiple_records = sum(True for x in all_data if len(all_data[x]) > 1)
    print('with multiple records\t\t : ' + str(multiple_records))


def write_output_file():
    # Write the output file
    global all_data
    with open(output_file_name, 'w') as out_f:
        for runner in all_data:
            # get runner's name, times of occurences and total distance
            name = runner
            times = len(all_data[runner])
            total = sum(all_data[runner])
            # write these values
            out_f.write(name + ',' + str(times) + ',' + '%.2f' % total + '\n')


def main():
    # Main function
    # get CSV filenames' set
    csv_set = get_csv_set()
    # iterating through all CSV files
    for file_name in csv_set:
        read_csv_file(file_name)
    # print out necessary info
    console_output(csv_set)
    # write data to the output file
    write_output_file()


if __name__ == '__main__':
    main()
