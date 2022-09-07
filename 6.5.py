rivers = {'germany': 'rhine', 'egypt': 'nile', 'denmark': 'suså'}
for stuff in rivers.keys():
    print('The ' + rivers[stuff].title() + ' is in ' + stuff.title())
for c in rivers.keys():
    print(c.title())
for r in rivers.values():
    print(r.title())
