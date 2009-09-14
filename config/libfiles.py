libname = 'scenarios'

srcFiles = [
    ]

hppFiles = [
    ]

pyconfigs = [
    'scenarios/__init__.py',
]

dependencies = []
# Put in any external lib here as you would pass it to a -l compiler flag, e.g.
# dependencies = ['boost_date_time']
Return('libname srcFiles hppFiles pyconfigs dependencies')
