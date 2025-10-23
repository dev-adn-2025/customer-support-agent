from ..state import GraphState
from ..utils.gmail_utils import get_most_recent_email

def email_listener_node(state: GraphState) -> GraphState:
    email = get_most_recent_email()
    # state["current_email"] = email
    # return state
    return {"current_email": email}