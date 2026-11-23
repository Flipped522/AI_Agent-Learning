from langchain.tools import tool


POLICY_DOCS = [
    "普通数码配件支持签收后 7 天无理由退货。",
    "质量问题需提交售后检测，检测通过后可维修、换货或退款。",
    "电子发票抬头错误可在 30 天内申请重开。",
]


@tool
def retrieve_policy(query: str) -> str:
    """检索售后、物流、发票和活动政策。"""
    hits = [doc for doc in POLICY_DOCS if any(char in doc for char in query)]
    if not hits:
        return "未检索到相关政策。"
    return "\n".join(hits[:2])


print(retrieve_policy.invoke({"query": "耳机退货政策"}))