# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"C370.00","system":"readv2"},{"code":"24137.0","system":"readv2"},{"code":"49770.0","system":"readv2"},{"code":"36622.0","system":"readv2"},{"code":"13264.0","system":"readv2"},{"code":"69017.0","system":"readv2"},{"code":"65344.0","system":"readv2"},{"code":"18914.0","system":"readv2"},{"code":"103224.0","system":"readv2"},{"code":"6220.0","system":"readv2"},{"code":"73065.0","system":"readv2"},{"code":"18905.0","system":"readv2"},{"code":"E84","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cystic-fibrosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["fibrosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["fibrosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["fibrosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
