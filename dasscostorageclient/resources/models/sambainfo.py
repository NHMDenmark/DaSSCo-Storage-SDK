from pydantic import BaseModel, Field


class SambaInfo(BaseModel):
    port: int | None
    hostname: str | None
    smb_name: str | None
    token: str | None
    samba_request_status: str | None = Field(alias='sambaRequestStatus')
    samba_request_status_message: str | None = Field(alias='sambaRequestStatusMessage')
