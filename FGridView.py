# -*- coding: utf-8 -*-

class FGridView(object):
  
    # Grid render function
    # @param list data - list of dictionaries/lists
    # @param dict labels - dictionary of labels, where keys equals keys of "data" element
    # @param list actions - list of actions including links to the handler and to the image, title, name of unique field
    # @param string sorting - link to the sorting handler
    @staticmethod
    def render_grid(data = [], labels = {}, actions = [], sorting = ''):
        if not data:
            return
        grid = "<div class='grid-view'>"
        grid += "<table class='items'>"
        if not labels:
            for row in data[0]:
                labels[row] = row
        columns_order = list(labels.keys())
        grid += "<thead>"
        for key, label in labels.iteritems():
            grid += "<th>"
            if sorting:
                grid += "<a href='"
                grid += sorting + key
                grid += "'>"
                grid += label
                grid += "</a>"
            else:
                grid += label
            grid += "</th>"
        if actions:
            grid += "<th class='button-column'>&nbsp;</th>"
        grid += "</thead>"
        grid += "<tbody>"
        for row in data:
            grid += "<tr class='odd'>"
            for key in columns_order:
                grid += "<td>"
                grid += str(row[key])
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
