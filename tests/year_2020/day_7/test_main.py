from puzzles.year_2020.day_7 import main

from .data import DUMMY_RULES_PARSED, DUMMY_RULES_RAW


def test_find_how_many_bags_can_contain_colour():
    dummy_target_colour = "shiny gold"
    assert (
        main.find_how_many_bags_can_contain_colour(
            rules=DUMMY_RULES_PARSED, target_colour=dummy_target_colour
        )
        == 5
    )


def test_can_colour_be_in_bag_true():

    dummy_parent = "dark orange"
    dummy_target_colour = "shiny gold"

    assert (
        main.can_colour_be_in_bag(
            rules=DUMMY_RULES_PARSED,
            parent=dummy_parent,
            target_colour=dummy_target_colour,
        )
        is True
    )


def test_can_colour_be_in_bag_false():

    dummy_parent = "dark olive"
    dummy_target_colour = "shiny gold"

    assert (
        main.can_colour_be_in_bag(
            rules=DUMMY_RULES_PARSED,
            parent=dummy_parent,
            target_colour=dummy_target_colour,
        )
        is False
    )


def test_parse_all_rules():
    assert main.parse_all_rules(DUMMY_RULES_RAW) == DUMMY_RULES_PARSED


def test_parse_rule_multiple():
    actual = main.parse_rule(DUMMY_RULES_RAW[0])
    expected = main.Rule(
        parent="light red",
        children=[
            main.Child(name="bright white", count=1),
            main.Child(name="muted yellow", count=2),
        ],
    )
    assert actual == expected


def test_parse_rule_single():
    actual = main.parse_rule(DUMMY_RULES_RAW[2])
    expected = main.Rule(
        parent="bright white",
        children=[
            main.Child(name="shiny gold", count=1),
        ],
    )
    assert actual == expected


def test_parse_rule_none():
    actual = main.parse_rule(DUMMY_RULES_RAW[7])
    expected = main.Rule(parent="faded blue", children=None)
    assert actual == expected
