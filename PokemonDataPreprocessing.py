
import csv
import argparse
import re

def replace_commas_in_quotes(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
          new_row = []
          for field in row:
            if ', ' in field:
              new_field = re.sub(r'(?<!^), (?!$)', '/', field)
              new_row.append(new_field)
            else:
              new_row.append(field)
          writer.writerow(new_row)

        infile.close()
        outfile.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Replace commas inside quoted fields in a CSV file.")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("output_file", help="Path to the output CSV file")
    args = parser.parse_args()

    # Call the function with command-line arguments
    replace_commas_in_quotes(args.input_file, args.output_file)
