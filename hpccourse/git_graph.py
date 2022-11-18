import graphviz


class Node:
    def __init__(self, label="", branch="master", edges=[], style="", pos=None):
        self.label, self.branch, self.edges, self.style, self.pos = label, branch, edges, style, pos


class Nodes:
    def __init__(self, nodes):
        self.nodes = nodes

    def get_range(self):
        return range(len(self.nodes))

    def replace_node(self, previous, next):
        range = self.get_range()
        for i in range:
            if previous in self.nodes[i].edges:
                self.nodes[i].edges = [e.replace(previous, next) for e in self.nodes[i].edges]

    def update_with_style(self):
        range = self.get_range()
        for i in range:
            if self.nodes[i].style == "<":
                n = Node(
                    label=self.nodes[i].label + "i",
                    branch=self.nodes[i].branch,
                    pos=self.nodes[i].pos + 0.5,
                    edges=self.nodes[i].edges,
                    style="point",
                )
                self.nodes[i].edges = [n.label]
                self.nodes.append(n)
            elif self.nodes[i].style == ">":
                n = Node(
                    label=self.nodes[i].label + "i",
                    branch=self.nodes[i].branch,
                    pos=self.nodes[i].pos - 0.5,
                    edges=[self.nodes[i].label],
                    style="point",
                )
                self.replace_node(self.nodes[i].label, n.label)
                self.nodes.append(n)

    def get_edge_style(self, label1, label2):
        style = "solid"
        for n in self.nodes:
            if n.label in [label1, label2] and "dashed" in n.style:
                print(n.style)
                style = "dashed"
        return dict(color="grey", arrowhead="none", style=style)

    def get_node_style(self, node, branch):
        if "purple" in node.style:
            color = "#C06C84"  # 6C5B7B F8B195 C06C84
        elif node.label in "123456789" or "red" in node.style:
            color = "#F67280"  # 6C5B7B F8B195 C06C84
        elif node.label in "ABCDE" or "blue" in node.style:
            color = "#355C7D"  # 6C5B7B F8B195 C06C84
        else:
            color = branch.color

        pos = str(node.pos) + "," + str(branch.pos) + "!"
        args = dict(
            fontsize="10",
            style="filled",
            fontcolor="white",
            fontname="Comic Sans MS",
            shape="circle",
            fillcolor=color,
            pos=pos,
        )
        if node.style == "point":
            args = dict(fontcolor="white", shape="point", color="grey", pos=pos)
        return args


class Branch:
    def __init__(self, label="master", color="master", pos=0):
        self.label, self.color, self.pos = label, color, pos
        self.show_title = True

    def title(self, node, digraph):
        if self.show_title:
            pos = self.pos - 0.5 if self.pos < 0 else self.pos + 0.5
            bpos = str(node.pos) + "," + str(pos) + "!"
            digraph.node(
                node.branch, fontsize="20", pos=bpos, fontcolor=self.color, shape="none", fontname="Comic Sans MS"
            )
            self.show_title = False


def get_git_graph(nodes, branches=None):

    if branches is None:
        branches = {
            "master": Branch(color="#F67280", pos=0),
            "feature": Branch(color="#355C7D", pos=1),
            "fix_bug": Branch(color="#6C5B7B", pos=-1),
            "fix_bug2": Branch(color="#F8B195", pos=2),
            "fix_bug3": Branch(color="#C06C84", pos=-2),
        }

    githist.update_with_style()

    digraph = graphviz.Digraph(engine="neato")
    digraph.graph_attr["rankdir"] = "LR"

    for n in nodes.nodes:
        b = branches[n.branch]
        b.title(n, digraph)

        digraph.node(n.label, **nodes.get_node_style(n, b))

        for e in n.edges:
            digraph.edge(n.label, e, **nodes.get_edge_style(n.label, e))

    digraph.render()
    return digraph
