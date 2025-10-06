from pydantic import BaseModel, Field

class SpecimenModel(BaseModel):
    institution: str | None
    collection: str | None
    barcode: str | None
    specimen_pid: str | None
    preparation_types: list[str]
    specimen_id: int | None
    role_restriction: list[str]

class AssetSpecimenModel(BaseModel):
    specimen_id: int | None
    specimen_pid: str | None
    asset_guid: str | None
    specimen_pid: str | None
    asset_preparation_type: str | None
    asset_detached: bool
    specify_collection_object_attachment_id: int | None
    specimen: SpecimenModel | None