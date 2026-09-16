import re

file_path = r'G:\[ ARR ]\mods\Authoria - Papyrus - MCM Recorder Fix\Scripts\Source\SKI_ConfigBase.psc'
with open(file_path, 'r') as f:
    content = f.read()

content = re.sub(r'bool a_noUpdate,\s*string a_stateName', r'bool a_noUpdate = false, string a_stateName = ""', content)
content = re.sub(r'bool a_noUpdate = false,\s*string a_stateName\)', r'bool a_noUpdate = false, string a_stateName = "")', content)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched SKI_ConfigBase")
