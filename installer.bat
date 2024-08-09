cd %LocalAppData%
mkdir drooler
cd drooler
curl "https://raw.githubusercontent.com/bijenmanlol/drooler-URI-protocol-py/main/drooler.bat" --output drooler.bat
curl "https://raw.githubusercontent.com/bijenmanlol/drooler-URI-protocol-py/main/main.py" --output main.py
curl "https://raw.githubusercontent.com/bijenmanlol/drooler-URI-protocol-py/main/data.json" --output data.json
msg "%username%" "Drooler-URI-protocol-py has been installed"
py main.py