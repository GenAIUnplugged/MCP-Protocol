import os
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
current_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(current_dir, f"claude_chat_{timestamp}.txt")
filename = filename.replace("\\", "\\\\")
print(filename)