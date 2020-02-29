from .solve import make_grid, solve, ungrid


def tidy(g):
    return "\n".join(out for line in g.split("\n") if (out := line.strip()) != "")


def test_basic():
    layout = tidy("""
            00000
            01110
            01010
            01110
            00000
            """)

    expected = tidy("""
            00000
            01110
            01110
            01110
            00000
            """)

    grid = make_grid(layout.split("\n"))
    ans = solve(grid)
    assert "\n".join(ungrid(ans)) == expected


def test_two():
    layout = tidy("""
            0000000000
            0111000000
            0101000000
            0111000000
            0000000000
            0000000000
            0000005550
            0000002040
            0000004440
            0000000000
            """)

    expected = tidy("""
            0000000000
            0111000000
            0111000000
            0111000000
            0000000000
            0000000000
            0000005550
            0000002240
            0000004440
            0000000000
            """)

    grid = make_grid(layout.split("\n"))
    ans = solve(grid)
    assert "\n".join(ungrid(ans)) == expected


def test_three():
    layout = tidy("""
            9898989898
            9451682739
            8989898819
            9451682739
            9389889898
            9451682739
            8989898819
            9451682739
            9000004449
            9999999999
            """)

    expected = tidy("""
            9898989898
            9888888889
            8989898889
            9888888889
            9889889898
            9888888889
            8989898889
            9888888889
            9888888889
            9999999999
            """)

    grid = make_grid(layout.split("\n"))
    ans = solve(grid)
    assert "\n".join(ungrid(ans)) == expected
