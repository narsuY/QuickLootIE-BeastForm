import re

# 1. Rename 'message' to 'a_message' in QuickLootIEMCM.psc
file_path = r'res/pex/Source/Scripts/QuickLootIEMCM.psc'
with open(file_path, 'r') as f:
    content = f.read()

content = content.replace('function ShowMsg(string message)', 'function ShowMsg(string a_message)')
content = content.replace('ShowMessage(message, false', 'ShowMessage(a_message, false')

with open(file_path, 'w') as f:
    f.write(content)


# 2. Add empty state events to clean SkyUI
skyui_path = r'C:\Users\User\.gemini\antigravity\scratch\skyui\dist\Data\Scripts\Source\SKI_ConfigBase.psc'
with open(skyui_path, 'r') as f:
    skyui_content = f.read()

stubs = '''
event OnInputOpenST()
endEvent

event OnInputAcceptST(string a_input)
endEvent
'''

if 'OnInputOpenST' not in skyui_content:
    skyui_content += "\n" + stubs

with open(skyui_path, 'w') as f:
    f.write(skyui_content)

print("Syntax fixed!")
