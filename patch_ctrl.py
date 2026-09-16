import re

# 1. Papyrus.h
with open('src/Config/Papyrus.h', 'r') as f: content = f.read()
if 'bool QLIE_RequireCtrlInBeastForm;' not in content:
    content = content.replace('extern bool QLIE_ShowWhenVampireLord;', 'extern bool QLIE_ShowWhenVampireLord;\n\t\textern bool QLIE_RequireCtrlInBeastForm;')
    with open('src/Config/Papyrus.h', 'w') as f: f.write(content)

# 2. Papyrus.cpp
with open('src/Config/Papyrus.cpp', 'r') as f: content = f.read()
if 'bool QLIE_RequireCtrlInBeastForm = true;' not in content:
    content = content.replace('bool QLIE_ShowWhenVampireLord = true;', 'bool QLIE_ShowWhenVampireLord = true;\n\tbool QLIE_RequireCtrlInBeastForm = true;')
    content = content.replace('LoadSettingsVar(QLIE_ShowWhenVampireLord, true);', 'LoadSettingsVar(QLIE_ShowWhenVampireLord, true);\n\t\t\tLoadSettingsVar(QLIE_RequireCtrlInBeastForm, true);')
    with open('src/Config/Papyrus.cpp', 'w') as f: f.write(content)

# 3. UserSettings.h
with open('src/Config/UserSettings.h', 'r') as f: content = f.read()
if 'bool RequireCtrlInBeastForm();' not in content:
    content = content.replace('static bool ShowWhenVampireLord();', 'static bool ShowWhenVampireLord();\n\t\tstatic bool RequireCtrlInBeastForm();')
    with open('src/Config/UserSettings.h', 'w') as f: f.write(content)

# 4. UserSettings.cpp
with open('src/Config/UserSettings.cpp', 'r') as f: content = f.read()
if 'RequireCtrlInBeastForm()' not in content:
    content = content.replace('bool UserSettings::ShowWhenVampireLord() { return Papyrus::QLIE_ShowWhenVampireLord; }', 'bool UserSettings::ShowWhenVampireLord() { return Papyrus::QLIE_ShowWhenVampireLord; }\n\tbool UserSettings::RequireCtrlInBeastForm() { return Papyrus::QLIE_RequireCtrlInBeastForm; }')
    with open('src/Config/UserSettings.cpp', 'w') as f: f.write(content)

# 5. MenuVisibilityManager.cpp
with open('src/MenuVisibilityManager.cpp', 'r') as f: content = f.read()
if 'RequireCtrlInBeastForm' not in content:
    replacement = '''if (!isVampireLord && !Config::UserSettings::ShowWhenWerewolf()) {
				logger::debug("LootMenu disabled because player is in Werewolf form");
				return false;
			}
            
            if (Config::UserSettings::RequireCtrlInBeastForm()) {
                auto deviceManager = RE::BSInputDeviceManager::GetSingleton();
                auto keyboard = deviceManager ? deviceManager->GetKeyboard() : nullptr;
                bool isCtrlHeld = keyboard && (keyboard->IsPressed(29) || keyboard->IsPressed(157)); // Left/Right CTRL
                if (!isCtrlHeld) {
                    logger::debug("LootMenu disabled because CTRL is not held in beast form");
                    return false;
                }
            }'''
    content = content.replace('''if (!isVampireLord && !Config::UserSettings::ShowWhenWerewolf()) {
				logger::debug("LootMenu disabled because player is in Werewolf form");
				return false;
			}''', replacement)
    with open('src/MenuVisibilityManager.cpp', 'w') as f: f.write(content)

# 6. InputManager.cpp
with open('src/Input/InputManager.cpp', 'r') as f: content = f.read()
if 'MenuVisibilityManager.h' not in content:
    content = content.replace('#include "Config/UserSettings.h"', '#include "Config/UserSettings.h"\n#include "MenuVisibilityManager.h"')
if 'keyCode == 29' not in content:
    replacement_event = '''const auto eventKey = NormalizeDeviceKey(event->GetDevice(), event->GetIDCode());
    
        if (eventKey.deviceType == DeviceType::kKeyboard && (eventKey.keyCode == 29 || eventKey.keyCode == 157)) {
            QuickLoot::MenuVisibilityManager::RefreshOpenState();
        }'''
    content = content.replace('const auto eventKey = NormalizeDeviceKey(event->GetDevice(), event->GetIDCode());', replacement_event)
    with open('src/Input/InputManager.cpp', 'w') as f: f.write(content)

print("Patch applied successfully.")
