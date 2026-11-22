import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

@tool
def get_order_status(order_no: str) -> dict:
    """根据订单号查询订单状态。适合回答订单是否发货、当前处理状态等问题。"""
    if order_no != "20260001":
        return {
            "ok": False,
            "message": "未找到该订单，请用户核对订单号。",
        }

    return {
        "ok": True,
        "order_no": order_no,
        "status": "SHIPPED",
        "latest_event": "订单已出库，等待揽收。",
    }


model = ChatOpenAI(
    model=os.environ["AGENT_OPENAI_MODEL"],
    api_key=os.environ["AGENT_OPENAI_API_KEY"],
    base_url=os.environ["AGENT_OPENAI_BASE_URL"],
    temperature=0,
)

agent = create_agent(
    model=model,
    tools=[get_order_status],
    system_prompt=(
        "你是电商客服助手。"
        "订单状态必须通过工具查询，不能编造。"
        "如果用户没有提供订单号，请要求补充订单号。"
    ),
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "帮我查一下订单 20260001 的状态"}
    ]
})

print(result["messages"][-1].content)