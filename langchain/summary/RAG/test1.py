POLICIES = [
    {
        "source": "after_sale_policy_v1",
        "text": "普通数码配件支持签收后 7 天无理由退货，质量问题按售后检测结果处理。",
    },
    {
        "source": "invoice_policy_v1",
        "text": "电子发票开具后如抬头错误，可在 30 天内申请重开。",
    },
]


def retrieve(query: str) -> list[dict]:
    keywords = ["退", "售后", "发票", "抬头"]
    return [
        doc for doc in POLICIES
        if any(keyword in query and keyword in doc["text"] for keyword in keywords)
    ]


question = "耳机签收 8 天了还能无理由退吗？"
docs = retrieve(question)

print("检索结果：")
for doc in docs:
    print(doc["source"], doc["text"])