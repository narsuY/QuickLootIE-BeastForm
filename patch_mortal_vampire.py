import re

with open('src/MenuVisibilityManager.cpp', 'r') as f:
    content = f.read()

# We want to add the vampire check right after the IsDead check
replacement = '''			if (!actor->IsDead()) {
				logger::debug("LootMenu disabled because the actor isn't dead");
				return false;
			}

			// Support for Mortal Vampire / Cannibal corpse feeding
			if (Config::UserSettings::RequireCtrlInBeastForm()) {
				bool isVampire = player->HasKeywordString("Vampire");
				if (isVampire && !RE::MenuControls::GetSingleton()->InBeastForm()) {
					bool isCtrlHeld = (GetAsyncKeyState(VK_CONTROL) & 0x8000) != 0;
					if (!isCtrlHeld) {
						logger::debug("LootMenu disabled for Mortal Vampire on corpse (CTRL not held)");
						return false;
					}
				}
			}'''

content = content.replace('''			if (!actor->IsDead()) {
				logger::debug("LootMenu disabled because the actor isn't dead");
				return false;
			}''', replacement)

with open('src/MenuVisibilityManager.cpp', 'w') as f:
    f.write(content)

print("Mortal vampire patch applied.")
