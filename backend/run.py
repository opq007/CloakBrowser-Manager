"""Windows-friendly development server entry point.

Run from the repository root:

    python backend/run.py

On Windows, uvicorn's --reload mode uses a SelectorEventLoop, which cannot
start Playwright's driver subprocess. This entry point avoids reload so uvicorn
uses a ProactorEventLoop.
"""

from __future__ import annotations

import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8080,
        loop="asyncio",
        reload=False,
    )
