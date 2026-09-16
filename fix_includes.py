with open('src/Input/InputManager.cpp', 'r') as f: content = f.read()
content = content.replace('#include "Input/InputManager.h"', '#include "Input/InputManager.h"\n#include "MenuVisibilityManager.h"')
with open('src/Input/InputManager.cpp', 'w') as f: f.write(content)
