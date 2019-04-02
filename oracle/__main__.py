"""
Scraping tools for annwn html data
"""
import os
from bs4 import BeautifulSoup as bs

def item_parser(item_html):
    """ Parser for HTML documents representing an item

    TODO: non-lazy-ass parse. Scrape out more attributes beyond name and type.

    Arguments:
    -----------
    item_html: raw HTML string representing a single item to be parsed.

    Returns:
    --------
    dict with keys as attribute names (e.g. column names), and values as data
    specific to the given item.
    """
    attribute_sequence = ['item_name', 'item_type']
        # 'alignment', 'material', 'keyword_list_space_delim', 'weight_stones',
        # 'weight_pebbles', 'value, attributes_list_space_delim'
    doc = bs(item_html, 'html.parser')
    item = doc.find_all('div', class_="mm")
    data = [] if not item else item[0].find_all('span')
    if data == []:
        return None
    return {attribute_sequence[i]: data[i].text for i in range(2)}

def quest_parser(quest_html):
    """
    # TODO: parse these bad boys
    """
    doc = bs(quest_html, 'html.parser')
    quest = doc.find_all('div', class_="mm")
    return None

def area_parser(area_html):
    """
    # TODO: get our parse on
    """
    return None

def npc_parser(npc_html):
    """
    # TODO: lovingly parse each mob
    """
    return None

def iter_dir(root_path, handler):
    """
    Walks through each file in the given directory, opens it, and uses the given
    `handler` function to parse the file.

    Arguments:
    -----------
    root_path: string representing the path of the root folder containing HTML
    documents to be parsed.
    hanlder: function (callback) to apply to each file in the given directory.
    """
    data = {}
    for root, _dirs, files in os.walk(root_path):
        for name in files:
            with open(root + name) as document:
                data.update({name: handler(document)})
    return data

def main():
    """
    Identifies data types and parsers (AKA handlers), and dispatches them
    through `iter_dir` to be parsed.

    Instead of printing the JSON string, it should either write to a file or a
    local database. Could also be turned into a CLI.
    """
    root_folder = 'test_data/'
    data_sets = {
        'items': item_parser,
        'areas': area_parser,
        'quests': quest_parser,
        'npcs': npc_parser
    }
    json_data = {}

    for file_path, handler in data_sets.items():
        json_data[file_path] = iter_dir(root_folder + file_path + '/', handler)
    print(json_data)

if __name__ == '__main__':
    main()
