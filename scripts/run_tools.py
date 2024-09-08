import subprocess
import sys


def run_command(command: str) -> None:
    """
    Run a shell command.
    :param command: Command to be executed.
    :return: None
    """
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {command}: {e}")
        sys.exit(1)


def main() -> None:
    """
    Main function for script to run all dev tools at once.
    :return:
    """
    commands = ["black .", "isort .", "flake8 .", "mypy .", "pytest"]

    for command in commands:
        print(f"Running: {command}")
        run_command(command)
        print("---")

    print("All tools ran successfully!")


if __name__ == "__main__":
    main()
