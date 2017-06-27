import pytest
import word_count

def test_wc():
    assert word_count.count_words(['a', 'a', 'c', 'c', 'd']) == \
       {'a':2, 'c':2, 'd': 1}
    
    assert word_count.count_words([]) == \
       {}
       
def test_numbers():
    assert word_count.count_words([1,2,3,4,1,2,2]) == \
       {1:2,2:3,3:1,4:1}    