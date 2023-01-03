import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed("fastest")
t.pensize(3)

# Set the colors
t.color("red", "white")

# Define the messages to draw
messages = ["Merry Christmas", "Happy New Year"]

# Set the starting position
t.penup()
t.goto(-100, 100)

# Loop through the messages
for message in messages:
  # Draw the message
  t.pendown()
  t.begin_fill()
  t.write(message, align="center", font=("Arial", 24, "bold"))
  t.end_fill()
  t.penup()

  # Move down for the next message
  t.sety(t.ycor() - 50)

# Keep the window open until it is closed
turtle.mainloop()
