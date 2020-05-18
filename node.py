from tome_iii_lvl_i import weights
def get_node_details(node_type):
    if node_type is "start":
        return {
            "style": ">",
            "weight": 0
        }
    elif node_type is "end":
        return {
            "style": "<",
            "weight": 0
        }
    elif node_type is "small":
        return {
            "style": "d",
            "weight": weights[0]
        }
    elif node_type is "large":
        return {
            "style": "s",
            "weight": weights[1]
        }
    else:
        return {
            "style": "o",
            "weight": 0
        }