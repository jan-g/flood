import heapq


def make_grid(lines):
    return {(x, y): int(c)
            for y, line in enumerate(lines)
            for x, c in enumerate(line)}


def ungrid(grid):
    xs = {x for (x, y) in grid}
    ys = {y for (x, y) in grid}
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    return ["".join(str(grid[x, y]) for x in range(minx, maxx + 1)) for y in range(miny, maxy + 1)]


def neighbours(coord):
    (x, y) = coord
    return {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}


def solve(grid):
    levels = dict(grid)
    unvisited = set(grid.keys())

    while len(unvisited) > 0:
        loc = unvisited.pop()
        visited = {loc}
        level = grid[loc]
        front = Heap([(level, loc)])
        while True:
            if len(front) > 0 and 0 <= front.first[0] < level:
                expand(grid, front, visited)
                continue

            levels[loc] = level

            if len(front) > 0 and front.first[0] == -1:
                # We've reached a sinkhole, so stop, because we can't go any higher
                break

            if len(front) == 0:
                break

            # Reached a natural pause; try raising the level
            level = front.first[0]
            locs = []

            # We expand the front of search from everywhere that meets this level
            while len(front) > 0 and front.first[0] == level:
                locs.append(xy := front.pop()[1])
                visited.add(xy)

            for xy in locs:
                for xy2 in neighbours(xy):
                    if xy2 not in visited:
                        front.push((grid.get(xy2, -1), xy2))

    return levels


def expand(grid, heap, visited):
    """Pull the first location off the heap and push its neighbours on"""
    (level, loc) = heap.pop()
    visited.add(loc)
    for xy in neighbours(loc):
        if xy not in visited:
            heap.push((grid.get(xy, -1), xy))


class Heap:
    def __init__(self, items, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._h = list(items)

    def push(self, item):
        heapq.heappush(self._h, item)

    def pop(self):
        return heapq.heappop(self._h)

    @property
    def first(self):
        return self._h[0]

    def __len__(self):
        return len(self._h)
