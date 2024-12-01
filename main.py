from dotenv import load_dotenv
from swarm import Swarm
from agents.router import router_agent
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

load_dotenv()
client = Swarm()
console = Console()

if __name__ == "__main__":
    console.print(
        Panel.fit("Welcome! Type your message or 'quit' to exit.", title="AI Assistant")
    )
    response = type('EmptyResponse', (), {'messages': [], 'context_variables': {}})()
    while True:
        user_input = Prompt.ask("> ").strip()

        if user_input.lower() == "quit":
            console.print(Panel("Goodbye!", style="bold red"))
            break

        if user_input:
            response.messages.append({"role": "user", "content": user_input})
            response = client.run(
                agent=router_agent,
                messages=response.messages,
                context_variables=response.context_variables,
            )
            console.print(
                Panel(
                    response.messages[-1]["content"],
                    style="blue",
                    title="[blue]AI Response",
                )
            )
