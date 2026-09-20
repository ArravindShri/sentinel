with open('data/20260919034500.export.CSV','r') as f:
    file_split=f.readline()
    parts=file_split.split('\t')
    print(parts[53])
    print(parts[56])
    print(parts[60])