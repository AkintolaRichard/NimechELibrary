# E Library

## Setting up the API

### Install Dependencies

1. **Python 3.11** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the home directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [FastAPI] is a fast lightweight backend framework. FastAPI is required to handle requests and responses.

- [Pymongo] is the Python Mongodb toolkit used to handle the Mongodb database.

- [Uvicorn] is the web server.

### Run the Server

From within the home directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
uvicorn index:app --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


### Documentation Example

FastAPI provides documentation for  the endpoints which can be found using '/localhost_url/docs'

