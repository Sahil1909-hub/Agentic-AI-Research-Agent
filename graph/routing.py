from utils.logger import logger

def route_query(state):

    route = state['route']

    if route == "WEB":
        return "research"
    
    elif route == "RAG":
        return "rag"
    
    elif route == "BOTH":
        return "research"
    
    return "research"