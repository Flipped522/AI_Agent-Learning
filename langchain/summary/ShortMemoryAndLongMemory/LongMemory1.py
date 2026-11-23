from langgraph.store.memory import InMemoryStore


store = InMemoryStore()
namespace = ("users", "user_123", "preferences")

store.put(namespace, "delivery", {"preferred_carrier": "SF"})
item = store.get(namespace, "delivery")

print(item.value)