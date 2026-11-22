import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


@tool
def get_order_status(order_no: str) -> str:
    """根据订单号查询订单状态。"""
    return f"订单 {order_no} 已发货，物流状态为运输中。"


model = ChatOpenAI(
    model=os.environ["AGENT_OPENAI_MODEL"],
    api_key=os.environ["AGENT_OPENAI_API_KEY"],
    base_url=os.environ["AGENT_OPENAI_BASE_URL"],
    temperature=0,
)

agent = create_agent(
    model=model,
    tools=[get_order_status],
    system_prompt="你是电商客服助手。订单状态必须通过工具查询。",
)

for chunk in agent.stream(
    {"messages": [{"role": "user", "content": "帮我查一下订单 20260001 的状态"}]},
    stream_mode="updates",
):
    print(chunk)