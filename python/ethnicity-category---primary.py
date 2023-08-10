# Caroline Fairhurst, Ian Watt, Fabiola Martin, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"9i","system":"readv2"},{"code":"9i20","system":"readv2"},{"code":"9i21","system":"readv2"},{"code":"9i22","system":"readv2"},{"code":"9i23","system":"readv2"},{"code":"9i25","system":"readv2"},{"code":"9i2B","system":"readv2"},{"code":"9i2F","system":"readv2"},{"code":"9i2J","system":"readv2"},{"code":"9i2K","system":"readv2"},{"code":"9i2L","system":"readv2"},{"code":"9i2M","system":"readv2"},{"code":"9i2N","system":"readv2"},{"code":"9iA1","system":"readv2"},{"code":"9iA2","system":"readv2"},{"code":"9iA4","system":"readv2"},{"code":"9iA5","system":"readv2"},{"code":"9iA6","system":"readv2"},{"code":"9iD0","system":"readv2"},{"code":"9iD1","system":"readv2"},{"code":"9iF0","system":"readv2"},{"code":"9iF1","system":"readv2"},{"code":"9iF2","system":"readv2"},{"code":"9iF3","system":"readv2"},{"code":"9iF4","system":"readv2"},{"code":"9iF5","system":"readv2"},{"code":"9iF6","system":"readv2"},{"code":"9iF7","system":"readv2"},{"code":"9iF8","system":"readv2"},{"code":"9iF9","system":"readv2"},{"code":"9iFC","system":"readv2"},{"code":"9iFD","system":"readv2"},{"code":"9iFE","system":"readv2"},{"code":"9iFF","system":"readv2"},{"code":"9iG","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ethnicity-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ethnicity-category---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ethnicity-category---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ethnicity-category---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
