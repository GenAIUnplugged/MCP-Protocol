from mcp.server.fastmcp import FastMCP
import json # Import json for converting historical data

mcp = FastMCP("Echo", dependencies=["mcp[cli]"])

# --- Existing Tools/Resources ---

@mcp.tool()
def add(a:int,b:int)->int:
    """
    Add two numbers together.
    """
    return a + b

@mcp.resource("greeting://{name}")
def greeting(name:str)->str:
    """
    Greet a user by name.
    Args:
        name (str) : The name of the user to greet.
    Returns:
        str : A greeting message.
    """
    return f"Hello {name}! How is the weather today?"


































