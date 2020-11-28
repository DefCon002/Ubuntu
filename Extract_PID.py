# Scratch
import re
log = "hi this is test numbers [12435]"
def extract_PID(log_line):
    regex = r'\[(\d+)\]'
    result = re.search(regex,log_line)
    if result is None:
        return ""
    return result[1]
print(extract_PID(log))