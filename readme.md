# FastAPI Visualize

A proof of concept where a python backend streams 3D data to
a webpage that displays it.

The backend uses Fast API and the front end is based on Three.js.

## Getting started

Step 1, create a virtual environment.
```
python -m venv env
```
Step 2, Activate new environment.
```powershell
# On Linux
$ source env/bin/activate

# On Windows (in Powershell)
> .\env\Scripts\Activate.ps1
```

Step 3, Install requirements.
```
pip install -r requirements.txt
```
Step 4, Start the server.
```
uvicorn server.main:app --reload
```
Step 5, Visit your webpage (whatever is put in web_root).
In your browser go to
```
http://127.0.0.1:8000/
```