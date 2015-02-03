#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Element(object):
    """Base element of HTML"""

    tag_name = 'html'
    content = []
    indent = 1

    def __init__(self, content=None):
        self.content.append(content)

    def append(self, content):
        """Append content to the element"""
        self.content.append(content)
        return self.content

    def render(self, file_out, ind="  "):
        """Render tag and string in the content. file_out is a file object"""
        for line in self.content:
            if isinstance(line, Element):
                ind += ind
                self.render(file_out, ind)
            file_out.write('<' + self.tag_name + '>\n')
            if line:
                file_out.write(ind + line + "\n")
            file_out.write('<' + self.tag_name + '/>\n')
        return


class Html(Element):
    """html element"""

    tag_name = 'html'


class Body(Element):
    """Body element"""

    tag_name = 'body'


class P(Element):
    """P element"""

    tag_name = 'p'
