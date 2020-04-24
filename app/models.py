from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def dbinit(sample_data):
    db.create_all()

    if sample_data:
        part1 = PartNumber("01234")
        db.session.add(part1)
        supplier1 = Supplier("Test1")
        db.session.add(supplier1)
        build_phase1 = BuildPhase("Phase 1")
        db.session.add(build_phase1)

    db.session.commit()


class Supplier(db.Model):
    """
    supplier table fields for database mapping
    """

    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.String(200))

    def __init__(self, supplier):
        self.supplier = supplier

    def __repr__(self):  # changes output of object when called
        return f"{self.supplier}"


class BuildPhase(db.Model):
    """
    build phase table fields for database mapping
    """

    id = db.Column(db.Integer, primary_key=True)
    build_phase = db.Column(db.String(200))

    def __init__(self, build_phase):
        self.build_phase = build_phase

    def __repr__(self):  # changes output of object when called
        return f"{self.build_phase}"


class PartNumber(db.Model):
    """
    part number table fields for database mapping
    """

    id = db.Column(db.Integer, primary_key=True)
    part_number = db.Column(db.String(200))

    def __init__(self, part_number):
        self.part_number = part_number

    def __repr__(self):  # changes output of object when called
        return f"{self.part_number}"
