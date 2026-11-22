import os
from typing import Literal
from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


class PurchaseIntent(BaseModel):
    category: str = Field(description="用户想购买的商品品类")
    budget_yuan: int | None = Field(default=None, description="预算金额，单位元")
    usage: str | None = Field(default=None, description="使用场景")
    urgency: Literal["unknown", "normal", "urgent"] = Field(
        default="unknown",
        description="是否急用",
    )
    gift: bool = Field(default=False, description="是否作为礼物")


model = ChatOpenAI(
    model=os.environ["AGENT_OPENAI_MODEL"],
    api_key=os.environ["AGENT_OPENAI_API_KEY"],
    base_url=os.environ["AGENT_OPENAI_BASE_URL"],
    temperature=0,
)

agent = create_agent(
    model=model,
    tools=[],
    response_format=PurchaseIntent,
    system_prompt="你负责从电商客户咨询中抽取购买意图。只抽取用户明确表达的信息。",
)

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "我想买一个 500 元以内的蓝牙耳机，明天出差要用，最好适合送同事。",
        }
    ]
})

print(result["structured_response"])