import re

# Fix UserSettings.cpp
with open('src/Config/UserSettings.cpp', 'r') as f: content = f.read()
if 'RequireCtrlInBeastForm()' not in content:
    content = content.replace('bool UserSettings::ShowWhenVampireLord() { return QLIE_ShowWhenVampireLord; }', 'bool UserSettings::ShowWhenVampireLord() { return QLIE_ShowWhenVampireLord; }\n\tbool UserSettings::RequireCtrlInBeastForm() { return QLIE_RequireCtrlInBeastForm; }')
    with open('src/Config/UserSettings.cpp', 'w') as f: f.write(content)

# Fix MenuVisibilityManager.cpp (Use GetAsyncKeyState)
with open('src/MenuVisibilityManager.cpp', 'r') as f: content = f.read()
content = re.sub(r'auto deviceManager = .*?return false;\n\t\t\t\t}\n\t\t\t}', '''bool isCtrlHeld = (GetAsyncKeyState(VK_CONTROL) & 0x8000) != 0;
                if (!isCtrlHeld) {
                    logger::debug("LootMenu disabled because CTRL is not held in beast form");
                    return false;
                }
            }''', content, flags=re.DOTALL)
if '<Windows.h>' not in content:
    content = '#include <Windows.h>\n' + content
with open('src/MenuVisibilityManager.cpp', 'w') as f: f.write(content)

print('Patched successfully.')
