command_is_running = False;

command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        command_is_running = True
        if command_is_running:
            print("Car has already started.")
        else:
            print("Car started.")
    elif command == "stop":
        if not command_is_running:
            print("Car is already stopped")
        else:
            command_is_running = False
            print("Car has stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        print("Quitting...")
        break
    else:
        print(f"Sorry, there is no {command} command")