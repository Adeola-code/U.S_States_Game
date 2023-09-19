import turtle
import pandas as pd

# Set up the screen
screen = turtle.Screen()
screen.title("U.S States Game")

# Load the map image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the state data from a CSV file
data = pd.read_csv("50_states.csv")

# Create a list of all the states and their coordinates from the CSV data
states_data = data.to_dict(orient="records")

# Initialize a list to store guessed states
guessed_states = []

# Create a Turtle object for marking states
state_marker = turtle.Turtle()
state_marker.penup()
state_marker.hideturtle()

# Main game loop
while len(guessed_states) < 50:  # Continue until all states are guessed

    # Get user input for guessing a state
    answer_state = screen.textinput("Guess the state", "What's another state's name?").title()

    if answer_state == "Exit":
        # Allow the user to exit the game by typing "Exit"
        break

    for state_data in states_data:
        if answer_state == state_data["state"] and answer_state not in guessed_states:
            # Check if the guessed state is in the list of states and hasn't been guessed already
            x = state_data["x"]
            y = state_data["y"]

            # Mark the guessed state on the map
            state_marker.goto(x, y)
            state_marker.write(answer_state, align="center", font=("Arial", 8, "normal"))
            guessed_states.append(answer_state)

# Save the unguessed states to a CSV file
unguessed_states = [state_data["state"] for state_data in states_data if state_data["state"] not in guessed_states]
unguessed_states_df = pd.DataFrame({"state": unguessed_states})
unguessed_states_df.to_csv("unguessed_states.csv")

# Close the window when the user clicks
turtle.exitonclick()
