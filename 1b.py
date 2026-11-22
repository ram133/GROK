"""
Minimal educational blockchain with Proof-of-Work.

Based on the classic structure shown in the Python docs examples
and many tutorials. Not intended for production use.
"""

from __future__ import annotations

import datetime
import hashlib
import json
from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class Block:
    index: int
    timestamp: str
    description: str
    previous_hash: str
    nonce: int = 0
    hash: str = field(default="", compare=False)

    def __post_init__(self) -> None:
        if not self.hash:
            object.__setattr__(self, "hash", self.calculate_hash())

    def calculate_hash(self) -> str:
        """Deterministic SHA-256 of the block contents (excluding the hash itself)."""
        payload = {
            "index": self.index,
            "timestamp": self.timestamp,
            "description": self.description,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
        }
        # sort_keys makes the JSON canonical
        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
        return hashlib.sha256(encoded).hexdigest()

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def __repr__(self) -> str:
        return (
            f"Block(index={self.index}, desc={self.description!r}, "
            f"nonce={self.nonce}, hash={self.hash[:16]}…)"
        )


class Blockchain:
    def __init__(self, difficulty: int = 2) -> None:
        if not isinstance(difficulty, int) or difficulty < 0:
            raise ValueError("difficulty must be a non-negative integer")
        self.difficulty = difficulty
        self.chain: list[Block] = []
        self._mine_and_append(
            index=0,
            description="Genesis Block",
            previous_hash="0" * 64,
        )

    @staticmethod
    def _now_iso() -> str:
        return datetime.datetime.now(datetime.timezone.utc).isoformat()

    def _mine_and_append(
        self,
        index: int,
        description: str,
        previous_hash: str,
    ) -> Block:
        """Mine a block that satisfies the current difficulty and append it."""
        prefix = "0" * self.difficulty
        nonce = 0

        while True:
            candidate = Block(
                index=index,
                timestamp=self._now_iso(),
                description=description,
                previous_hash=previous_hash,
                nonce=nonce,
            )
            if candidate.hash.startswith(prefix):
                self.chain.append(candidate)
                return candidate
            nonce += 1

    def add_block(self, description: str) -> Block:
        description = description.strip()
        if not description:
            raise ValueError("Block description must be non-empty")

        previous = self.chain[-1]
        return self._mine_and_append(
            index=previous.index + 1,
            description=description,
            previous_hash=previous.hash,
        )

    def is_valid(self) -> bool:
        """Full integrity check of the chain."""
        prefix = "0" * self.difficulty

        for i, block in enumerate(self.chain):
            # Index must be sequential
            if block.index != i:
                return False

            # Hash must be correct for the current contents
            if block.hash != block.calculate_hash():
                return False

            # Proof-of-work must be satisfied
            if not block.hash.startswith(prefix):
                return False

            # Link to previous block must be correct
            if i > 0 and block.previous_hash != self.chain[i - 1].hash:
                return False

        return True

    def print_chain(self, hash_preview: int = 16) -> None:
        """Pretty-print the whole chain."""
        for block in self.chain:
            print(
                f"[{block.index:3d}] {block.timestamp} | "
                f"{block.description:<20} | "
                f"nonce={block.nonce:<6} | "
                f"hash={block.hash[:hash_preview]}…"
            )
        print(f"\nChain valid: {self.is_valid()}")


if __name__ == "__main__":
    bc = Blockchain(difficulty=3)          # a bit harder than the original

    bc.add_block("Laptop")
    bc.add_block("Passport")
    bc.add_block("House keys")

    bc.print_chain()