# server.py
class ToolServer:
    def __init__(self):
        print("ToolServer initialized")
def tool(func):
    func.is_tool = True  # Optional flag to detect tools
    return func
