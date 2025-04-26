# Import the FastMCP library
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("GreetingsServer")

@mcp.tool()
def greets(name: str) -> str:
    """
    Responds with a personalized greeting when the user says 'hi', 'hello', or any other greeting.

    This tool should be called when the user initiates a conversation with a greeting 
    such as "Hi", "Hello", "Hey", "Good morning", "Good evening", or similar phrases.
    
    Parameters:
    - name (str): The name of the person to greet.

    Returns:
    - A friendly greeting message including the person's name.

    Example usage:
    - Input: name = "John"
    - Output: "Hello, John! How are you today?"

    Ideal when the conversation starts or when the user expects a warm, friendly reply.
    """
    return f"Hello, {name}! How are you today?"

if __name__ == "__main__":
    mcp.run(transport="stdio")

  