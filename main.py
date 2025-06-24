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
	"r": "reset",
	"c": "chat",
	"m": "math",
	"t": "task",
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
	print(titles.MATH)

	import subprocess as sub

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

# task manager app

def task_app():
	"""task manager application."""
	clear()
	print(titles.TASK)

	import json

	def load_tasks():
		"""load tasks from a JSON file."""
		try:
			with open("tasks.json", "r") as file:
				return json.load(file)
		except (FileNotFoundError, json.JSONDecodeError):
			return []
		
	def save_tasks(tasks):
		"""save tasks to a JSON file."""
		with open("tasks.json", "w") as file:
			json.dump(tasks, file, indent=4)

	def display_tasks(tasks):
		"""display the list of tasks."""
		if not tasks:
			print("no tasks found.")
			return
		print("\ntasks:")
		for i, task in enumerate(tasks, start=1):
			status = f"({st.colorize('x', st.FG.GREEN)})" if task["completed"] \
				else f"({st.colorize('o', st.FG.RED)})"
			print(f"{st.colorize(f"{i}.", st.FG.BLUE)} {status} {task['task']}")
		print()

	def add_task(tasks, task):
		"""add a new task."""
		tasks.append({"task": task, "completed": False})
		save_tasks(tasks)
		print(f"\n➡️ task added: {task}\n")

	def change_task_status(tasks, index):
		"""change a task's status."""
		try:
			if 1 <= index <= len(tasks):
				tasks[index - 1]["completed"] = not tasks[index - 1]["completed"]
				save_tasks(tasks)
				print(f"\n➡️ task {index}'s status changed.\n")
			else:
				print(f"\n{st.colorize('error', st.FG.RED)}: invalid task number.\n")
		except ValueError:
			print(f"\n{st.colorize('error', st.FG.RED)}: please enter a valid number.\n")

	def rename_task(tasks, index, new_name):
		"""rename a task."""
		try:
			if 1 <= index <= len(tasks):
				tasks[index - 1]["task"] = new_name
				save_tasks(tasks)
				print(f"\n➡️ task {index} renamed to: {new_name}\n")
			else:
				print(f"\n{st.colorize('error', st.FG.RED)}: invalid task number.\n")
		except ValueError:
			print(f"\n{st.colorize('error', st.FG.RED)}: please enter a valid number.\n")

	def delete_task(tasks, index):
		"""delete a task."""
		try:
			if index is None:
				index = int(input("enter the task number to delete: "))
			if 1 <= index <= len(tasks):
				deleted_task = tasks.pop(index - 1)
				save_tasks(tasks)
				print(f"\n➡️ task {index} deleted: {deleted_task['task']}\n")
			else:
				print(f"\n{st.colorize('error', st.FG.RED)}: invalid task number.\n")
		except ValueError:
			print(f"\n{st.colorize('error', st.FG.RED)}: please enter a valid number.\n")

	while True:
		command = input(st.colorize(">", st.FG.BLUE)).strip()
		tasks = load_tasks()

		if command.lower() == f'{COMMAND_PREFIX}x':
			clear()
			print_title()
			return
		elif command.lower() == f'{COMMAND_PREFIX}r':
			clear()
			print(titles.TASK)
		elif command.lower().startswith(f'{COMMAND_PREFIX}a '):
			task_text = command[len(f'{COMMAND_PREFIX}a '):].strip()
			if not task_text:
				print(f"\n{st.colorize('error', st.FG.RED)}: please provide a task description.\n")
			else:
				add_task(tasks, task_text)
		elif command.lower() == f'{COMMAND_PREFIX}l':
			display_tasks(tasks)
		elif command.lower().startswith(f'{COMMAND_PREFIX}c '):
			arg = command[len(f'{COMMAND_PREFIX}c '):].strip()
			if not arg:
				print(f"\n{st.colorize('error', st.FG.RED)}: please specify the task number.\n")
			else:
				try:
					index = int(arg)
					change_task_status(tasks, index)
				except ValueError:
					print(f"\n{st.colorize('error', st.FG.RED)}: please enter a valid number.\n")
		elif command.lower().startswith(f'{COMMAND_PREFIX}d '):
			arg = command[len(f'{COMMAND_PREFIX}d '):].strip()
			if not arg:
				print(f"\n{st.colorize('error', st.FG.RED)}: please specify the task number.\n")
			else:
				try:
					index = int(arg)
					delete_task(tasks, index)
				except ValueError:
					print(f"\n{st.colorize('error', st.FG.RED)}: please enter a valid number.\n")
		elif command.lower().startswith(f'{COMMAND_PREFIX}n '):
			parts = command[len(f'{COMMAND_PREFIX}n '):].strip().split(' ', 1)
			if len(parts) < 2 or not parts[0] or not parts[1]:
				print(f"\n{st.colorize('error', st.FG.RED)}: please specify the task number and new name.\n")
			else:
				try:
					index = int(parts[0])
					new_name = parts[1].strip()
					rename_task(tasks, index, new_name)
				except ValueError:
					print(f"\n{st.colorize('error', st.FG.RED)}: please enter a valid number.\n")
		else:
			print(f"\n{st.colorize('error', st.FG.RED)}: unknown command.\n")

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
		elif input_text.lower() == f'{COMMAND_PREFIX}t':
			task_app()
		else:
			print("unknown command. type '-h' for help.")

if __name__ == "__main__":
	print_title()
	main()