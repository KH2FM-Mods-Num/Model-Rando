import sys
import os
import yaml
import random

#Functions to write stuff
def writemodel(old,new):
    old = 'obj/' + old
    new = 'obj/' + new
    #A.FM
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
        oldmodels = models['Base'] + models['ExtraDomain']
        newmodels = models['Base'] + models['ExtraCodomain']
        while len(oldmodels) >= len(newmodels):
            newmodels += (models['Base'] + models['ExtraCodomain'])
        random.shuffle(newmodels)
        for i in range(len(oldmodels)):
            if oldmodels[i] == newmodels[i]:
                pass
            writemodel(oldmodels[i],newmodels[i])

f.close()
