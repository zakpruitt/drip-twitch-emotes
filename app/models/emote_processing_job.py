from app import db

from models.base_job import BaseJob


class EmoteProcessingJob(BaseJob):
    unprocessed_emote_url = db.Column(db.String(500), nullable=True)
    author_id = db.Column(db.Integer, nullable=False)
