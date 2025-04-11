class GoogleGenerativeAIAgent:
    def __init__(self, name, auto_run, tools=None, instructions=""):
        self.name = name
        self.auto_run = auto_run
        self.instructions = instructions
        self.tools = tools or []

    def run_task(self, task):
        print(f"[Agent: {self.name}] Running task: {task.description}")

        print("Following instructions:", self.instructions)

        for tool in self.tools:
            if tool.__name__ == "open_paint":
                tool()
            elif tool.__name__ == "draw_rectangle":
                tool()
            elif tool.__name__ == "add_text_in_paint":
                tool("130")  # Hardcoded for testing
