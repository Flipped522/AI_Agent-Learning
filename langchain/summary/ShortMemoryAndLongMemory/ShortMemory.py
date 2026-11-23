# 这里只用内存字典演示短期记忆概念。
# 真实系统要用 LangGraph checkpointer 持久化 thread 状态，而不是普通内存字典。
threads: dict[str, list[dict]] = {}


def add_message(thread_id: str, role: str, content: str) -> list[dict]:
    history = threads.setdefault(thread_id, [])
    history.append({"role": role, "content": content})
    return history


add_message("customer_001", "user", "我明天出差，想买降噪耳机。")
add_message("customer_001", "assistant", "可以优先看支持快速配送的降噪耳机。")
history = add_message("customer_001", "user", "这款能赶上吗？")

print(history)