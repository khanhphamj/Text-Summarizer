from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import LONGTEXT


class Summary(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    datetime: datetime
    main_content: str = Field(sa_column=Column(LONGTEXT))
    summarizer: str = Field(sa_column=Column(LONGTEXT))
    rating: Optional[int] = None