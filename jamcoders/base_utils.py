# For comparison of answers
def assert_equal(want, got):

    if want == got or (type(want) == float and type(got) == float and abs(want - got) < 0.001):
        print("Test case passed.")
        return

    print()
    print("--------- Test case failed. ---------")
    print(f"Want: {repr(want)} (type: {type(want).__name__})")
    print(f"Got:  {repr(got)} (type: {type(got).__name__})")
    print("-------------------------------------")
    print()