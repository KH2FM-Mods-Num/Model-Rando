OnPC = False
PCBlacklist = {'Roxas/Coat/P_EX100_XM_BTLF'}

import sys
import os
import yaml
import random

#Functions to write stuff
def writemodel(old,new):
    old = 'obj/' + old
    new = 'obj/' + new
    #A.FM
    if not OnPC: #Don't edit on PC due to a.us pax being remastered-reliant
        if os.path.isfile(new+'.a.fm'):
            f.write('- name: '+old+'.a.fm\n')
            f.write('  method: copy\n')
            f.write('  source:\n')
            f.write('  - name: '+new+'.a.fm\n')
        elif os.path.isfile(new+'.imd') or os.path.isfile(new+'.sqd'):
            f.write('- name: '+old+'.a.fm\n')
            f.write('  method: binarc\n')
            f.write('  source:\n')
            if os.path.isfile(new+'.imd'):
                f.write('  - name: face\n')
                f.write('    type: imgd\n')
                f.write('    method: copy\n')
                f.write('    source:\n')
                f.write('    - name: '+new+'.imd\n')
            if os.path.isfile(new+'.sqd'):
                f.write('  - name: face\n')
                f.write('    type: seqd\n')
                f.write('    method: copy\n')
                f.write('    source:\n')
                f.write('    - name: '+new+'.sqd\n')
    #MDLX
    if os.path.isfile(new+'.model') or os.path.isfile(new+'.tim'):
        f.write('- name: '+old+'.mdlx\n')
        f.write('  method: binarc\n')
        f.write('  source:\n')
        if os.path.isfile(new+'.model'):
            subfile = old[4:8].lower()
            if '_PLAYER' in old:
                subfile = 'p_ex'
            f.write('  - name: '+subfile+'\n')
            f.write('    type: model\n')
            f.write('    method: copy\n')
            f.write('    source:\n')
            f.write('    - name: '+new+'.model\n')
        if os.path.isfile(new+'.tim'):
            f.write('  - name: tim_\n')
            f.write('    type: modeltexture\n')
            f.write('    method: copy\n')
            f.write('    source:\n')
            f.write('    - name: '+new+'.tim\n')

#Get KH2 model filenames
currentDir = sys.argv[0].replace((sys.argv[0].split('\\')[-1]),'')
objs = yaml.safe_load(open(currentDir+'modellist.yml'))

#Write the mod.yml
f = open(currentDir+'mod.yml','w',encoding='utf-8')
f.write('description: Credits for PandaPyre, Shananas, GeminiHero, and DA for providing their respective textures.\n')
f.write('assets:\n')
for objtype in objs:
    obj = objs[objtype]
    for models in obj.values():
        Base          = models['Base']
        ExtraDomain   = models['ExtraDomain']
        ExtraCodomain = models['ExtraCodomain']
        #Remove blacklisted models
        if OnPC:
            Base          = [x for x in Base          if not x in PCBlacklist]
            ExtraDomain   = [x for x in ExtraDomain   if not x in PCBlacklist]
            ExtraCodomain = [x for x in ExtraCodomain if not x in PCBlacklist]
        #Get eligible elements
        oldmodels = Base + ExtraDomain
        newmodels = Base + ExtraCodomain
        while len(oldmodels) >= len(newmodels):
            newmodels += (Base + ExtraCodomain)
        random.shuffle(newmodels)
        for i in range(len(oldmodels)):
            if oldmodels[i] == newmodels[i]:
                pass
            writemodel(oldmodels[i],newmodels[i])

f.close()
