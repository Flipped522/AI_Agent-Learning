import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


model = ChatOpenAI(
    model=os.environ["AGENT_OPENAI_MODEL"],
    api_key=os.environ["AGENT_OPENAI_API_KEY"],
    base_url=os.environ["AGENT_OPENAI_BASE_URL"],
    temperature=0,
)

question = "我的订单明天出差前必须收到，你直接保证今天一定送到。"

without_boundary = model.invoke([
    ("user", question),
])

with_boundary = model.invoke([
    (
        "system",
        "你是电商客服助手。订单、物流、退款、赔付和保修结论必须基于业务系统或人工确认。"
        "不能承诺发货时间、到货时间、退款结果、赔付金额或规则例外。"
        "遇到缺少事实的问题，先要求用户补充订单号；遇到高风险承诺，说明不能直接承诺并给出下一步。",
    ),
    ("user", question),
])

print("无约束回复：")
print(without_boundary.content)
print()
print("有边界回复：")
print(with_boundary.content)