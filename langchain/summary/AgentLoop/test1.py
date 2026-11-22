def get_order_logistics(order_no: str) -> str:
    """模拟物流工具。"""
    orders = {
        "20260001": "已发货，预计明天送达",
        "20260002": "待发货，仓库正在拣货",
    }
    return orders.get(order_no, "未找到订单")


def fake_model_step(user_input: str, observation: str | None = None) -> dict:
    """模拟模型的下一步决策。"""
    if observation is not None:
        return {
            "type": "finish",
            "content": f"根据查询结果：{observation}",
        }

    if "20260001" in user_input:
        return {
            "type": "action",
            "tool": "get_order_logistics",
            "args": {"order_no": "20260001"},
        }

    return {
        "type": "finish",
        "content": "请提供订单号，我再帮你查询。",
    }


def run_agent(user_input: str) -> str:
    observation = None

    for _ in range(3):
        step = fake_model_step(user_input, observation)

        if step["type"] == "finish":
            return step["content"]

        if step["type"] == "action" and step["tool"] == "get_order_logistics":
            observation = get_order_logistics(**step["args"])
            continue

    return "当前问题暂时无法自动完成，请转人工处理。"


print(run_agent("帮我查一下订单20260001到哪了"))
print(run_agent("我的订单到哪了？"))