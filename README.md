# Example Python Project Structure

**Features**:
- example nested library `mylib`
	- relative imports
	- submodules
		- `mylib.compute`
		- `mylib.functional`

- `context.py` in entry point directories (`tests/` & `notebooks`)
- various entry points
	- console
		- `python3 notebooks/blah.py`
	- notebook
		- `notebooks/example_ntb.py`
	- tests
		- `python3 tests/test_compute.py`
	- `main.py`
		- `python3 main.py`
	
In `pycharm`, running the entry points (e.g. `tests/test_compute.py`)
	does not require `context.py` because `pycharm` modifies module search
	path `sys.path` by adding dirs marked as sources / tests. In console,
	or notebooks, we need to manage that ourselves. (Or we can install the
	module globally, ...)

