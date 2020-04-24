from flask import (Blueprint, Response, flash, redirect, render_template,
                   request, url_for)

from app.aws_s3 import AwsS3

from .models import BuildPhase, PartNumber, Supplier
from .services import file_type

docs = Blueprint("docs", __name__)
s3 = AwsS3("documentportal123")


@docs.route("/")
def index():
    """
    get all input variables from db and import to form
    """
    part_number = PartNumber.query.all()
    build_phase = BuildPhase.query.all()
    supplier = Supplier.query.all()

    return render_template(
        "index.html",
        part_number=part_number,
        build_phases=build_phase,
        suppliers=supplier,
    )


@docs.route("/files")
def files() -> Response:
    """
    get all files held in bucket
    """
    s3_files = s3.get_s3_files()
    return render_template("files.html", files=s3_files)


@docs.route("/upload", methods=["POST"])
def upload() -> Response:
    """
    upload new file to s3 bucket
    """
    file = request.files["file"]
    part_number = request.form["part_number"]
    build_phase = request.form["build_phase"]
    supplier = request.form["supplier"]

    s3_upload = s3.upload_file(file, part_number, build_phase, supplier)
    if s3_upload:
        flash("File upload complete")
    return redirect(url_for("docs.files"))


@docs.route("/delete", methods=["POST"])
def delete():
    """
    delete file from s3 bucket
    """
    key = request.form["key"]
    s3_delete = s3.delete_file(key)

    if s3_delete:
        flash(f"{key} deleted")
    return redirect(url_for("docs.files"))


@docs.route("/download", methods=["POST"])
def download():
    """
    download file from s3 bucket
    """
    key = request.form["key"]
    file_object = s3.download_file(key)

    return Response(
        file_object["Body"].read(),
        mimetype=file_type(key),
        headers={"Content-Disposition": f"attachment;filename={key}"},
    )
