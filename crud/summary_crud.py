from typing import List, Optional, Any

from sqlmodel import Session, select
from sqlmodel.ext.asyncio.session import AsyncSession

from models.summaries import Summary


def create_summary(db: Session, summary: Summary):
    db.add(summary)
    db.commit()
    db.refresh(summary)
    return summary
