class Alert:
    def __init__(self, account_id) -> None:
        self.account_id = account_id

    def __str__(self) -> str:
        return f"!!! Alert !!! Account {self.account_id} seems suspicious !"