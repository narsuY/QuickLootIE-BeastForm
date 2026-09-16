import re

file_path = r'res/pex/Source/Scripts/QuickLootIEMCM.psc'
with open(file_path, 'r') as f:
    lines = f.readlines()

def patch_line(line):
    # Match the function call and everything inside the outer parentheses
    match = re.search(r'(Set(Text|Slider|Menu|KeyMap)OptionValueST)\s*\((.*)\)', line)
    if not match:
        return line
        
    func = match.group(1)
    args_str = match.group(3)
    
    # Very basic argument counting (assumes no complex nested commas outside of GetEnabledStatusText etc)
    # Actually, a simpler way: just check if 'false' or '""' is already in the args.
    if ', false' in args_str.lower() or ', ""' in args_str:
        return line # Already patched
        
    if func == 'SetSliderOptionValueST':
        # Needs value, format string, noUpdate, stateName
        return line.replace(f'({args_str})', f'({args_str}, "{0}", false, "")')
    else:
        # Needs value, noUpdate, stateName
        return line.replace(f'({args_str})', f'({args_str}, false, "")')

new_lines = [patch_line(l) for l in lines]

with open(file_path, 'w') as f:
    f.writelines(new_lines)

print("Robust patch applied.")
