import os
import sys

# Adds "practice_python" to sys.path
# Now you can do import with "from practice_python.Sub-Package ..."
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "practice_python"))
)
