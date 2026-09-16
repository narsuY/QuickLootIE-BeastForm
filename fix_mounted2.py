file_path = 'res/pex/Source/Scripts/QuickLootIEMCM.psc'
with open(file_path, 'r') as f:
    content = f.read()

# Replace any variant of the empty mounted string
import re
content = re.sub(
    r'AddTextOptionST\("state_ShowWhenMounted",\s*"",\s*GetEnabledStatusText\(QLIE_ShowWhenMounted\)\)',
    'AddTextOptionST("state_ShowWhenMounted", "", GetEnabledStatusText(QLIE_ShowWhenMounted))',
    content
)
# Just in case there are unseen chars
content = content.replace('AddTextOptionST("state_ShowWhenMounted", "", GetEnabledStatusText(QLIE_ShowWhenMounted))', 'AddTextOptionST("state_ShowWhenMounted", "", GetEnabledStatusText(QLIE_ShowWhenMounted))')
content = content.replace('AddTextOptionST("state_ShowWhenMounted",		"",		GetEnabledStatusText(QLIE_ShowWhenMounted))', 'AddTextOptionST("state_ShowWhenMounted", "", GetEnabledStatusText(QLIE_ShowWhenMounted))')

with open(file_path, 'w') as f:
    f.write(content)
print("Mounted fix applied!")
