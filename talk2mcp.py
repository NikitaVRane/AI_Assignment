import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from mcp.agents.google_genai_agent import GoogleGenerativeAIAgent
from mcp.tasks import Task
from mcp.tools.paint_tools import open_paint, draw_rectangle, add_text_in_paint

agent = GoogleGenerativeAIAgent(
    name="PaintBot",
    auto_run=True,
    tools=[open_paint, draw_rectangle, add_text_in_paint],
    instructions="""
    You are an autonomous agent that solves math problems and renders the result visually in MS Paint.
    
    Steps:
    1. Use `open_paint()` to open Paint.
    2. Use `draw_rectangle()` to draw a box.
    3. Use `add_text_in_paint(text)` to write the answer inside that box.
    Always follow these steps. Assume Paint is closed when starting.
    """
)

task = Task("What is 52 + 78? Show the result in a rectangle inside Paint.")
agent.run_task(task)
