lineup = {
    'pg': 'Coby White',
    'sg': 'Zach LaVine',
    'sf': 'Otto Porter',
    'pf': 'Lauri Markkanen',
    'c': 'Wendell Carter',
}

bulls = ('Chicago', 'Bulls', 'Eastern')

def print_info(city, name, conference):
    print(f'The {city} {name} play in the {conference} conference')

# absorb the addtional keyword agruments with **kwargs
def print_backcourt(pg, sg, **kwargs):
    print(pg, 'and', sg)

# unpacks the lineup dict as keyword arguments matchs to function arguments
print_backcourt(**lineup)
print_info(*bulls)
