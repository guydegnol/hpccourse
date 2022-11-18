import graphviz

from .git_graphviz import Node, Nodes, Branch


def get_nodes(name):
    if name == "galaxy":
        return Nodes(
            [
                Node(label="1", branch="master", pos=0, destination="2", style="<"),
                Node(label="2", branch="master", pos=1.1, destination="3", style="<"),
                Node(label="3", branch="master", pos=3, destination="4", style=">"),
                Node(label="4", branch="master", pos=4, style=">,dashed,purple"),
                Node(label="A", branch="casting", pos=1, destination="B", origin="1"),
                Node(label="B", branch="casting", pos=2, destination="3"),
                Node(label="Z", branch="bernard_pivot", pos=2.6, destination="4", origin="2"),
            ]
        )
    if name == "premerge":
        return Nodes(
            [
                Node(label="1", branch="master", pos=0, destination="2", style="<"),
                Node(label="2", branch="master", pos=1, destination="3"),
                Node(label="3", branch="master", pos=2),
                Node(label="A", branch="feature", pos=1, destination="B", origin="1"),
                Node(label="B", branch="feature", pos=2),
            ]
        )
    if name == "merge":
        return Nodes(
            [
                Node(label="1", branch="master", pos=0, destination="2", style="<"),
                Node(label="2", branch="master", pos=1, destination="3"),
                Node(label="3", branch="master", pos=2, destination="4"),
                Node(label="4", branch="master", pos=3, style=">,dashed,purple"),
                Node(label="A", branch="feature", pos=1, destination="B", origin="1"),
                Node(label="B", branch="feature", pos=2, destination="4"),
            ]
        )
    if name == "rebase":
        return Nodes(
            [
                Node(label="1", branch="master", pos=0, destination="2", style="<"),
                Node(label="2", branch="master", pos=1, destination="3"),
                Node(label="3", branch="master", pos=2, destination="A"),
                Node(label="A", branch="master", pos=3, destination="B"),
                Node(label="B", branch="master", pos=4, destination="4"),
                Node(label="4", branch="master", pos=5, style=">,dashed,purple"),
            ]
        )


def get_git_graph(nodes, branches=None, cpos=None, title=None):

    if type(nodes) == str:
        nodes = get_nodes(nodes)

    if branches is None:
        branches = {
            "master": Branch(color="#F67280", pos=0),
            "feature": Branch(color="#355C7D", pos=1),
            "fix_bug": Branch(color="#6C5B7B", pos=-1),
            "fix_bug2": Branch(color="#F8B195", pos=2),
            "fix_bug3": Branch(color="#C06C84", pos=-2),
            "casting": Branch(color="#355C7D", pos=1),
            "bernard_pivot": Branch(color="#6C5B7B", pos=-1),
        }

    nodes.update_with_style()

    digraph = graphviz.Digraph(engine="neato")
    digraph.graph_attr["rankdir"] = "LR"
    if title:
        digraph.graph_attr["labelloc"] = "t"
        digraph.graph_attr["label"] = title

    for n in nodes.nodes:
        b = branches[n.branch]
        b.title(n, digraph)

        digraph.node(n.label, **nodes.get_node_style(n, b, cpos))
        if n.origin:
            digraph.edge(n.origin, n.label, **nodes.get_edge_style(n.label, n.origin, cpos))
        if n.destination:
            digraph.edge(n.label, n.destination, **nodes.get_edge_style(n.label, n.destination, cpos))

    digraph.render()
    return digraph
