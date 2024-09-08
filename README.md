# Pixel Pour
Pixel pour is a Python program that simulates falling grains of sand for educational purposes.

* Real-time sand simulation with gravity and collision detection using NumPy
* Smooth particle rendering using PyGame
* Cross-platform support on Windows, macOS and Linux
* Interactive sand placement with mouse input
* Real-time display of FPS and total grain count

## Prerequisites
Before you begin, ensure you have met the following requirements:
* Python 3.12+
* Poetry (for dependency management)

## Installing Pixel Pour

Clone the repository:
```
git clone https://github.com/sldgr/pixel_pour.git
cd pixel_pour
```
Install Poetry if you haven't:
```
pip install poetry
```
Install the project dependencies:
```
pip install
```

## Using Pixel Pour
Run the simulation with:
```
poetry run python -m pixel_pour.main
```

## Configuration
You can adjust simulation parameters in `pixelpour/utils/config.py`:
* `WIDTH` and `HEIGHT`: Set the simulation window size
* `FPS`: Target frame rate
* `SAND_DROP_RATE`: Control how quickly new sand is added
* `GRAVITY`: Adjust the strength of gravity
* `MAX_FALL_SPEED`: Set the terminal velocity for sand grains

## Contributing to Pixel Pour
Contributions are welcome! To contribute to <project_name>, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contact
If you want to contact me you can reach me at <cole.d.harding@gmail.com>.

## License
This project is open source and available under the MIT License.
