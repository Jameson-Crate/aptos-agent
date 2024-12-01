from swarm import Agent
from agents.portfolios import portfolio_agent
from rich.console import Console

console = Console()


def handle_portfolio():
    return portfolio_agent


router_agent = Agent(
    name="Router Agent",
    instructions="""You are a routing agent that directs messages to the appropriate specialized agent.
    
    For portfolio management and analysis, route to the portfolio agent.
    
    Analyze the user's message and call the appropriate agent function.""",
    functions=[handle_portfolio],
)
