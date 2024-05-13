from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from datetime import datetime


class Summary(SQLModel, table=True):
    __tablename__ = "summaries"
    id: Optional[str] = Field(default=None, primary_key=True)
    
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


Summary.model_rebuild()
