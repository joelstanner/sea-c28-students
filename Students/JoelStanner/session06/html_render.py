#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Element(object):
    """Base element of HTML"""

    def __init__(self, tag_name="HTML", ind=0, content=""):
        indent = 0

        self.tag_name = tag_name
        self.ind = ind + indent
        self.content = content

    def append(self, content):
        """Append content to the element"""
        self.content += content
        return self.content

    def render(self, file_out, ind=""):
        """Render tag and string in the content"""
        self.file_out = file_out
        self.ind = ind
        return
