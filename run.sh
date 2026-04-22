python -m compileall src # check compile time
python -m uvicorn main:app --reload --app-dir src
