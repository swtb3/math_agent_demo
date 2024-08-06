from transformers import Tool


class DivisionTool(Tool):
    
    name = "division_tool"
    description = (
        "This tool performs a simple division between two Real numbers like: x / y = z"
        "It returns the result of the division operation"
    )

    inputs = {
        "x": {
            "type": "float",
            "description": "The number on the left side of the / operator",
        },
        "y": {
            "type": "float",
            "description": "The number on the right side of the / operator",
        }
    }
    output_type = "float"
    
    def forward(self, x: float, y: float) -> float:
        
        if not x:
            raise Exception("You must provide a value for x")
        if not y:
            raise Exception("You must provide a value for y")
        
        return x / y