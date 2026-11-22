# https://docs.python.org/3/library/hashlib.html
from dataclasses import dataclass
import datetime
import hashlib
import json


@dataclass(frozen=True)
class Block:
    index: int
    timestamp: str
    description: str
    previous_hash: str
    nonce: int = 0
    hash: str = ""

    def __post_init__(self) -> None:
        if not self.hash:
            object.__setattr__(self, "hash", self.calculate_hash())

    def calculate_hash(self) -> str:
        payload = json.dumps(
            {
                "index": self.index,
                "timestamp": self.timestamp,
                "description": self.description,
                "previous_hash": self.previous_hash,
                "nonce": self.nonce,
            },
            sort_keys=True,
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()


class Blockchain:
    def __init__(self, difficulty: int = 2) -> None:
        self.difficulty = max(0, difficulty)
        self.chain: list[Block] = [self._create_genesis_block()]

    @staticmethod
    def _now_iso() -> str:
        return datetime.datetime.now(datetime.timezone.utc).isoformat()

    def _create_genesis_block(self) -> Block:
        return Block(
            index=0,
            timestamp=self._now_iso(),
            description="Genesis Block",
            previous_hash="0" * 64,
        )

    def add_block(self, description: str) -> Block:
        if not description.strip():
            raise ValueError("Block description must be non-empty.")

        previous_block = self.chain[-1]
        prefix = "0" * self.difficulty
        nonce = 0

        while True:
            candidate = Block(
                index=previous_block.index + 1,
                timestamp=self._now_iso(),
                description=description,
                previous_hash=previous_block.hash,
                nonce=nonce,
            )
            if candidate.hash.startswith(prefix):
                self.chain.append(candidate)
                return candidate
            nonce += 1

    def is_valid(self) -> bool:
        prefix = "0" * self.difficulty
        for i, block in enumerate(self.chain):
            if block.index != i:
                return False
            if block.hash != block.calculate_hash():
                return False
            if not block.hash.startswith(prefix):
                return False
            if i > 0 and block.previous_hash != self.chain[i - 1].hash:
                return False
        return True


if __name__ == "__main__":
    my_blockchain = Blockchain(difficulty=2)
    my_blockchain.add_block("Laptop")
    my_blockchain.add_block("Passport")

    for block in my_blockchain.chain:
        print(
            f"[{block.index}] {block.timestamp} | {block.description} | "
            f"nonce={block.nonce} | hash={block.hash[:16]}..."
        )

    print("Chain valid:", my_blockchain.is_valid())
