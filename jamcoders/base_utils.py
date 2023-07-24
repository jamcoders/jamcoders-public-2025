import base64

class NotebookTracking:
    tracker = None

    @classmethod
    def is_active(cls):
        return cls.tracker != None
    
    @classmethod
    def set_activation(cls, is_active):
        if is_active:
            # Importing notebook_tracker_client triggers a "!pip install", and imports google.colab,
            #   both of which can fail if executed in the wrong environment (e.g., not not colab). #   Therefore, we perform this import only if and when notebook tracking is enabled.  
            from notebook_tracking_client import NotebookTracker
            cls.tracker = NotebookTracker()
            cls.tracker.init()
        else:
            cls.tracker = None


# For comparison of answers
def assert_equal(want, got):

    assert_passed = (want == got or (type(want) == float and type(got) == float and abs(want - got) < 0.001))

    if NotebookTracking.is_active():
        NotebookTracking.tracker.send_assertion_event(assert_passed)

    if assert_passed:
        print("Test case passed.")
    else:
        print()
        print("--------- Test case failed. ---------")
        print(f"Want: {repr(want)} (type: {type(want).__name__})")
        print(f"Got:  {repr(got)} (type: {type(got).__name__})")
        print("-------------------------------------")
        print()


# Encodes ASCII string to base64
def encode_base64(str):
    message = str
    message_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode("ascii")
    return base64_message


# Decodes base64 to ASCII string
def decode_base64(b64):
    base64_message = b64
    base64_bytes = base64_message.encode("ascii")
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode("ascii")
    return message


DEBUGGABLE_ARGS = "_debuggable_args"
DEBUGGABLE_KWARGS = "_debuggable_kwargs"

def debuggable(f):
    @functools.wraps(f)
    def g(*args, **kwargs):
        try:
            args_copy = copy.deepcopy(args)
            kwargs_copy = copy.deepcopy(kwargs)
        except Exception:
            args_copy = None
            kwargs_copy = None
        result = f(*args, **kwargs)
        setattr(g, DEBUGGABLE_ARGS, args_copy)
        setattr(g, DEBUGGABLE_KWARGS, kwargs_copy)
        return result
    return g