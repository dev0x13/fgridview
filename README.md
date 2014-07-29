FGridView
=========

FGridView generates YII-style GridView for Python web frameworks like Flask. CSS was partially taken from YII framework, but styles are replaceable.
Usage example:

    data = [{"uid": 1, "name": "Porto", "comments": "The woman"},
            {"uid": 2, "name": "Ghast", "comments": "The daemon"}]

    labels = OrderedDict() # Important!
    labels["name"] = "Name"
    labels["comments"] = "Misc"

    actions = [{"link": "/entities/update/", "title": "Update",
                "image": "/static/img/update.png", "id":  "uid"},
               {"link": "/entities/delete/", "title": "Delete",
                "image": "/static/img/delete.png", "id": "uid"}]

    def css_expression_func(row_number, row):
        if row["is_error"] == 1:
            return "err"
        if row_number % 2 == 0:
            return "odd"
        else:
            return "even"

    # Example sorting handling
    sorting_params = {}
    sorting = "/users?sort=1&field="
    if request.method == "GET":
        if request.args.get("sort") and request.args.get("order") and request.args.get("field"):
            sorting_params = {"field": request.args.get("field"), "order": request.args.get("order")}
            # Your code with selecting data from source in due order

    grid = FGridView.render_grid(data, labels, actions, sorting, css_expression_func, sorting_params)
