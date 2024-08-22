import csv

def read_csv(filepath):
    lines = []
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            line_no_spaces = []
            for r in line:
                line_no_spaces.append(r.strip())
            lines.append(line_no_spaces)
    return lines