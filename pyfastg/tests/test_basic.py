from pyfastg import parse_fastg


def test_parse_medium_assembly_graph():
    digraph = parse_fastg("pyfastg/tests/input/assembly_graph.fastg")
    assert len(digraph.nodes) == 66
    assert len(digraph.edges) == 86
    for i in range(1, 34):
        si = str(i)
        assert si + "+" in digraph.nodes
        assert si + "-" in digraph.nodes


def test_parse_small_assembly_graph():
    digraph = parse_fastg("pyfastg/tests/input/small.fastg")
    assert len(digraph.nodes) == 6
    assert len(digraph.edges) == 8
    i2length = {1: 9, 2: 3, 3: 5}
    i2cov = {1: 4.5, 2: 100, 3: 16.5}
    for i in range(1, 4):
        si = str(i)
        for suffix in ("+", "-"):
            name = si + suffix
            assert name in digraph.nodes
            assert digraph.nodes[name]["coverage"] == i2cov[i]
            assert digraph.nodes[name]["length"] == i2length[i]

    valid_edges = (
        ("2+", "1+"),
        ("2+", "3-"),
        ("2+", "3+"),
        ("1+", "3-"),
        ("3-", "2-"),
        ("3+", "1-"),
        ("3+", "2-"),
        ("1-", "2-"),
    )
    for e in valid_edges:
        assert e in digraph.edges
