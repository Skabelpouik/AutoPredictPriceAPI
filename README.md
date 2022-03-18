# Automobile Price Prediction as a REST API using Flask

## Groupe 5: Allan, Eric, Fanny

## Procedure
1. Start a virtual environment and install requirements

## File Structure
* predictapi
    * predict_app
        * app.py: Flask API application
        * models: directory that contains the pickled model files
    * scrapping
        * annonces_auto.csv: ads file
        * annonces_pagination.csv: url file
        * konbert-export-516369765ab94.sql
        * scrapping.ipynb: script scrapping 
    * test
        * test.py: request file for testing API
    * requirements.txt: list of packages that the app will import
    * setup.py: setup file for the API

## Testing the API
1. Run the Flask API locally for testing. Go to directory with `app.py`.

```bash
python app.py
```
2. Run the test.py files.

```bash
python test/test.py
```

## Appendix

### Virtual Environment
1. Create new virtual environment
```bash
python -m venv mypredictvenv
```
2. Activate virtual environment
```bash
mypredictvenv/Scripts/activate.bat
```
3. Install required packages from `requirements.txt`
```bash
pip install -r requirements.txt 
```
You will only have to install the `requirements.txt` when working with a new virtual environment.