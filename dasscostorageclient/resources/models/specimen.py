from pydantic import BaseModel, Field


class Specimen(BaseModel):
    institution: str | None
    collection: str | None
    barcode: str
    pid: str = Field(alias='specimen_pid')
    preparation_type: str
