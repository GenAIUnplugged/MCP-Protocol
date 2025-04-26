from mcp.server.fastmcp import FastMCP
import os
from collections import defaultdict

mcp = FastMCP("FileTypeReportServer")

@mcp.tool()
def file_type_report(directory: str) -> dict:
    "Generates a report of file types and their sizes (in MB) within a folder recursively."
    if not os.path.exists(directory):
        return {"error": "Directory does not exist"}

    file_summary = defaultdict(int)

    for root, dirs, files in os.walk(directory):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            path = os.path.join(root, file)
            try:
                size = os.path.getsize(path)
                file_summary[ext or "NO_EXT"] += size
            except FileNotFoundError:
                continue  # File may have been deleted during scan

    return {ext: round(size / (1024 * 1024), 2) for ext, size in file_summary.items()}

mcp.add_tool(file_type_report)

if __name__ == "__main__":
    mcp.run(transport="stdio")
