import pytest


def test_change_age(create_human):
    human = create_human
    new_age = 55
    human.grow()
    assert human.age == new_age, "No changes age"


def test_become_dead(create_human_dead):
    human = create_human_dead
    human.grow()
    with pytest.raises(Exception):
        human.grow()


def test_dead_age(create_human):
    human = create_human
    new_age = 120
    human.grow()
    assert human.age == new_age + 1, 'Human dead'


def test_change_gender(create_human):
    human = create_human
    new_gender = 'male'
    human.change_gender('male')
    assert human.gender == new_gender, "No changes gender"


def test_get_uncorrect_gender(create_human):
    human = create_human
    new_gender = 'femaalle'
    human.change_gender(new_gender)
    assert human.gender == new_gender, 'Uncorrect gender'


def test_human_unborn(create_human):
    human = create_human
    new_age = -2
    human.grow()
    assert human.age == new_age + 1, 'Human is live'
