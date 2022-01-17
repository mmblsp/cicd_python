from webcount import most_common_word


def test_most_common_word():
    assert most_common_word(['a', 'b', 'c', 'd'], 'abbbcc') \
        == 'b', 'most_common_word with unique asnwer'

def test_most_common_word_empty_candidate():
    from pytest import raises
    with raises(Exception):
        most_common_word([], 'abc')

def test_most_common_ambiguous_result():
    assert most_common_word(['a', 'b', 'c'], 'ab') \
        in ('a', 'b'), "there might be a tie"