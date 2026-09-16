import re

file_path = r'res/pex/Source/Scripts/SKI_ConfigBase.psc'
with open(file_path, 'r') as f:
    content = f.read()

def add_defaults(content, func_name, has_format=False):
    # E.g. function SetTextOptionValueST(String a_value, Bool a_noUpdate, String a_stateName)
    # The regex looks for function \s+ SetTextOptionValueST \s* \( ... \)
    pattern = r'(function\s+' + func_name + r'\s*\([^)]*?Bool\s+a_noUpdate[^,]*?,\s*String\s+a_stateName[^\)]*?\))'
    
    def repl(m):
        sig = m.group(1)
        # Add defaults if they are missing
        if 'a_noUpdate = false' not in sig:
            sig = re.sub(r'(Bool\s+a_noUpdate)(?!\s*=)', r'\1 = false', sig)
        if 'a_stateName = ""' not in sig:
            sig = re.sub(r'(String\s+a_stateName)(?!\s*=)', r'\1 = ""', sig)
        if has_format and 'a_formatString = "{0}"' not in sig:
            sig = re.sub(r'(String\s+a_formatString)(?!\s*=)', r'\1 = "{0}"', sig)
        return sig

    return re.sub(pattern, repl, content, flags=re.IGNORECASE)

content = add_defaults(content, 'SetTextOptionValueST')
content = add_defaults(content, 'SetToggleOptionValueST')
content = add_defaults(content, 'SetSliderOptionValueST', has_format=True)
content = add_defaults(content, 'SetMenuOptionValueST')
content = add_defaults(content, 'SetColorOptionValueST')
content = add_defaults(content, 'SetKeyMapOptionValueST')
content = add_defaults(content, 'SetInputOptionValueST')

# Also fix the Add*OptionST ones if they are missing flags = 0
def add_flags(content, func_name):
    pattern = r'(function\s+' + func_name + r'\s*\([^)]*?Int\s+a_flags[^\)]*?\))'
    def repl(m):
        sig = m.group(1)
        if 'a_flags = 0' not in sig:
            sig = re.sub(r'(Int\s+a_flags)(?!\s*=)', r'\1 = 0', sig)
        return sig
    return re.sub(pattern, repl, content, flags=re.IGNORECASE)

content = add_flags(content, 'AddTextOptionST')
content = add_flags(content, 'AddToggleOptionST')
content = add_flags(content, 'AddSliderOptionST')
content = add_flags(content, 'AddMenuOptionST')
content = add_flags(content, 'AddColorOptionST')
content = add_flags(content, 'AddKeyMapOptionST')
content = add_flags(content, 'AddInputOptionST')

# Also empty state functions need it (they might have been defined as empty block functions)
content = add_defaults(content, 'SetTextOptionValueST') # run again just in case

with open(file_path, 'w') as f:
    f.write(content)
print("Surgically patched SKI_ConfigBase.psc")
