Create virtual environment, install requirements and run app:

cd miljoenenjacht
py -3 -m venv .venv
.venv\Scripts\activate
python -m pip install Flask
python -m flask --app app run --debug