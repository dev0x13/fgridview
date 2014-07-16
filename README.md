FGridView
=========

FGridView generates YII-style GridView for Python web frameworks like Flask. CSS was partially taken from YII framework, but styles are replaceable.
Usage example:

    def css_expression_func(row_number, row):
        if row['is_error'] == 1:
            return "err"
        if row_number % 2 == 0:
            return "odd"
        else:
            return "even"

    data = [{'uid': 1, 'name': 'Porto', 'comments': 'woman'},
            {'uid': 2, 'name': 'Ghast', 'comments': 'daemon'}]    
    labels['name'] = 'Name'
    labels['comments'] = 'Misc'
    actions = [{'link': '/entities/update/', 'title': 'Update', 'image': '/static/img/update.png', 'id':  'uid'}, 
    {'link': '/entities/delete/', 'title': 'Delete', 'image': '/static/img/delete.png', 'id': 'uid'}]
    grid = FGridView.render_grid(data, labels, actions, css_expression_func)
