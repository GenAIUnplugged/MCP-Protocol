import PyPDF2
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("PDFReaderServer")

@mcp.tool()
def read_pdf_text(query: str) -> str:
    """
    Fetch the contents from the Attention is All You Need pdf for the transformer model queries.    
    :param pdf_path: User Query.
    :return: Extracted text as a string along with the query.
    """
    pdf_path = "C:\\Youtube\\MCPProtocol\\Code\\MCP_Demo_2\\NIPS-2017-attention-is-all-you-need-Paper.pdf"
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
                if text:
                    text += "\n"  # Add a newline after each page's text
            return (
                f"Using the fetched text from the PDF file:\n{pdf_path}\n\n"
                f"Content:\n{text}\n",
                f"Query:{query}",
                f"Please answer based on the content above."
            )
    except FileNotFoundError:
        return f"File not found: {pdf_path}"
    except Exception as e:
        return f"An error occurred: {e}"
    
@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return "App configuration here"

if __name__ == "__main__":
    mcp.run(transport="stdio")