from app import db


class Supplier(db.Model):
    """
    supplier table fields for database mapping
    """
    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.String(200))

    def __repr__(self):  # changes output of object when called
        return f"{self.supplier}"


class BuildPhase(db.Model):
    """
    build phase table fields for database mapping
    """
    id = db.Column(db.Integer, primary_key=True)
    build_phase = db.Column(db.String(200))

    def __repr__(self):  # changes output of object when called
        return f"{self.build_phase}"


class PartNumber(db.Model):
    """
    part number table fields for database mapping
    """
    id = db.Column(db.Integer, primary_key=True)
    part_number = db.Column(db.String(200))

    def __repr__(self):  # changes output of object when called
        return f"{self.part_number}"
