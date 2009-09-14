libname = 'scenarios'

srcFiles = [
    'src/scenariosModule.cpp',
    'src/SimulationModel.cpp',
    ]

hppFiles = [
    'src/scenariosModule.hpp',
    'src/SimulationModel.hpp',
    ]

pyconfigs = [
    'scenarios/__init__.py',
    'scenarios/simulationmodel.py',
]

dependencies = []
# Put in any external lib here as you would pass it to a -l compiler flag, e.g.
# dependencies = ['boost_date_time']
Return('libname srcFiles hppFiles pyconfigs dependencies')
