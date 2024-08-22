def read_property(key, file):
    config_file = open(file)
    for line in config_file:
        if key.lower() in line.lower():
            sub_lines = line.split("=")
            return sub_lines[1].strip()
    config_file.close()
    return f'"{key}" not found in {file}'
