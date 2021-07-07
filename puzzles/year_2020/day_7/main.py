import dataclasses
from typing import Dict, List, Optional

from .data import RULES


@dataclasses.dataclass
class Child:
    name: str
    count: int


@dataclasses.dataclass
class Rule:
    parent: str
    children: Optional[List[Child]]


def find_how_many_bags_can_contain_colour(
    rules: Dict[str, Optional[List[Child]]], target_colour: str
) -> int:
    count = 0
    for parent in rules.keys():
        if can_colour_be_in_bag(
            rules=rules,
            parent=parent,
            target_colour=target_colour,
        ):
            count += 1
    return count


def can_colour_be_in_bag(
    rules: Dict[str, Optional[List[Child]]],
    parent: str,
    target_colour: str,
) -> bool:

    children = rules[parent]
    if not children:
        return False  # For bags that can't contain other bags
    if parent == target_colour:
        return False  # A bag can't contain itself

    for child in children:
        if child.name == target_colour:
            return True  # For when the target colour is in the current bag
        if can_colour_be_in_bag(
            rules=rules,
            parent=child.name,
            target_colour=target_colour,
        ):
            return True  # For when the target colour can be found eventually
    return False  # For when the target colour cannot be found eventually


def parse_all_rules(rules: List[str]) -> Dict[str, Optional[List[Child]]]:
    parsed_rules = {}
    for rule in rules:
        parsed_rule = parse_rule(rule=rule)
        parsed_rules[parsed_rule.parent] = parsed_rule.children
    return parsed_rules


def parse_rule(rule: str) -> Rule:

    split_string = rule.split(" bags contain ")

    parent = split_string[0]
    unparsed_children = split_string[1]

    if unparsed_children == "no other bags.":
        return Rule(
            parent=parent,
            children=None,
        )

    unparsed_children = unparsed_children.replace(".", "")
    unparsed_children = unparsed_children.replace(" bags", "")
    unparsed_children = unparsed_children.replace(" bag", "")

    split_unparsed_children = unparsed_children.split(", ")

    children = []

    for child in split_unparsed_children:
        split_child = child.split(" ")
        children.append(
            Child(
                name=" ".join(split_child[1:]),
                count=int(split_child[0]),
            )
        )
    return Rule(
        parent=parent,
        children=children,
    )


def main() -> None:
    TARGET_COLOUR = "shiny gold"
    rules = parse_all_rules(rules=RULES)
    result = find_how_many_bags_can_contain_colour(
        rules=rules, target_colour=TARGET_COLOUR
    )
    print(f"{TARGET_COLOUR} bags can eventually be contained by {result} bags")


if __name__ == "__main__":
    main()
