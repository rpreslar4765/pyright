from _typeshed import Incomplete

class ShardManifest:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, id: Incomplete | None = ..., shard_owners: Incomplete | None = ...) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id) -> None: ...
    @property
    def shard_owners(self): ...
    @shard_owners.setter
    def shard_owners(self, shard_owners) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...