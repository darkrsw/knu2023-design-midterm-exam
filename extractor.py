import ast
import sys
from ast import NodeVisitor

def init_metrics(avisitor):
    return {'num_total_if': len(avisitor.iflist), 
            'max_nested_if': avisitor.max_nested_if, 
            'num_total_for': len(avisitor.forlist), 
            'max_nested_for': avisitor.max_nested_for}

def collect_function_structure(path: str):
    with open(path, "r") as f:
        source = f.read()

    myast = ast.parse(source)

    cvisitor = ClassVisitor()
    #fvisitor = FunctionVisitor()
    #forifvisitor = ForIfVisitor()

    cvisitor.visit(myast)
    clist = cvisitor.getClasses()

    ret_map = {}

    for aclass in clist:
        fvisitor = FunctionVisitor()
        fvisitor.visit(aclass)
        flist = fvisitor.getFunctions()
        ret_map[aclass.name] = {}

        for afunc in flist:
            forifvisitor = ForIfVisitor()
            forifvisitor.visit(afunc)
            ret_map[aclass.name][afunc.name] = init_metrics(forifvisitor)

    return ret_map

class ClassVisitor(NodeVisitor):
    def __init__(self):
        super().__init__()
        self.clist = []

    def visit_ClassDef(self, node):
        self.clist.append(node)
        return super().generic_visit(node)

    def getClasses(self):
        return self.clist


class FunctionVisitor(NodeVisitor):
    def __init__(self):
        super().__init__()
        self.flist = []

    def add_node(self, node):
        self.flist.append(node)

    def visit_FunctionDef(self, node):
        self.add_node(node)
        return super().generic_visit(node)

    def visit_AsyncFunctionDef(self, node):
        self.add_node(node)
        return super().generic_visit(node)

    def getFunctions(self):
        return self.flist


class ForIfVisitor(NodeVisitor):
    def __init__(self):
        super().__init__()
        self.iflist = []
        self.forlist = []
        self.cur_nested_if = 0
        self.cur_nested_for = 0
        self.max_nested_if = 0
        self.max_nested_for = 0

    def visit_If(self, node):
        self.iflist.append(node)
        self.cur_nested_if += 1
        self.max_nested_if = max(self.cur_nested_if, self.max_nested_if)
        r = super().generic_visit(node)
        self.cur_nested_if -= 1
        return r

    def visit_For(self, node):
        self.forlist.append(node)
        self.cur_nested_for += 1
        self.max_nested_for = max(self.cur_nested_for, self.max_nested_for)
        r = super().generic_visit(node)
        self.cur_nested_for -= 1
        return r


if __name__ == "__main__":
    r = collect_function_structure(sys.argv[1])
    print(r)
