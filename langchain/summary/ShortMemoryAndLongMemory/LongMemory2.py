from langgraph.store.memory import InMemoryStore


store = InMemoryStore()


def save_preference(user_id: str, key: str, value: dict) -> None:
    namespace = ("users", user_id, "preferences")
    store.put(namespace, key, value)


def get_preference(user_id: str, key: str) -> dict | None:
    namespace = ("users", user_id, "preferences")
    item = store.get(namespace, key)
    return None if item is None else item.value


save_preference("user_123", "delivery", {"preferred_carrier": "SF"})
print(get_preference("user_123", "delivery"))