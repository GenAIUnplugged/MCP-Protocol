from mcp.server.fastmcp import FastMCP
import os
from datetime import datetime 

mcp = FastMCP("ConversationSaver")

@mcp.tool()
def save_conversation(conversation: str) -> str:
    """
    Saves a conversation string to a text file in the current working directory.

    This tool takes the entire conversation content as input and creates a 
    timestamped `.txt` file with that content. The file is stored in the
    current working directory in a human-readable format. This is useful for 
    storing transcripts, logs, summaries, or user sessions for future reference.

    Args:
        conversation (str): The complete text of the conversation to be saved.

    Returns:
        str: A message indicating success along with the file path, or an 
        error message if saving failed.
    """
    
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Get current working directory
        current_dir = os.getcwd()

        # Create a 'conversations' folder inside it
        save_folder = os.path.join(current_dir, "conversations")
        os.makedirs(save_folder, exist_ok=True)  # << Automatically create if doesn't exist
        
        filename = os.path.join(save_folder, f"conversation_{timestamp}.txt")
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(conversation)
        
        return f"Conversation saved successfully at: {filename}"
    
    except Exception as e:
        return f"Failed to save conversation: {str(e)}"

if __name__ == "__main__":
    mcp.run()
