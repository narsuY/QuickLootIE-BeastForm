import re
file_path = r'res/pex/Source/Scripts/QuickLootIEMCM.psc'
with open(file_path, 'r') as f:
    content = f.read()

# Replace SetTextOptionValueST(something) with SetTextOptionValueST(something, false, "")
# Need to make sure it doesn't already have false
content = re.sub(r'(SetTextOptionValueST\([^,]+?\))', lambda m: m.group(1)[:-1] + ', false, "")', content)

# Do the same for SetSliderOptionValueST, SetMenuOptionValueST, SetKeyMapOptionValueST, etc.
content = re.sub(r'(SetSliderOptionValueST\([^,]+?\))', lambda m: m.group(1)[:-1] + ', "{0}", false, "")', content)
content = re.sub(r'(SetMenuOptionValueST\([^,]+?\))', lambda m: m.group(1)[:-1] + ', false, "")', content)
content = re.sub(r'(SetKeyMapOptionValueST\([^,]+?\))', lambda m: m.group(1)[:-1] + ', false, "")', content)

with open(file_path, 'w') as f:
    f.write(content)
print("Patched all calls in QuickLootIEMCM.psc")
