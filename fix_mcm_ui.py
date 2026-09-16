import re

file_path = 'res/pex/Source/Scripts/QuickLootIEMCM.psc'
with open(file_path, 'r') as f:
    content = f.read()

# 1. Properties
if 'QLIE_RequireCtrlInBeastForm' not in content:
    content = content.replace('bool property QLIE_ShowWhenVampireLord = true auto hidden', 'bool property QLIE_ShowWhenVampireLord = true auto hidden\nbool property QLIE_RequireCtrlInBeastForm = true auto hidden')

# 2. DrawPageDisplay
draw_patch = '''	AddTextOptionST("state_ShowWhenMounted",		"",		GetEnabledStatusText(QLIE_ShowWhenMounted))
	AddTextOptionST("state_ShowWhenWerewolf",		"Show when in Werewolf form",		GetEnabledStatusText(QLIE_ShowWhenWerewolf))
	AddTextOptionST("state_ShowWhenVampireLord",		"Show when in Vampire Lord form",		GetEnabledStatusText(QLIE_ShowWhenVampireLord))
	AddTextOptionST("state_RequireCtrlInBeastForm",		"Require CTRL to feed as Vampire",		GetEnabledStatusText(QLIE_RequireCtrlInBeastForm))'''
if 'Show when in Werewolf form' not in content:
    content = content.replace('AddTextOptionST("state_ShowWhenMounted",\t\t"",\t\tGetEnabledStatusText(QLIE_ShowWhenMounted))', draw_patch)

# 3. States
states_patch = '''state state_ShowWhenVampireLord
	event OnSelectST()
		QLIE_ShowWhenVampireLord = !QLIE_ShowWhenVampireLord
		SetTextOptionValueST(GetEnabledStatusText(QLIE_ShowWhenVampireLord))
	endevent

	event OnDefaultST()
		QLIE_ShowWhenVampireLord = true
		SetTextOptionValueST(GetEnabledStatusText(QLIE_ShowWhenVampireLord))
	endevent
endstate

state state_RequireCtrlInBeastForm
	event OnSelectST()
		QLIE_RequireCtrlInBeastForm = !QLIE_RequireCtrlInBeastForm
		SetTextOptionValueST(GetEnabledStatusText(QLIE_RequireCtrlInBeastForm))
	endevent

	event OnDefaultST()
		QLIE_RequireCtrlInBeastForm = true
		SetTextOptionValueST(GetEnabledStatusText(QLIE_RequireCtrlInBeastForm))
	endevent
endstate'''
if 'state state_RequireCtrlInBeastForm' not in content:
    content = re.sub(r'state state_ShowWhenVampireLord.*?endstate', states_patch, content, flags=re.DOTALL)

# 4. ResetSettings
if 'QLIE_RequireCtrlInBeastForm = true' not in content:
    content = re.sub(r'QLIE_ShowWhenVampireLord = true\s*QLIE_EnableForContainers = true', 'QLIE_ShowWhenVampireLord = true\n\tQLIE_RequireCtrlInBeastForm = true\n\tQLIE_EnableForContainers = true', content)

# 5. Export
if '"RequireCtrlInBeastForm"' not in content:
    content = re.sub(r'JsonUtil.SetPathIntValue\(path, "ShowWhenVampireLord", QLIE_ShowWhenVampireLord as int\)', 'JsonUtil.SetPathIntValue(path, "ShowWhenVampireLord", QLIE_ShowWhenVampireLord as int)\n\tJsonUtil.SetPathIntValue(path, "RequireCtrlInBeastForm", QLIE_RequireCtrlInBeastForm as int)', content)

# 6. Import
if 'JsonUtil.GetPathIntValue(path, "RequireCtrlInBeastForm"' not in content:
    content = re.sub(r'QLIE_ShowWhenVampireLord = JsonUtil.GetPathIntValue\(path, "ShowWhenVampireLord", QLIE_ShowWhenVampireLord as int\)', 'QLIE_ShowWhenVampireLord = JsonUtil.GetPathIntValue(path, "ShowWhenVampireLord", QLIE_ShowWhenVampireLord as int)\n\tQLIE_RequireCtrlInBeastForm = JsonUtil.GetPathIntValue(path, "RequireCtrlInBeastForm", QLIE_RequireCtrlInBeastForm as int)', content)

with open(file_path, 'w') as f:
    f.write(content)
print("Patch applied for drawing UI!")
