import os
import csv
import re


def parse_doxygen_warnings_log(log_file_path):
    """
     warnings log file  containing the line number, file name, and warning message.
    """
    log_entries = []
    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                line = line.strip()
                match = re.match(r"(.+?):(\d+):\s+(\w+):\s+(.+)", line)
                if match:
                    log_entries.append({'line': match.group(2), 'file': match.group(1), 'message': match.group(4)})
    except FileNotFoundError:
        print(f"Error: File '{log_file_path}' not found.")
        return []

    return log_entries

def write_csv_file(log_entries, output_file_path):
    """
    Write log to a CSV file.
    """
    with open(output_file_path, mode='w', newline='') as output_file:
        writer = csv.writer(output_file)

        # Write the header row
        writer.writerow(['line', 'file', 'message'])

        # Write each log entry as a row in the CSV file
        for log_entry in log_entries:
            row = [log_entry['line'], log_entry['file'], log_entry['message']]
            writer.writerow(row)

    print("CSV file written to:", output_file_path)

if __name__ == '__main__':
    log_file_path = os.path.abspath('warnings.log')
    output_file_path = 'output.csv'

    log_entries = parse_doxygen_warnings_log(log_file_path)
    write_csv_file(log_entries, output_file_path)
