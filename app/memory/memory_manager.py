chat_history = []

def save_messages(role, content):
    chat_history.append({
        "role":role,
        "content":content
    })


def get_history():
    return chat_history