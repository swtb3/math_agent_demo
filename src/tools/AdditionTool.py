from transformers import Tool


class AdditionTool(Tool):
    
    name = "addition_tool"
    description = "A tool that performs simple addition"
    inputs = {
        "x": {
            "type": "float",
            "description": "The number on the left side of the + operator",
        },
        "y": {
            "type": "float",
            "description": "The number on the right side of the + operator",
        }
    }
    output_type = "float"
    
    def forward(self, x: float, y: float) -> float:
        
        if not x:
            raise Exception("You must provide a value for x")
        if not y:
            raise Exception("You must provide a value for y")
            
        return x + y