from transformers import Tool


class MultiplicationTool(Tool):
    
    name = "mulitplication_tool"
    description = (
        "This tool performs a simple multiplication between two Real numbers like: A * B = C"
        "Where A + B + C = D is required, this tool must be invoked twice like: A * B = F then C * F = D"
        "It returns the result of the multiplication operation"
    )

    inputs = {
        "first_number": {
            "type": "number",
            "description": "The number on the left side of the * operator",
        },
        "second_number": {
            "type": "number",
            "description": "The number on the right side of the * operator",
        }
    }
    output_type = "number"
    
    def forward(self, inputs):
        x = inputs["first_number"]
        y = inputs["second_number"]
        return x * y