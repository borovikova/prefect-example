# prefect-example

1. Clone the repo
2. Create and activate virtual env:
```bash
python3 -m venv myenv
source myenv/bin/activate
```
3. Install requirements 
```bash
pip install -r requirements.txt
``` 
Note: `my_workflow.py` uses `pandas` but `pandas` is not installed

4. Start prefect server
```bash
prefect server start
```
5. Create work pool
```bash
prefect work-pool create --type process my-work-pool
```
6. Run deployment
```bash
prefect --no-prompt deploy --all --prefect-file prefect.yaml
```
7. You should get an error 
```
ModuleNotFoundError: No module named 'pandas'
```