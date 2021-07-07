# flake8: noqa (to prevent line length warnings)
from puzzles.year_2020.day_7.main import Child

DUMMY_RULES_RAW = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 9 faded blue bags, 2 shiny gold bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 1 bright white bag, 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags.",
]

DUMMY_RULES_PARSED = {
    "light red": [
        Child(name="bright white", count=1),
        Child(name="muted yellow", count=2),
    ],
    "dark orange": [
        Child(name="bright white", count=3),
        Child(name="muted yellow", count=4),
    ],
    "bright white": [Child(name="shiny gold", count=1)],
    "muted yellow": [
        Child(name="faded blue", count=9),
        Child(name="shiny gold", count=2),
    ],
    "shiny gold": [
        Child(name="dark olive", count=1),
        Child(name="vibrant plum", count=2),
    ],
    "dark olive": [
        Child(name="faded blue", count=3),
        Child(name="dotted black", count=4),
    ],
    "vibrant plum": [
        Child(name="bright white", count=1),
        Child(name="faded blue", count=5),
        Child(name="dotted black", count=6),
    ],
    "faded blue": None,
    "dotted black": None,
}
