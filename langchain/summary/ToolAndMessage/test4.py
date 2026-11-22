from langchain.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage

messages = [
    # 系统消息：定义客服规则
    SystemMessage(
        "你是电商客服助手。"
        "回答库存问题时，必须以真实库存数据为依据，"
        "不能编造库存数量或是否有货。"
        "如果没有库存数据，请明确告知用户暂时无法确认。"
    ),

    # 用户消息：提出问题
    HumanMessage("这款蓝牙耳机现在还有库存吗？")
]

print(messages)