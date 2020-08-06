from flask import jsonify
from models import Widget

def get_all_widgets():
    all_widgets = Widget.query.all()
    results = []
    for widget in all_widgets:
        results.append(widget.as_dict())
    # results = [user.as_dict() for user in all_users]
    return jsonify(results)

def create_widget(name, wodgets, quantity):
    new_widget = Widget(name=name, wodgets=wodgets, quantity=quantity)
    db.session.add(new_widget)
    db.session.commit()
    return jsonify(new_widget.as_dict())

def get_widget(id):
    widget = Widget.query.get(id)
    if widget:
        return jsonify(widget.as_dict())
    else: 
        return jsonify(message =f'Error getting user at {id}')

def update_widget(id, name, wodgets, quantity):
    widget = Widget.query.get(id)
    if widget:
        widget.name = name or widget.name
        widget.wodgets = wodgets or widget.wodgets
        widget.quantity = quantity or widget.quantity
        db.session.commit()
        return jsonify(widget.as_dict())
    else:
        return jsonify(message=f'No Widget at id {id}')

def delete_widget(id):
    widget = Widget.query.get(id)
    if widget:
        db.session.delete(user)
        db.session.commit()
        return redirect('/widgets')
    else:
        return jsonify(message=f'No widget at id {id}')