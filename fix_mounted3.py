import re
file_path = 'res/pex/Source/Scripts/QuickLootIEMCM.psc'
with open(file_path, 'r') as f:
    content = f.read()

content = re.sub(
    r'AddTextOptionST\("state_ShowWhenMounted",\s*"",\s*GetEnabledStatusText\(QLIE_ShowWhenMounted\)\)',
    'AddTextOptionST("state_ShowWhenMounted", "$qlie_ShowWhenMounted_text", GetEnabledStatusText(QLIE_ShowWhenMounted))',
    content
)

with open(file_path, 'w') as f:
    f.write(content)
print("Mounted fix applied securely!")
