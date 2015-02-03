#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Element(object):
    """Base element of HTML"""

    tag_name = 'html'
    indent_lvl = 1
    content = []

    def __init__(self, content=""):
        self.content.append(content)

    def append(self, content):
        """Append content to the element"""
        self.content.append(content)
        return self.content

    def render(self, file_out, ind="  "):
        """Render tag and string in the content. file_out is a file object"""
        file_out.write('<' + self.tag_name + '>\n')
        for line in self.content:
            file_out.write(ind * self.indent_lvl + line + "\n")
            if self.indent_lvl > 1:
                self.render(file_out)
        file_out.write('<' + self.tag_name + '/>\n')
        return


class Html(Element):
    """Body element"""

    tag_name = 'html'


class Body(Element):
    """Body element"""

    tag_name = 'body'


class P(Element):
    """P element"""

    tag_name = 'p'
