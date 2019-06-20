from flask import Flask, jsonify
from flask_cors import CORS
import csv

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

filename = '/Users/kuicao/Desktop/info.csv'
fail_list = []
all_list = []
select_list = []
with open(filename) as f:
    reader = csv.reader(f)
    #head_row = next(reader) #read first row
    #print(head_row)
    for i in reader:
        Dict = {}
        Dict['Year'] = 2019
        Dict['Month'] = i[7]
        Dict['Day'] = i[8]
        Dict['Hour'] = i[9]
        Dict['Minute'] = i[10]
        Dict['Second'] = i[11]
        all_list.append (Dict)
        if i[13] == 'Fail':
            select_list.append (Dict)
            fail_list.append ("2019-{}-{} {}:{}:{}.{}".format(i[7],i[8],i[9],i[10],i[11],i[12]))

BOOKS = {
        'title': 1
    }


# sanity check route
@app.route('/all', methods=['GET'])
def showalllist():
    return jsonify({
        'all': all_list
    })

@app.route('/fail', methods=['GET'])
def showfaillist():
    return jsonify({
        'fail': select_lista
    })

if __name__ == '__main__':
    app.run()
