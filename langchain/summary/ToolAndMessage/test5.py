
from langchain.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage
)

# 构造消息列表
messages = [
    # 1. 系统消息
    SystemMessage("你是电商客服助手，订单物流必须基于工具结果回答。"),

    # 2. 用户提出查询请求
    HumanMessage("订单20260001到哪了？"),

    # 3. AI 发起工具调用请求
    AIMessage(
        content=[],
        tool_calls=[
            {
                "name": "get_order_logistics",
                "args": {"order_no": "20260001"},
                "id": "call_001"
            }
        ]
    ),

    # 4. 模拟工具执行结果
    ToolMessage(
        content="订单已发货，物流单号 SF123456，预计明天送达。",
        tool_call_id="call_001",
        name="get_order_logistics",
        artifact={
            "carrier": "SF",
            "tracking_no": "SF123456"
        }
    ),

    # 5. AI 根据工具结果生成最终回答
    AIMessage(
        "我查到订单20260001已发货，"
        "物流单号 SF123456，预计明天送达。"
    )
]

# 遍历输出消息
for message in messages:
    print("消息类型：", type(message).__name__)
    print("消息内容：", message.content)

    if isinstance(message, AIMessage):
        print("工具调用：", message.tool_calls)

    if isinstance(message, ToolMessage):
        print("工具调用ID：", message.tool_call_id)
        print("附加数据：", message.artifact)

    print("-" * 50)
