from transformers import Tool


class SquareTool(Tool):
    
    name = "square_tool"
    description = (
        "This tool Squares the given input number like x*x =x^2."
        "Alternative formats for squaring are x**2, x(x), x^2, x*x"
        "It returns the result of the Squaring Operation"
    )

    inputs = {
        "x": {
            "type": "float",
            "description": "The number that we intend to square",
        },
    }
    output_type = "float"
    
    def forward(self, x: float):
        return x * x