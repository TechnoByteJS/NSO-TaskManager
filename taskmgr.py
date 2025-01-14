import tkinter as tk
from PIL import Image, ImageTk

# Colors
COLOR_LABEL_TEXT = "#5cb3df"
COLOR_COUNT_TEXT = "#4d21ca"
COLOR_HIGH_COUNT = "#e75353"
COLOR_LIMIT_TEXT = "#989896"
COLOR_GRAPH_BG   = "#dbbeed"

# Fonts
FONT_LABEL = ("Dinkiebitmap 7px Demo", 12)
FONT_COUNT = ("Press Start 2P", 30)
FONT_SUB_COUNT = ("Press Start 2P", 18)
FONT_LIMIT = ("Press Start 2P", 12)

# Counts and limits
count1_name = "Followers"
count1 = 1234567
count2_name = "Stress"
count2 = 0
count3_name = "Affection"
count3 = 0
count4_name = "Mental Darkness"
count4 = 0

count2_limit = 100
count3_limit = 100
count4_limit = 100

# Historical data (26 chunks, each 5 pixels on the graph)
count2_history = [count2] * 26
count3_history = [count3] * 26
count4_history = [count4] * 26

# Function to determine text color based on count
def get_count_color(count):
	return COLOR_HIGH_COUNT if count >= 80 else COLOR_COUNT_TEXT

# Function to draw graphs
def draw_graphs():
	canvas.delete("graph")

	# Update count 2 graph
	for i, value in enumerate(count2_history):
		height = 55 * (1 - value / count2_limit)
		if value > 0:
			canvas.create_rectangle(236 + i * 5, 83 + height, 236 + (i + 1) * 5, 138, fill=COLOR_LABEL_TEXT, outline="", tags="graph")
	
	# Update count 3 graph
	for i, value in enumerate(count3_history):
		height = 55 * (1 - value / count3_limit)
		if value > 0:
			canvas.create_rectangle(236 + i * 5, 154 + height, 236 + (i + 1) * 5, 209, fill=COLOR_LABEL_TEXT, outline="", tags="graph")
	
	# Update count 4 graph
	for i, value in enumerate(count4_history):
		height = 55 * (1 - value / count4_limit)
		if value > 0:
			canvas.create_rectangle(236 + i * 5, 225 + height, 236 + (i + 1) * 5, 280, fill=COLOR_LABEL_TEXT, outline="", tags="graph")

# Function to draw counts and graphs periodically
def draw_counts():
	global count2, count3, count4
	global count2_history, count3_history, count4_history
	
	# Update historical data
	count2_history.append(count2)
	count2_history.pop(0)
	count3_history.append(count3)
	count3_history.pop(0)
	count4_history.append(count4)
	count4_history.pop(0)
	
	# Update graphs
	draw_graphs()
	
	# Update count texts
	canvas.delete("count_texts")
	canvas.create_text(70, 38, text=str(count1), font=FONT_COUNT, fill=COLOR_COUNT_TEXT, anchor=tk.NW, tags="count_texts")
	canvas.create_text(66, 108, text=f"{count2:3}", font=FONT_SUB_COUNT, fill=get_count_color(count2), anchor=tk.NW, tags="count_texts")
	canvas.create_text(66, 179, text=f"{count3:3}", font=FONT_SUB_COUNT, fill=get_count_color(count3), anchor=tk.NW, tags="count_texts")
	canvas.create_text(66, 250, text=f"{count4:3}", font=FONT_SUB_COUNT, fill=get_count_color(count4), anchor=tk.NW, tags="count_texts")
	
	# Draw limits
	canvas.create_text(140, 115, text=f"/{count2_limit}", font=FONT_LIMIT, fill=COLOR_LIMIT_TEXT, anchor=tk.NW, tags="count_texts")
	canvas.create_text(140, 186, text=f"/{count3_limit}", font=FONT_LIMIT, fill=COLOR_LIMIT_TEXT, anchor=tk.NW, tags="count_texts")
	canvas.create_text(140, 257, text=f"/{count4_limit}", font=FONT_LIMIT, fill=COLOR_LIMIT_TEXT, anchor=tk.NW, tags="count_texts")

	# Simulate changing counts (you can replace this with actual logic)
	count2 = min(count2 + 1, count2_limit)
	count3 = min(count3 + 2, count3_limit)
	count4 = min(count4 + 3, count4_limit)
	
	# Schedule the next update
	root.after(2000, draw_counts)

# Create window and canvas
root = tk.Tk()
root.title("Task Manager")
root.resizable(False, False)
canvas = tk.Canvas(root, width=376, height=292)
canvas.pack()

# Background image
background = ImageTk.PhotoImage(Image.open("bg.png"))
canvas.create_image(0, 0, image=background, anchor=tk.NW)

# Count 1 label
canvas.create_text(68, 20, text=count1_name, font=FONT_LABEL, fill=COLOR_LABEL_TEXT, anchor=tk.NW)
# Count 2 label
canvas.create_text(68, 91, text=count2_name, font=FONT_LABEL, fill=COLOR_LABEL_TEXT, anchor=tk.NW)
# Count 3 label
canvas.create_text(68, 162, text=count3_name, font=FONT_LABEL, fill=COLOR_LABEL_TEXT, anchor=tk.NW)
# Count 4 label
canvas.create_text(68, 233, text=count4_name, font=FONT_LABEL, fill=COLOR_LABEL_TEXT, anchor=tk.NW)

# Count 2 graph background
canvas.create_rectangle(236, 83, 366, 138, fill=COLOR_GRAPH_BG, outline="")
# Count 3 graph background
canvas.create_rectangle(236, 154, 366, 209, fill=COLOR_GRAPH_BG, outline="")
# Count 4 graph background
canvas.create_rectangle(236, 225, 366, 280, fill=COLOR_GRAPH_BG, outline="")

# Start updating the counts and graphs
draw_counts()

root.mainloop()