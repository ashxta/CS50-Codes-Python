import sys
import csv
from tabulate import tabulate

def format_csv_to_ascii_table(file_path):
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)

            data = [dict(zip(header, row)) for row in reader]

            table = tabulate(data, headers="keys", tablefmt="grid")

            return table
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python pizza.py <file.csv>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not file_path.endswith('.csv'):
        print("Invalid file extension. Please specify a CSV file.")
        sys.exit(1)

    ascii_table = format_csv_to_ascii_table(file_path)
    print(ascii_table)

if __name__ == "__main__":
    main()
