import os
from dotenv import load_dotenv
load_dotenv()


def get_env(name: str, terminal_action=True) -> str:
    """
    return to environment variables
    """
    if name in os.environ:
        return os.environ[name]
    try:
        if terminal_action is True:
            return (input(f'Enter your {name}: '))
        else:
            return name
    except Exception as e:
        print(e)
