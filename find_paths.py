import os
base = 'G:/[ ARR ]/mods'
dirs = [
    'C:/Users/User/.gemini/antigravity/scratch/skyui/dist/Data/Scripts/Source',
]
keywords = ['PapyrusUtil AE', 'JContainers', 'Papyrus Extender', 'SKSE', 'Vanilla Scripts']
for kw in keywords:
    for f in os.listdir(base):
        if kw in f and '[NoDelete]' not in f and 'Scrab' not in f:
            src1 = os.path.join(base, f, 'Scripts', 'Source')
            src2 = os.path.join(base, f, 'scripts', 'source')
            src3 = os.path.join(base, f, 'Source', 'Scripts')
            if os.path.exists(src1): dirs.append(src1.replace('/', '\\\\'))
            elif os.path.exists(src2): dirs.append(src2.replace('/', '\\\\'))
            elif os.path.exists(src3): dirs.append(src3.replace('/', '\\\\'))
            break
print(';'.join(dirs))
