import pytest
from render import virtual_shadow as mod

CASES = [
    ("pages_two", "m.page_count(100, 64) == 2"),
    ("pages_zero", "m.page_count(0, 64) == 1"),
    ("key_pair", "m.page_key(7, 2) == (7, 2)"),
    ("migrate_pair", "m.migrate_page(5, 3) == (5, 3)"),
    ("bounds_sum", "m.tight_bounds(1, 2) == 3"),
    ("bone_mid", "m.bone_sample(0.5, 30) == 15"),
    ("expired_true", "m.expired(1, 20, 5) is True"),
    ("expired_false", "m.expired(18, 20, 5) is False"),
    ("mask_true", "m.mask_depth(0.5) is True"),
    ("mask_false", "m.mask_depth(0.0) is False"),
    ("pool_id", "m.page_pool(1) == 1"),
    ("precision_far", "m.distance_precision(10, 1) == approx(0.1)"),
    ("precision_near", "m.distance_precision(1, 1) == approx(1.0)"),
    ("pages_large", "m.page_count(1000, 64) == 16"),
    ("bone_zero", "m.bone_sample(0.0, 30) == 0")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
