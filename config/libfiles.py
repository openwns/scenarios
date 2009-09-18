libname = 'scenarios'

srcFiles = [
    ]

hppFiles = [
    ]

pyconfigs = [
    'scenarios/__init__.py',
    'scenarios/interfaces.py',
    'scenarios/placer/__init__.py',
    'scenarios/placer/hexagonal.py',
    'scenarios/placer/circular.py',
    'scenarios/builders/__init__.py',
    'scenarios/builders/creatorplacer.py',
    'scenarios/traffic/__init__.py',
    'scenarios/simple/__init__.py',
    'scenarios/simple/singlecell.py',
    'scenarios/toolsupport/__init__.py',
    'scenarios/toolsupport/pytreevisitors/__init__.py',
    'scenarios/toolsupport/pytreevisitors/builders/__init__.py',
    'scenarios/toolsupport/pytreevisitors/builders/creatorplacer.py',
]

dependencies = []
# Put in any external lib here as you would pass it to a -l compiler flag, e.g.
# dependencies = ['boost_date_time']
Return('libname srcFiles hppFiles pyconfigs dependencies')
