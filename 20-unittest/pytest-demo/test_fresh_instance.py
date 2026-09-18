# test_fresh_instance.py
# Does 'self' carry data from one test to the next?

class TestFreshInstance:

    # Step 1 - Store something on self in the first test
    def test_first(self):
        self.note = "set in test_first"
        print("\ntest_first stored:", self.note)
        assert self.note == "set in test_first"

    # Step 2 - Look for it in the second test
    def test_second(self):
        found = hasattr(self, "note")
        print("\ntest_second can see 'note'?", found)
        assert found is False
