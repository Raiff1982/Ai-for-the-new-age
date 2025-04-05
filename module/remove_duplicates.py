import subprocess


def remove_duplicates(file_path):
	with open(file_path, 'r') as file:
		lines = file.readlines()

	# Remove duplicates while preserving order
	seen = set()
	unique_lines = []
	for line in lines:
		if line not in seen:
			unique_lines.append(line)
			seen.add(line)

	with open(file_path, 'w') as file:
		file.writelines(unique_lines)


def check_outdated_packages():
	result = subprocess.run(['pip', 'list', '--outdated'], capture_output=True, text=True)
	print("Outdated packages:")
	print(result.stdout)


if __name__ == "__main__":
	file_path = 'requirements.txt'  # Path to your requirements.txt file
	remove_duplicates(file_path)
	print(f"Duplicates removed from {file_path}")

	check_outdated_packages()
