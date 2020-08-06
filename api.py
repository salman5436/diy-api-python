from models import app, Widget
from flask import jsonify, request
from crud.widget_crud import get_all_widgets, create_widget, get_widget, update_widget, delete_widget

@app.route('/widgets', methods=['GET', 'POST'])
def widget_index_create():
    if request.method == 'GET':
        return get_all_widgets()
    if request.method == 'POST':
        return create_widget(name=request.form['name'], wodgets=request.form['wodgets'], quantity=request.form['quantity'])

@app.route('/widgets/<id>', methods=['GET', 'PUT', 'DELETE'])
def widget_show_put_delete(id):
    if request.method == 'GET':
        return get_user(id)
    if request.method == 'PUT':
        return get_widget(id)
    if request.method == 'DELETE':
        return delete_widget(id)

