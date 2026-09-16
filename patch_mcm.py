import sys

file_path = r'res/pex/Source/Scripts/QuickLootIEMCM.psc'
with open(file_path, 'r') as f:
    content = f.read()

content = content.replace(
    'bool property QLIE_ShowWhenMounted = false auto hidden',
    'bool property QLIE_ShowWhenMounted = false auto hidden\n'
    'bool property QLIE_ShowWhenWerewolf = true auto hidden\n'
    'bool property QLIE_ShowWhenVampireLord = true auto hidden'
)

content = content.replace(
    'AddTextOptionST("state_ShowWhenMounted",\t\t"",\t\tGetEnabledStatusText(QLIE_ShowWhenMounted))',
    'AddTextOptionST("state_ShowWhenMounted",\t\t"",\t\tGetEnabledStatusText(QLIE_ShowWhenMounted))\n'
    '\tAddTextOptionST("state_ShowWhenWerewolf",\t\t"",\tGetEnabledStatusText(QLIE_ShowWhenWerewolf))\n'
    '\tAddTextOptionST("state_ShowWhenVampireLord",\t"",\tGetEnabledStatusText(QLIE_ShowWhenVampireLord))'
)

state_block = '''state state_ShowWhenMounted
	event OnSelectST()
		QLIE_ShowWhenMounted = !QLIE_ShowWhenMounted
		SetTextOptionValueST(GetEnabledStatusText(QLIE_ShowWhenMounted))
	endevent

	event OnDefaultST()
		QLIE_ShowWhenMounted = false
		SetTextOptionValueST(GetEnabledStatusText(QLIE_ShowWhenMounted))
	endevent
endstate'''

new_state_blocks = state_block + '''

state state_ShowWhenWerewolf
	event OnSelectST()
		QLIE_ShowWhenWerewolf = !QLIE_ShowWhenWerewolf
		SetTextOptionValueST(GetEnabledStatusText(QLIE_ShowWhenWerewolf))
	endevent

	event OnDefaultST()
		QLIE_ShowWhenWerewolf = true
		SetTextOptionValueST(GetEnabledStatusText(QLIE_ShowWhenWerewolf))
	endevent
endstate

state state_ShowWhenVampireLord
	event OnSelectST()
		QLIE_ShowWhenVampireLord = !QLIE_ShowWhenVampireLord
		SetTextOptionValueST(GetEnabledStatusText(QLIE_ShowWhenVampireLord))
	endevent

	event OnDefaultST()
		QLIE_ShowWhenVampireLord = true
		SetTextOptionValueST(GetEnabledStatusText(QLIE_ShowWhenVampireLord))
	endevent
endstate'''

content = content.replace(state_block, new_state_blocks)

content = content.replace(
    'QLIE_ShowWhenMounted = false',
    'QLIE_ShowWhenMounted = false\n\tQLIE_ShowWhenWerewolf = true\n\tQLIE_ShowWhenVampireLord = true'
)

content = content.replace(
    'JsonUtil.SetPathIntValue(path, "ShowWhenMounted", QLIE_ShowWhenMounted as int)',
    'JsonUtil.SetPathIntValue(path, "ShowWhenMounted", QLIE_ShowWhenMounted as int)\n'
    '\tJsonUtil.SetPathIntValue(path, "ShowWhenWerewolf", QLIE_ShowWhenWerewolf as int)\n'
    '\tJsonUtil.SetPathIntValue(path, "ShowWhenVampireLord", QLIE_ShowWhenVampireLord as int)'
)

content = content.replace(
    'QLIE_ShowWhenMounted = JsonUtil.GetPathIntValue(path, "ShowWhenMounted", QLIE_ShowWhenMounted as int)',
    'QLIE_ShowWhenMounted = JsonUtil.GetPathIntValue(path, "ShowWhenMounted", QLIE_ShowWhenMounted as int)\n'
    '\tQLIE_ShowWhenWerewolf = JsonUtil.GetPathIntValue(path, "ShowWhenWerewolf", QLIE_ShowWhenWerewolf as int)\n'
    '\tQLIE_ShowWhenVampireLord = JsonUtil.GetPathIntValue(path, "ShowWhenVampireLord", QLIE_ShowWhenVampireLord as int)'
)

with open(file_path, 'w') as f:
    f.write(content)

print("Python script finished successfully.")
