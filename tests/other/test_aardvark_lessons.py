from practice_python.other.aardvark_lessons import minimal_partition, earliest_unique_elements


class TestMinimalPartition:
    def test_example1(self):
        assert minimal_partition([3,1,2,4,3]) == 1

    def test_example2(self):
        assert minimal_partition([3,4,2,1,3]) == 1

    def test_example3(self):
        assert minimal_partition([7,-1,9,0,0,3,3]) == 7

    def test_example4(self):
        assert minimal_partition([3,3,0,0,9,-1,7]) == 7

    def test_example5(self):
        assert minimal_partition([-1,1]) == 2

    def test_example6(self):
        assert minimal_partition([1,-1]) == 2

    def test_example7(self):
        assert minimal_partition([0,0]) == 0

    def test_example8(self):
        assert minimal_partition([-3,-4,-2,-1,-3]) == 1

    def test_example9(self):
        assert minimal_partition([1,-1,-1,0,0,1,-1,-1,0,1,0,1,0,-1,1]) == 0


class TestEarliestUniqueElements:
    def test_example1(self):
        assert earliest_unique_elements([5,3,1,2,4,3], 4) == 4

    def test_example2(self):
        assert earliest_unique_elements([7,6,5,4,3,2,1], 5) == 6

    def test_example3(self):
        assert earliest_unique_elements([1,2,3,4,5],5) == 4

    def test_example4(self):
        assert earliest_unique_elements([5,3,1,2,3], 4) == -1

class TestFindLastMaxCommand:
    def test_example1(self):
        assert earliest_unique_elements([5,3,1,2,4,3], 4) == 4