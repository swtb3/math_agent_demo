from transformers import Tool


class SquareTool(Tool):
    
    name = "square_tool"
    description = (
        "This tool Squares the given input number like A*A =A^2."
        "Alternative formats for squaring are A**2, A(A), A^2, A*A"
        "It returns the result of the Squaring Operation"
    )

    inputs = {
        "number_to_square": {
            "type": "number",
            "description": "The number that we intend to square",
        },
    }
    output_type = "number"
    
    def forward(self, inputs):
        x = inputs["number_to_square"]
        return x * x