#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Element(object):
    """Base element of HTML"""

    indent = 0

    def __init__(self, tag_name="", ind=0, content=""):

        self.tag_name = tag_name
        self.indent = ind
        self.content = content

    def append(self, content):
        """Append content to the element"""
        self.content += content
        return self.content

    def render(self, file_out, ind=""):
        """Render tag and string in the content"""
        print("<", self.tag_name, ">")
        self.file_out = file_out
        self.ind = ind
        return
