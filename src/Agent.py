from transformers.agents import ReactJsonAgent
from src.tools.AdditionTool import AdditionTool
from src.tools.DivisionTool import DivisionTool
from src.tools.MultiplicationTool import MultiplicationTool
from src.tools.SubtractionTool import SubtractionTool
from src.LLMEngine import HfEngine


def get_agent(model_id: str ="meta-llama/Meta-Llama-3-8B-Instruct", config: dict=None):
    """
    Args:
        model_id (str, optional): model string matching a repo in huggingface models. Defaults to "meta-llama/Meta-Llama-3-8B-Instruct".
        config (dict, optional): Configuration obejct. Defaults to None.

    Returns:
        _huggingface_agent_: An agent driven by the selected LLM agent with toolkit loaded
    """
    llm_engine = HfEngine(model_id=model_id, config=config)

    agent = ReactJsonAgent(
        tools=[],
        llm_engine=llm_engine,
        add_base_tools=False
    )

    agent.toolbox.add_tool(AdditionTool)
    agent.toolbox.add_tool(DivisionTool)
    agent.toolbox.add_tool(MultiplicationTool)
    agent.toolbox.add_tool(SubtractionTool)
    
    return agent