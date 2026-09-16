import re

file_path = r'C:\Users\User\.gemini\antigravity\scratch\skyui\dist\Data\Scripts\Source\SKI_ConfigBase.psc'
with open(file_path, 'r') as f:
    content = f.read()

stub = '''
function AddInputOptionST(String a_stateName, String a_text, String a_value, Int a_flags = 0)
endFunction

Int function AddInputOption(String a_text, String a_value, Int a_flags = 0)
    return -1
endFunction

function SetInputOptionValueST(String a_value, Bool a_noUpdate = false, String a_stateName = "")
endFunction

function SetInputDialogStartText(String a_text)
endFunction
'''

if 'AddInputOptionST' not in content:
    content += "\n" + stub

with open(file_path, 'w') as f:
    f.write(content)
print("Stubbed AddInputOptionST in clean SkyUI")
