import sys
sys.setrecursionlimit(1500)

import openminds
import openminds.latest as om
from pathlib import Path

p = Path('../openMINDS_instances/instances/latest')
c = openminds.Collection()
for folder in (p / 'terminologies').iterdir():
    c.load(str(folder))
c.load(str(p / 'licenses'))
#c.load(str(p / 'contentTypes'))
c.load(str(p / 'commonCoordinateSpaceVersions' / 'BigBrain' / 'BigBrain_2015.jsonld'))
1/0
for folder in (p / 'commonCoordinateSpaceVersions').iterdir():
    print ("working on folder", folder)
    c.load(str(folder))
#c.load(str(p / 'commonCoordinateSpaces'))
