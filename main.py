import sys
from src.manage_data import fetch_user_Event
from src.file_handle import parse_events


def start_app():
    if len(sys.argv) != 2:
        print("Correct version: python main.py <username of github>")
        return 
    
    username = sys.argv[1]
    event = fetch_user_Event(username)

    if event is None:
        print("We can not find events!")

    parsed = parse_events(event)

    print(f"\nRecent GitHub activity of '{username}':\n")
    for activity in parsed:
        print(f"- {activity}")




if __name__ == "__main__":
    start_app()



