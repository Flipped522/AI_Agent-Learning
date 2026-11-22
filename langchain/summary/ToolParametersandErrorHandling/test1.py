from pydantic import BaseModel, Field
from langchain.tools import tool


class OrderLookupInput(BaseModel):
    order_no: str = Field(description="订单号，只能包含数字，例如 20260001")


@tool(args_schema=OrderLookupInput)
def get_order_status(order_no: str) -> dict:
    """根据订单号查询订单状态。订单号必须是数字。"""
    if not order_no.isdigit():
        return {
            "ok": False,
            "error_type": "INVALID_ORDER_NO",
            "message": "订单号格式不正确，请用户提供数字订单号。",
        }

    if order_no != "20260001":
        return {
            "ok": False,
            "error_type": "ORDER_NOT_FOUND",
            "message": "未找到该订单，请用户核对订单号。",
        }

    return {
        "ok": True,
        "order_no": order_no,
        "status": "SHIPPED",
        "latest_logistics": "包裹已到达上海转运中心。",
    }


print(get_order_status.invoke({"order_no": "abc"}))
print(get_order_status.invoke({"order_no": "20260002"}))
print(get_order_status.invoke({"order_no": "20260001"}))