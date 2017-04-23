# -*- coding: utf-8 -*-
"""
Tabs Extension for Python-Markdown
==================================

License: GPLv3 or later
"""

from __future__ import unicode_literals

# import logging
import markdown
from markdown.util import etree

# logger = logging.getLogger(__name__)


class TabExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.parser.blockprocessors.add(
            'tabs',
            TabsProcessor(md.parser),
            '<hashheader'
        )


def makeExtension(configs={}):
    return TabExtension(configs=configs)


class Tab:
    ID_NAME = "tabs-processor-id-"

    def __init__(self, group_id, id, default=False):
        self.title = ""
        self.text = ""
        self.id = self.ID_NAME + str(id)
        self.group_id = self.ID_NAME + str(group_id)
        self.default = default

    def print(self):
        print("Tab: '" + self.title + "' Text: '" + self.text + "'")


class TabsProcessor(markdown.blockprocessors.BlockProcessor):
    def __init__(self, parser):
        super(TabsProcessor, self).__init__(parser)
        self.id_counter = 0

    def test(self, parent, block):
        return block.startswith(":Tab:")

    def run(self, parent, blocks):
        #print("run")
        group_id = self.get_new_id()
        tab_blocks = []
        for b in blocks:
            tab_blocks.append(b)
            if b.endswith(":TabsEnd:"):
                break

        for b in tab_blocks:
            blocks.pop(0)

        #print(tab_blocks)
        # Get tabs
        tabs = []
        first_tab = True
        for b in tab_blocks:
            b_striped = b.strip()
            if b_striped.startswith(":Tab:"):
                rows = [r.strip() for r in b_striped.split('\n')]
                assert rows[0].startswith(":Tab:")
                tab = Tab(group_id, self.get_new_id())
                tab.title = rows[0][5:].strip()
                tab.text = '\n'.join(rows[1:])
                if first_tab:
                    first_tab = False
                    tab.default = True
                tabs.append(tab)
            elif b_striped.endswith(":TabsEnd:"):
                # We are continuing the previous tab
                tabs[-1].text += '\n\n' + b_striped[:-9]
            else:
                # We are continuing the previous tab
                tabs[-1].text += '\n\n' + b

        #for t in tabs:
        #    t.print()

        # Generate output
        tabs_div = etree.SubElement(parent, 'div')
        tabs_div.set("class", "tab")
        for t in tabs:
            self.add_button(tabs_div, t)
        for t in tabs:
            self.add_content(parent, t)

    def add_button(self, div_parent, tab):
        tab_button = etree.SubElement(div_parent, 'button')
        default = ""
        if tab.default:
            default = " default_open"
        tab_button.set('class', 'tablinks ' + tab.group_id + default)
        tab_button.set(
            'onclick',
            "openTab(event, '" + tab.group_id + "', '" + tab.id + "')"
        )
        tab_button.text = tab.title

    def add_content(self, parent, tab):
        tab_content = etree.SubElement(parent, 'div')
        tab_content.set('id', tab.id)
        tab_content.set('class', 'tabcontent ' + tab.group_id)
        self.parser.parseChunk(tab_content, tab.text)

    def get_new_id(self):
        id = self.id_counter
        self.id_counter += 1
        return id
