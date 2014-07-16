FGridView
=========

FGridView generates YII-style GridView for Python web frameworks like Flask. CSS was partially taken from YII framework, but styles are replaceable.
Usage example:

    data = [{'uid': 1, 'name': 'Porto', 'comments': 'woman'},
            {'uid': 2, 'name': 'Ghast', 'comments': 'demon'}]    
    labels['name'] = 'Name'
    labels['comments'] = 'Misc'
    actions = [{'link': '/entities/update/', 'title': 'Update', 'image': '/static/img/update.png', 'id':  'uid'}, 
    {'link': '/entities/delete/', 'title': 'Delete', 'image': '/static/img/delete.png', 'id': 'uid'}]
    grid = FGridView.render_grid(data, labels, actions)
