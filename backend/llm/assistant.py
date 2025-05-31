import os
from llm.functions.function_manager import FunctionFactory

class Assistant:
    def __init__(self, instructions_path: str):
        with open(instructions_path, 'r') as f:
            self.system_prompt = f.read()

    def get_system_prompt(self, params=None):
        # Optionally fill params if needed
        if params:
            return self.system_prompt.format(**params)
        return self.system_prompt

    def get_function_definitions(self):
        # Gather all function definitions from FunctionFactory
        return [fn.get_props().get("function") for fn in FunctionFactory._registry.values()] 