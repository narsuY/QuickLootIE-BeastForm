import re

file_path = 'res/pex/Source/Scripts/QuickLootIEMCM.psc'
with open(file_path, 'r') as f:
    content = f.read()

draw_patch = '''	AddTextOptionST("state_ShowWhenMounted",		"",		GetEnabledStatusText(QLIE_ShowWhenMounted))
	AddTextOptionST("state_ShowWhenWerewolf",		"Show when in Werewolf form",		GetEnabledStatusText(QLIE_ShowWhenWerewolf))
	AddTextOptionST("state_ShowWhenVampireLord",		"Show when in Vampire Lord form",		GetEnabledStatusText(QLIE_ShowWhenVampireLord))
	AddTextOptionST("state_RequireCtrlInBeastForm",		"Require CTRL to feed as Vampire",		GetEnabledStatusText(QLIE_RequireCtrlInBeastForm))'''

if 'Show when in Werewolf form' not in content:
    content = re.sub(r'AddTextOptionST\("state_ShowWhenMounted",.*?GetEnabledStatusText\(QLIE_ShowWhenMounted\)\)', draw_patch, content)

with open(file_path, 'w') as f:
    f.write(content)
print("Patch applied for drawing UI!")
