def build_context(user_question: str, order_summary: str | None, policy_snippet: str | None) -> list[tuple[str, str]]:
    system_prompt = (
        "你是电商客服助手。回答必须基于提供的订单、商品或政策信息。"
        "如果上下文不足，请说明缺少什么信息。"
    )

    context_parts = []
    if order_summary and any(word in user_question for word in ["订单", "物流", "退", "售后"]):
        context_parts.append(f"订单信息：{order_summary}")
    if policy_snippet and any(word in user_question for word in ["退", "换", "保修", "售后"]):
        context_parts.append(f"政策信息：{policy_snippet}")

    if context_parts:
        system_prompt += "\n\n当前可用上下文：\n" + "\n".join(context_parts)

    return [
        ("system", system_prompt),
        ("user", user_question),
    ]


messages = build_context(
    user_question="这个耳机签收 10 天了，还能退吗？",
    order_summary="订单 20260002，商品：降噪耳机，签收时间：2026-05-01。",
    policy_snippet="普通数码配件支持 7 天无理由退货；质量问题按售后检测结果处理。",
)

for role, content in messages:
    print(role, "=>", content)