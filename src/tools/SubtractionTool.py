from transformers import Tool


class SubtractionTool(Tool):
    
    name = "subtraction_tool"
    description = (
        "This tool performs a simple subtraction between two Real numbers like: x - y = z"
        "It returns the result of the subtraction operation"
    )

    inputs = {
        "x": {
            "type": "number",
            "description": "The number on the left side of the - operator",
        },
        "y": {
            "type": "number",
            "description": "The number on the right side of the - operator",
        }
    }
    output_type = "number"
    
    def forward(self, x: float, y: float) -> float:

        if not x:
            raise Exception("You must provide a value for x")
        if not y:
            raise Exception("You must provide a value for y")
        
        return x - y