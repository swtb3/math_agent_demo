from transformers import Tool
import numpy as np

class SquareRootTool(Tool):
    
    name = "square_root_tool"
    description = (
        "This tool calculates the Square Root the given input number like sqrt(A)"
        "It returns the result of the Square Root Operation"
    )

    inputs = {
        "number_to_square_root": {
            "type": "number",
            "description": "The number that we intend to square root",
        },
    }
    output_type = "number"
    
    def forward(self, inputs):
        x = inputs["number_to_square_root"]
        return np.sqrt(x)