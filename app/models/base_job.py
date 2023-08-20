from enum import Enum

from app import db

from .base_model import BaseModel


class JobStatus(Enum):
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"
    FAILED = "failed"


class BaseJob(BaseModel):
    __abstract__ = True

    job_name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum(JobStatus), nullable=False)

    def set_in_progress(self):
        self.status = JobStatus.IN_PROGRESS.value

    def set_completed(self):
        self.status = JobStatus.COMPLETED.value

    def set_failed(self):
        self.status = JobStatus.FAILED.value

    def is_in_progress(self) -> bool:
        return self.status == JobStatus.IN_PROGRESS.value

    def is_completed(self) -> bool:
        return self.status == JobStatus.COMPLETED.value

    def is_failed(self) -> bool:
        return self.status == JobStatus.FAILED.value
