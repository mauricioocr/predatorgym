# build_files.sh
sudo apt install libsqlite3-dev
pyenv install 3.11.3
python3.12 -m pip install -r requirements.txt
python3.12 manage.py collectstatic
