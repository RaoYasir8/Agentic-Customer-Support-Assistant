from datetime import datetime
from langchain_core.tools import tool


MOCK_ORDERS = {
    "ORD-1001": {
        "status": "Shipped",
        "estimated_delivery": "2026-04-28",
        "carrier": "DHL",
    },
    "ORD-1002": {
        "status": "Processing",
        "estimated_delivery": "2026-05-01",
        "carrier": "FedEx",
    },
    "ORD-1003": {
        "status": "Delivered",
        "estimated_delivery": "2026-04-20",
        "carrier": "TCS",
    },
}


PRODUCT_FAQ = {
    "return_policy": "Customers can request a return within 14 days of delivery if the product is unused and in original packaging.",
    "refund_policy": "Refunds are processed within 5 to 7 business days after the returned item is inspected.",
    "shipping_policy": "Standard shipping usually takes 3 to 7 business days depending on the location.",
    "warranty_policy": "Most products include a 1-year limited warranty against manufacturing defects.",
}


@tool
def check_order_status(order_id: str) -> str:
    """Check the status of a customer order using an order ID like ORD-1001."""
    order = MOCK_ORDERS.get(order_id.upper())

    if not order:
        return "Order not found. Please ask the customer to confirm the order ID."

    return (
        f"Order {order_id.upper()} is currently {order['status']}. "
        f"Carrier: {order['carrier']}. "
        f"Estimated delivery: {order['estimated_delivery']}."
    )


@tool
def get_support_policy(policy_name: str) -> str:
    """Retrieve company support policies such as return_policy, refund_policy, shipping_policy, or warranty_policy."""
    normalized_name = policy_name.lower().strip().replace(" ", "_")
    policy = PRODUCT_FAQ.get(normalized_name)

    if not policy:
        return (
            "Policy not found. Available policies are: "
            "return_policy, refund_policy, shipping_policy, warranty_policy."
        )

    return policy


@tool
def create_support_ticket(customer_issue: str) -> str:
    """Create a mock support ticket for issues that need human support."""
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    ticket_id = f"TICKET-{timestamp}"

    return (
        f"Support ticket created successfully. Ticket ID: {ticket_id}. "
        f"Issue summary: {customer_issue}. "
        "A human support agent will follow up soon."
    )


@tool
def product_information(product_name: str) -> str:
    """Get basic product information for a requested product."""
    return (
        f"{product_name} is one of our supported products. "
        "For exact pricing, availability, and technical details, please check the product page or ask support to verify live inventory."
    )


support_tools = [
    check_order_status,
    get_support_policy,
    create_support_ticket,
    product_information,
]