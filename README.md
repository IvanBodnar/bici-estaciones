### Installation
- Clone the repository.  **The download will take a while, since it has to fetch the csv file**  
$ git clone git@github.com:IvanBodnar/bici-estaciones.git

- cd into bici_estaciones

- Create and activate a virtual environment  
$ python3.7 -m venv venv  
$ source venv/bin/activate  

- Install the package in editable mode  
$ pip install -e .

- Run the program  
$ python bici_estaciones/main.py

- To run the tests install requirements.txt  
$ pip install -r requirements.txt  
$ pytest