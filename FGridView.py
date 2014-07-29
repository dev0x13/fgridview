# -*- coding: utf-8 -*-

class FGridView(object):

    # Grid render function
    # @param list data                List of data dictionaries/lists
    # @param dict columns             Dictionary of columns attributes (only name or name and type)
    # @param list actions             List of actions including links to the handler and to the image, title, name of unique field
    # @param string sorting           Link to the sorting handler
    # @param dict sorting_params      Sorting parameters dictionary (for showing in table head)
    # @param func css_expression_func CSS styling expression
    @staticmethod
    def render_grid(data = [], columns = {}, actions = [], sorting = "",
                    css_expression_func = None, sorting_params = {}):
        if not data:
            return ""
        sorting_style = ""
        style = ""
        if not columns:
            for row in data[0]:
                columns[row] = row
        columns_order = list(columns.keys())
        order = 0
        row_number = 0
        grid = "<div class='grid-view'>"
        grid += "<table class='items'>"
        grid += "<thead>"
        for key, column in columns.iteritems():
            column = column["label"] if type(column) is dict else column
            grid += "<th>"
            if sorting:
                if sorting_params:
                    if sorting_params["field"] == key:
                        if sorting_params["order"] == "1":
                            sorting_style = "asc"
                        else:
                            sorting_style = "desc"
                        order = 1 - int(sorting_params["order"])
                grid += "<a class='{0}' href='".format(sorting_style)
                grid += sorting + key + "&order=" + str(order)
                grid += "'>"
                grid += column
                grid += "</a>"
            else:
                grid += column
            grid += "</th>"
        if actions:
            grid += "<th class='button-column'>&nbsp;</th>"
        grid += "</thead>"
        grid += "<tbody>"
        for row in data:
            row_number += 1
            if css_expression_func:
                style = css_expression_func(row_number, row)
            else:
                style = "odd"
            grid += "<tr class='{0}'>".format(style)
            for key in columns_order:
                grid += "<td>"
                if row[key] == None:
                    row[key] = ""
                try:
                    row[key] = unicode(row[key], "utf-8")
                except:
                    pass
                try:
                    row[key] = str(row[key])
                except:
                    pass
                if type(columns[key]) is dict and columns[key]["type"] != "html":
                    row[key] = row[key].replace(">", "&gt").replace("<", "&lt")
                grid += row[key]
                grid += "</td>"
            if actions:
                grid += "<td class='button-column'>"
                for action in actions:
                    grid += "<a title='"
                    grid += action['title']
                    grid += "' href='"
                    grid += action['link'] + str(row[action['id']])
                    grid += "'>"
                    grid += "<img src='"
                    grid += action['image']
                    grid += "' alt='"
                    grid += action['title']
                    grid += "'></a>"
                grid += "</td>"
            grid += "</tr>"
        grid += "</tbody>"
        grid += "</table>"
        grid += "</div>"
        return grid
