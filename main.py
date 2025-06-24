
# dt is a terminal workspace created by dubi
# it has many tools that integrate AI

from os import system

def clear():
    system('cls||clear')

# loading screen

clear()
print("loading...")

# imports (while loading)

import style as st
import chat
import titles

clear()

# title screen

def print_title():
	"""prints the title screen, stylized."""
	print(titles.MAIN)

# command line interface

COMMAND_PREFIX = "-"

# apps

APP_COMMANDS = {
	"x": "exit",
	"c": "chat",
	"m": "math",
	"r": "reset",
}

# help

def print_help():
	"""prints the available commands with their icons."""
	for cmd, app in APP_COMMANDS.items():
		print(f"· {app} ({st.colorize(f"{COMMAND_PREFIX}{cmd}", st.FG.GREEN)})")
	print()

# chat app

def chat_app():
	"""chat application."""
	clear()
	print(titles.CHAT)

	SYSTEM_PROMPT = "You are a friendly AI assistant.\n" \
		"Answer questions and provide information to the user.\n" \
		"Do not use markdown or any other formatting in your responses."

	model = chat.MODEL
	history = {"user": [], "assistant": [], "system": [SYSTEM_PROMPT]}

	while True:
		user_input = input("👤 ")

		if user_input.lower() == f'{COMMAND_PREFIX}x':
			clear()
			print_title()
			return
		elif user_input.lower() == f'{COMMAND_PREFIX}r':
			clear()
			print(titles.CHAT)
			history = {"user": [], "assistant": [], "system": [SYSTEM_PROMPT]}
			print("\n⚙️ history reset.\n")
			continue
		elif user_input.lower().startswith(f'{COMMAND_PREFIX}m'):
			model = user_input.split(" ", 1)[1]
			chat.MODEL = model
			print(f"\n⚙️ model changed to: {st.colorize(model, st.FG.GREEN)}.\n")
			continue

		history["user"].append(user_input)
		response = chat.gen(
			user=history["user"],
			system=history["system"],
			assistant=history["assistant"],
			model=model
		)
		history["assistant"].append(response)
		print(f"\n🧠 {response.lower()}\n")

# math app

def math_app():
	"""math application."""
	clear()

	import subprocess as sub

	print(titles.MATH)

	while True:
		user_input = input(f"{st.colorize('=>', st.FG.RED)} ")

		if user_input.lower() == f'{COMMAND_PREFIX}x':
			clear()
			print_title()
			return
		elif user_input.lower() == f'{COMMAND_PREFIX}r':
			clear()
			print(titles.MATH)
			continue

		try:
			result = eval(user_input, {"__builtins__": None}, {})
			print(f"\n{st.colorize('=', st.FG.GREEN)} {str(result)}\n")
		except Exception as e:
			print(f"\n{st.colorize('error', st.FG.RED)}: {str(e).lower()}.\n")

# main

def main():
	while True:
		input_text = input(st.colorize(f">>", st.FG.GREEN))
		if input_text.lower() == f'{COMMAND_PREFIX}x':
			clear()
			break
		elif input_text.lower() == f'{COMMAND_PREFIX}h':
			print_help()
		elif input_text.lower() == f'{COMMAND_PREFIX}r':
			clear()
			print_title()
		elif input_text.lower() == f'{COMMAND_PREFIX}c':
			chat_app()
		elif input_text.lower() == f'{COMMAND_PREFIX}m':
			math_app()
		else:
			print("unknown command. type '-h' for help.")

if __name__ == "__main__":
	print_title()
	main()
