"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    incoming_list = [1,7,2,9,22]
    find_greatest_number = max(incoming_list)
    pass


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    incoming_list = [1,7,2,9,22]
    incoming_list.sort()
    find_least_number = incoming_list[:1]
    
    pass


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    incoming_list[1,7,2,9,22]
    sum(incoming_list)
    add_list_numbers = sum(incoming_list)
    pass



def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    incoming_dict = {"names": "sam", "locations": "virginia"}
    maxkey = max(incoming_dict, key=incoming_dict.len())
    longest_value_key = maxkey
    pass
