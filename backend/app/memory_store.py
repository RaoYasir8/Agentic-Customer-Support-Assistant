from langchain_core.chat_history import InMemoryChatMessageHistory


class ChatMemoryStore:
    def __init__(self):
        self._store: dict[str, InMemoryChatMessageHistory] = {}

    def get_history(self, session_id: str) -> InMemoryChatMessageHistory:
        if session_id not in self._store:
            self._store[session_id] = InMemoryChatMessageHistory()
        return self._store[session_id]

    def clear_history(self, session_id: str) -> None:
        if session_id in self._store:
            self._store[session_id].clear()


memory_store = ChatMemoryStore()