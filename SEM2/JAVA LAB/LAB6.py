def groupAndSortOwners(files):
    result = {}

    for file, owner in files.items():
        if owner not in result:
            result[owner] = []
        result[owner].append(file)

    # sort filenames for each owner
    for owner in result:
        result[owner].sort()

    return result


files = {
    'Input.txt': 'Albert',
    'Code.py': 'Stanley',
    'Output.txt': 'Albert',
    'btech.txt': 'Albert'
}

print(groupAndSortOwners(files))
