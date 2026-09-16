import re

file_path = 'res/pex/Source/Scripts/QuickLootIEMCM.psc'
with open(file_path, 'r') as f:
    content = f.read()

# Fix the AddTextOptionST strings
draw_patch = '''	AddTextOptionST("state_ShowWhenMounted",		"",		GetEnabledStatusText(QLIE_ShowWhenMounted))
	AddTextOptionST("state_ShowWhenWerewolf",		"Show when in Werewolf form",		GetEnabledStatusText(QLIE_ShowWhenWerewolf))
	AddTextOptionST("state_ShowWhenVampireLord",		"Show when in Vampire Lord form",		GetEnabledStatusText(QLIE_ShowWhenVampireLord))
	AddTextOptionST("state_RequireCtrlInBeastForm",		"Require CTRL to loot (Beasts/Vampires)",		GetEnabledStatusText(QLIE_RequireCtrlInBeastForm))'''

content = re.sub(r'AddTextOptionST\("state_ShowWhenMounted".*?AddTextOptionST\("state_RequireCtrlInBeastForm"[^\n]*\n', draw_patch + '\n', content, flags=re.DOTALL)

# Now fix the states to include OnHighlightST
states_patch = '''state state_ShowWhenWerewolf
	event OnSelectST()
		QLIE_ShowWhenWerewolf = !QLIE_ShowWhenWerewolf
		SetTextOptionValueST(GetEnabledStatusText(QLIE_ShowWhenWerewolf))
	endevent

	event OnDefaultST()
		QLIE_ShowWhenWerewolf = true
		SetTextOptionValueST(GetEnabledStatusText(QLIE_ShowWhenWerewolf))
	endevent

	event OnHighlightST()
		SetInfoText("Whether the loot menu opens while in Werewolf form. Default: Enabled")
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

	event OnHighlightST()
		SetInfoText("Whether the loot menu opens while in Vampire Lord form. Default: Enabled")
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

	event OnHighlightST()
		SetInfoText("If enabled, you must hold CTRL to see the loot menu in Beast Form, or as a Mortal Vampire looking at a corpse. This prevents QuickLoot from blocking your vanilla Feed options. Default: Enabled")
	endevent
endstate'''

content = re.sub(r'state state_ShowWhenWerewolf.*?endstate\n\nstate state_ShowWhenVampireLord.*?endstate\n\nstate state_RequireCtrlInBeastForm.*?endstate', states_patch, content, flags=re.DOTALL)

with open(file_path, 'w') as f:
    f.write(content)
print("Patch applied for fixing missing texts and descriptions!")
