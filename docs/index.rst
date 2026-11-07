Python package guide
====================

This project starts with a small, tested Python package. Replace the greeting
with your own public API and keep its tests and documentation alongside it.

Public API
----------

.. automodule:: python_controls_local
   :members:

CI and build outputs
--------------------

The repository's Actions page contains separate Python and documentation runs.
The Python workflow tests and builds a wheel, then installs that exact wheel in
a fresh consumer job. The documentation workflow saves the generated HTML as
an artifact. Download and extract that artifact, then open ``index.html``.
