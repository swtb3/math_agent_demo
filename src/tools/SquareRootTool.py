from transformers import Tool
import numpy as np

class SquareRootTool(Tool):
    
    name = "square_root_tool"
    description = (
        "This tool calculates the Square Root the given input number like sqrt(x)"
        "It returns the result of the Square Root Operation"
    )

    inputs = {
        "x": {
            "type": "float",
            "description": "The number that we intend to square root",
        },
    }
    output_type = "float"
    
    def forward(self, x: float) -> float:
        if x < 0:
            raise Exception(f'It is not possible to square root a negative number, call final answer tool now and report this to the user') #unless the user would like to let you hadle Imaginary Numbers
        return np.sqrt(x)