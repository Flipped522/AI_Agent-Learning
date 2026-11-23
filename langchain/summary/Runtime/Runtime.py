from dataclasses import dataclass
from langchain.tools import tool, ToolRuntime


ORDERS = {
    "user_123": ["20260001", "20260002"],
    "user_456": ["20260003"],
}


@dataclass
class RequestContext:
    user_id: str
    channel: str


@tool
def list_my_orders(runtime: ToolRuntime[RequestContext]) -> list[str]:
    """查询当前用户自己的订单号列表。"""
    return ORDERS.get(runtime.context.user_id, [])