class BrowserHistory:

    def __init__(self, homepage: str):
        self.A = [homepage]
        self.i = 0

    def visit(self, url: str) -> None:
        self.i += 1
        self.A = self.A[:self.i]
        self.A.append(url)

    def back(self, steps: int) -> str:
        self.i = max(0, self.i - steps)
        return self.A[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, len(self.A) - 1)
        return self.A[self.i]


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.bound = 0 # we need to clear all the forward history

    def visit(self, url: str) -> None:
        self.curr += 1
        if self.curr == len(self.history):
            self.history.append(url)
        else:
            self.history[self.curr] = url
        self.bound = self.curr

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.bound)
        return self.history[self.curr]