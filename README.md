1. Start postgres db in docker
docker run --rm --name doc_design_rgr_db -d -e POSTGRES_PASSWORD=*******  -e POSTGRES_DB=doc_design_rgr_db -p 5432:5432 postgres

2. Create virtual environment
python3 -m venv /path/to/new/virtual/environment

3. Activate virtual environment
.\path\to\new\virtual\environment\Scripts\activate

4. Install requirements
pip install -r requirements.txt

5. Run 
python main.py
