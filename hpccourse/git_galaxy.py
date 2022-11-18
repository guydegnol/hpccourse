def get_git_galaxy_log_graph(nodenum):

    import graphviz

    changes = [
        ["master", "0,0!", "boris", [2, 1]],  # 0
        ["casting", "1,1!", "groot", [3]],  # 1
        ["master", "2.5,0!", "Je m'appelle boris", [4, 5]],  # 2
        ["casting", "4,1!", "groot!", [5]],  # 3
        ["bernard_pivot", "3.6,-1!", "Je s'appelle boris", [6]],  # 4
        ["master", "5.5,0!", "Je m'appelle groot!", [6]],  # 5
        ["master", "9,0!", "Je s'appelle groot!", []],  # 6
    ]

    digraph = graphviz.Digraph(engine="neato")
    digraph.graph_attr["rankdir"] = "LR"

    colors = {"master": "#F67280", "casting": "#355C7D", "bernard_pivot": "#6C5B7B"}

    digraph.node(
        "master", fontsize="20", pos="0,-0.5!", fontcolor=colors["master"], shape="none", fontname="Comic Sans MS"
    )
    digraph.node(
        "casting", fontsize="20", pos="1.1,1.5!", fontcolor=colors["casting"], shape="none", fontname="Comic Sans MS"
    )
    digraph.node(
        "bernard_pivot",
        fontsize="20",
        pos="3.6,-1.5!",
        fontcolor=colors["bernard_pivot"],
        shape="none",
        fontname="Comic Sans MS",
    )

    for n, change in enumerate(changes):
        branch, pos, label, edge = change
        args = dict(
            fontsize="10",
            style="filled",
            fontcolor="white",
            fontname="Comic Sans MS",
            shape="rectangle",
            fillcolor=colors[branch],
        )

        if n > nodenum:
            args.update(dict(fontcolor=colors[branch], fillcolor=colors[branch]))
        elif n == nodenum:
            args.update(dict(fontcolor="yellow", color="yellow", fillcolor="red", fontsize="10"))
        digraph.node(label, pos=pos, **args)

    for n, change in enumerate(changes):
        for e in change[3]:
            digraph.edge(changes[n][2], changes[e][2], color="grey")

    digraph.render()
    return digraph
