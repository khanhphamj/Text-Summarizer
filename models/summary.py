from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from datetime import datetime


class SummaryBase(SQLModel):
    # The date time of the summary
    datetime: datetime

    # Main content of the summary
    main_content: Optional[str]

    # Summarizer of the main content
    summarizer: Optional[str]

    # The rating of the summary
    rating: Optional[int]

    def __getitem__(self, item):
        return getattr(self, item)

    class Config:
        from_attributes = True


class Summary(SummaryBase, table=True):
    __tablename__ = 'summary'

    id: str = Field(primary_key=True)


Summary.model_rebuild()
