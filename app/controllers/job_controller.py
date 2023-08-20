from flask import Blueprint, render_template
from app.models.emote_processing_job import EmoteProcessingJob

job_bp = Blueprint('job', __name__, url_prefix='/jobs')


@job_bp.route('/jobs/emotes', methods=['GET'])
def list_emote_processing_jobs():
    emote_processing_jobs = EmoteProcessingJob.get_all()
    return render_template('jobs.html', jobs=emote_processing_jobs)
