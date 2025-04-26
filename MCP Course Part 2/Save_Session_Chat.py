from mcp.server.fastmcp import FastMCP
import os
from datetime import datetime

mcp = FastMCP("Session_Chat_To_Memory")

@mcp.tool()
def saveChat(chat: str) -> str:
    """
    Saves the chat to a text file with a timestamp to the current working directory.
    """
    # Get the current working directory
    current_dir = os.path.abspath(os.getcwd())

    # Generate a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(current_dir, f"chat_{timestamp}.txt")
    
    try:
        # Save the chat to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(chat)
    except Exception as e:
        return f"Error saving chat: {str(e)}"
    
    return f"Chat saved to {file_path}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
