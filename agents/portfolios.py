from swarm import Agent
from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console
import asyncio
from aptos_sdk.async_client import IndexerClient

console = Console()


def get_address(context_variables):
    console.print(
        Panel.fit(
            "Enter the address (0x...) of the relevant portfolio.",
            title="Portfolio Agent",
        )
    )
    address = Prompt.ask(
        "> ",
    ).strip()
    context_variables["address"] = address
    return "success"


async def _get_account_info(context_variables):
    address = context_variables["address"]
    INDEXER_URL = "https://api.mainnet.aptoslabs.com/v1/graphql"
    indexer_client = IndexerClient(INDEXER_URL)
    query = """
        query GetFungibleAssetBalances($account: String) {
        current_fungible_asset_balances(
            where: {owner_address: {_eq: $account}}
            limit: 100
            order_by: {amount: desc}
        ) {
            asset_type
            amount
            __typename
        }
        }
    """
    variables = {"account": f"{address}"}
    data = await indexer_client.query(query, variables)
    return data


def get_account_info(context_variables):
    data = asyncio.run(_get_account_info(context_variables))
    return data


portfolio_agent = Agent(
    name="Portfolio Agent",
    instructions="""You are a portfolio agent that provides information and analysis on portfolios.
    
    To get started, you can get the address from the user with the appropriate tool. You can then
    then account information in order to successfully answer questions about the relevant portfolio.
    
    Analyze the user's message and call the appropriate agent function.""",
    functions=[get_address, get_account_info],
    context_variables={},
)
