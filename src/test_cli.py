import src.ui.main as ui

def main():
	print("Test Output Success")

	a = input("Would you like to launch the UI? [Yy/Nn]: \n").strip()

	if a == 'y' or a == 'Y':
		ui.main()

	print("Thank you for using stepgen!")
	print(r"  If you had any issues, please make an issue on the GitHub!")
