# Caroline Fairhurst, Ian Watt, Fabiola Martin, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"226","system":"readv2"},{"code":"226Z","system":"readv2"},{"code":"9S","system":"readv2"},{"code":"9SE","system":"readv2"},{"code":"9SJ","system":"readv2"},{"code":"9SZ","system":"readv2"},{"code":"9T1A","system":"readv2"},{"code":"9iFK","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ethnicity-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ethnicity-group---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ethnicity-group---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ethnicity-group---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
