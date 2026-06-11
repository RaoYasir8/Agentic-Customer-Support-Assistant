from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq import ChatGroq

from app.config import settings
from app.memory_store import memory_store
from app.support_tools import support_tools


SYSTEM_PROMPT = """
You are an AI-powered customer support assistant.
Your job is to help customers politely, clearly, and accurately.

Rules:
1. Behave like a professional support agent.
2. Use tools when the user asks about order status, policies, product information, or ticket creation.
3. If the issue is complex, offer to create a support ticket.
4. Do not invent order details. Use the order tool for order-related questions.
5. Keep responses concise but helpful.
6. Remember conversation context using chat history.
7. If information is missing, ask the user for the missing detail.
"""


llm = ChatGroq(
    groq_api_key=settings.GROQ_API_KEY,
    model=settings.GROQ_MODEL,
    temperature=0.3,
    max_tokens=1024,
)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)


agent = create_tool_calling_agent(
    llm=llm,
    tools=support_tools,
    prompt=prompt,
)


agent_executor = AgentExecutor(
    agent=agent,
    tools=support_tools,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=5,
)


agent_with_memory = RunnableWithMessageHistory(
    agent_executor,
    lambda session_id: memory_store.get_history(session_id),
    input_messages_key="input",
    history_messages_key="chat_history",
)


async def run_support_agent(message: str, session_id: str) -> str:
    result = await agent_with_memory.ainvoke(
        {"input": message},
        config={"configurable": {"session_id": session_id}},
    )

    return result["output"]