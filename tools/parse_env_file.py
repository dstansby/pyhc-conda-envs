fname = 'environment_py311.yml'

with open(fname, 'r') as f:
    lines = f.readlines()

tmp_name = '_tmp.yml'
with open(tmp_name, 'w') as f:
    for line in lines:
        if '=' in line:
            parts = line.split('=')
            if len(parts) == 3 and len(parts[1]):
                # Remove second part of conda version specification
                line = '='.join(line.split('=')[:2]) + '\n'
        f.write(line)
