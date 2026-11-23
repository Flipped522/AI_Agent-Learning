def answer_with_docs(question: str, docs: list[dict]) -> str:
    if not docs:
        return (
            "我当前没有找到可依据的政策资料，不能直接给出结论。"
            "请补充订单号、商品名称或联系人工客服确认。"
        )

    context = "\n".join(
        f"[{i + 1}] {doc['source']}：{doc['text']}"
        for i, doc in enumerate(docs)
    )
    return (
        "请基于以下资料回答用户问题，并在回答中标注来源编号。\n\n"
        f"用户问题：{question}\n\n"
        f"资料：\n{context}"
    )


question = "海外购耳机签收 10 天还能退吗？"
docs = []
print(answer_with_docs(question, docs))