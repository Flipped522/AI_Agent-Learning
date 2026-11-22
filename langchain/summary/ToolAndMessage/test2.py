import os
from langchain.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


model = ChatOpenAI(
    model=os.environ["AGENT_OPENAI_MODEL"],
    api_key=os.environ["AGENT_OPENAI_API_KEY"],
    base_url=os.environ["AGENT_OPENAI_BASE_URL"],
    temperature=0,
)

messages = [
    SystemMessage(
        "你是电商客服助手。"
        "如果涉及订单、物流、库存、退款和赔付，不能编造事实。"
    ),
    HumanMessage("这款蓝牙耳机适合出差使用吗？"),
]

response = model.invoke(messages)
print(type(response))
print(response.content)
print(response.usage_metadata)